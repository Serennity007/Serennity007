#!/usr/bin/env python3
"""Generate a chibi capybara "eating" the GitHub contribution calendar as an animated SVG.

Usage:
  GH_TOKEN=<token> python3 generate_animal_snake.py --user Serennity007 \
      --theme dark --out dist --out-name animal-snake-dark

No third-party dependencies: GraphQL via urllib, SVG via string building.
Animation is pure SMIL so it survives GitHub's camo image proxy.
"""
import argparse
import json
import os
import urllib.request

# ---------------------------------------------------------------- calendar

QUERY = """
query($u:String!){
  user(login:$u){
    contributionsCollection{ contributionCalendar{
      weeks{ contributionDays{ date contributionCount } }
    } }
  }
}"""


def fetch_weeks(user: str) -> list:
    token = os.environ["GH_TOKEN"]
    body = json.dumps({"query": QUERY, "variables": {"u": user}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "animal-snake-generator",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if "errors" in data:
        raise SystemExit(f"GraphQL error: {data['errors']}")
    return data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]


# ---------------------------------------------------------------- palette

THEMES = {
    "dark": {
        "empty": "#1b2129",
        "trail": "#263041",
        "greens": ["#0e4429", "#006d32", "#26a641", "#39d353"],
    },
    "light": {
        "empty": "#ebedf0",
        "trail": "#dbe3ea",
        "greens": ["#9be9a8", "#40c463", "#30a14e", "#216e39"],
    },
}

CELL = 12          # cell size
GAP = 3            # gap between cells
STEP = CELL + GAP  # 15
PAD_X, PAD_Y = 24, 34


def level_color(count: int, theme: dict) -> str:
    if count <= 0:
        return theme["empty"]
    greens = theme["greens"]
    return greens[min((count - 1) * len(greens) // 8, len(greens) - 1)]


# ---------------------------------------------------------------- path

def build_path_cells(weeks: list) -> list:
    """Cells in serpentine visiting order: (col, row, count)."""
    ncols = len(weeks)
    cells = []
    for r in range(7):
        cols = range(ncols) if r % 2 == 0 else range(ncols - 1, -1, -1)
        for c in cols:
            days = weeks[c]["contributionDays"]
            if r < len(days):
                cells.append((c, r, days[r]["contributionCount"]))
    return cells


# ---------------------------------------------------------------- svg parts

SPRITE = """<g id="capy">
  <g>
    <animateTransform attributeName="transform" type="translate"
      values="0 0;0 -2;0 0" dur="0.7s" repeatCount="indefinite"/>
    <g id="flip">
      <!-- body -->
      <ellipse cx="-5" cy="3" rx="14" ry="10" fill="#b3905e" stroke="#8a6a3f" stroke-width="1.5"/>
      <!-- legs -->
      <rect x="-10" y="10" width="4.5" height="5.5" rx="2" fill="#8a6a3f"/>
      <rect x="0" y="11" width="4.5" height="5" rx="2" fill="#8a6a3f"/>
      <!-- head (boxy capybara snout) -->
      <rect x="4" y="-11" width="21" height="16" rx="7" fill="#b3905e" stroke="#8a6a3f" stroke-width="1.5"/>
      <!-- ear -->
      <circle cx="9" cy="-11.5" r="3" fill="#8a6a3f"/>
      <!-- snout patch -->
      <rect x="19" y="-5" width="7" height="8" rx="3" fill="#c9a876"/>
      <circle cx="23" cy="-1.5" r="1.1" fill="#5e4426"/>
      <!-- eye + glint -->
      <circle cx="14" cy="-4.5" r="1.9" fill="#2b1d0e"/>
      <circle cx="14.7" cy="-5.2" r="0.65" fill="#ffffff"/>
      <!-- blush -->
      <ellipse cx="10.5" cy="0.5" rx="2.7" ry="1.5" fill="#e8a8a0" opacity="0.65"/>
      <!-- the green cell it is nibbling -->
      <g>
        <rect x="25" y="1.5" width="7.5" height="7.5" rx="1.6" fill="#39d353" stroke="#1a7f37" stroke-width="1"/>
        <animate attributeName="opacity" values="1;1;0.75;1" dur="0.6s" repeatCount="indefinite"/>
      </g>
    </g>
  </g>
</g>"""


def generate(user: str, theme_name: str) -> str:
    theme = THEMES[theme_name]
    weeks = fetch_weeks(user)
    ncols = len(weeks)
    cells = build_path_cells(weeks)
    n = len(cells)

    width = PAD_X * 2 + ncols * STEP - GAP
    height = PAD_Y * 2 + 7 * STEP - GAP
    T = max(8.0, round(n * 0.045, 1))  # total loop seconds

    # grid cells
    grid = []
    for c in range(ncols):
        for r in range(len(weeks[c]["contributionDays"])):
            cnt = weeks[c]["contributionDays"][r]["contributionCount"]
            x = PAD_X + c * STEP
            y = PAD_Y + r * STEP
            grid.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2.5" '
                f'fill="{level_color(cnt, theme)}"/>'
            )

    # motion path (serpentine, cell-center to cell-center)
    pts = [
        (PAD_X + c * STEP + CELL / 2, PAD_Y + r * STEP + CELL / 2)
        for (c, r, _) in cells
    ]
    d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f} " + " ".join(
        f"L {x:.1f} {y:.1f}" for x, y in pts[1:]
    )

    # flip (face travel direction): discrete scale.x at row boundaries
    flips, key_times = [], ["0"]
    row_start = {}
    for i, (c, r, _) in enumerate(cells):
        row_start.setdefault(r, i)
    for r in range(7):
        f = row_start[r] / n
        flips.append("1 1" if r % 2 == 0 else "-1 1")
        if r > 0:
            key_times.append(f"{f:.4f}")
    key_times.append("1")
    # SMIL requires len(values) == len(keyTimes): repeat the last flip to fill
    flips = flips + [flips[-1]] * (len(key_times) - len(flips))
    flip_anim = (
        f'<animateTransform attributeName="transform" type="scale" '
        f'calcMode="discrete" values="{";".join(flips)}" '
        f'keyTimes="{";".join(key_times)}" dur="{T}s" repeatCount="indefinite"/>'
    )

    # trail/eat overlays, timed to when the capybara passes each cell
    eats = []
    for i, (c, r, cnt) in enumerate(cells):
        t = (i + 0.6) / n
        x = PAD_X + c * STEP
        y = PAD_Y + r * STEP
        # eaten cells dissolve into the trail color (snake-style erase)
        overlay = theme["trail"]
        op = "1"
        eats.append(
            f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2.5" '
            f'fill="{overlay}" opacity="0">'
            f'<animate attributeName="opacity" values="0;0;{op};{op}" '
            f'keyTimes="0;{t:.4f};{min(t + 0.012, 1):.4f};1" '
            f'dur="{T}s" repeatCount="indefinite"/></rect>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"
  viewBox="0 0 {width} {height}" role="img" aria-label="Chibi capybara eating the GitHub contribution calendar of {user}">
  <defs><path id="walk" d="{d}"/></defs>
  {"".join(grid)}
  {"".join(eats)}
  <g>
    <animateMotion dur="{T}s" repeatCount="indefinite" rotate="0">
      <mpath href="#walk"/>
    </animateMotion>
    <g transform="scale(1)">
      {flip_anim.replace("<animateTransform", "<g><animateTransform", 1).replace('repeatCount="indefinite"/>', 'repeatCount="indefinite"/></g>', 1) if False else ""}
    </g>
    {SPRITE.replace('<g id="flip">', '<g id="flip">' + flip_anim, 1)}
  </g>
</svg>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", required=True)
    ap.add_argument("--theme", choices=THEMES, required=True)
    ap.add_argument("--out", default="dist")
    ap.add_argument("--out-name", required=True)
    args = ap.parse_args()
    svg = generate(args.user, args.theme)
    os.makedirs(args.out, exist_ok=True)
    path = os.path.join(args.out, f"{args.out_name}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {path} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
