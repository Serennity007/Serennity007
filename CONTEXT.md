# CONTEXT

个人 GitHub 主页（本仓库）的领域术语与口径。任何对 README / 资产的修改都必须遵守这里定义的词汇，禁止引入口径之外的新数字。

## 术语表

- **主页 (Profile README)**：本仓库的 README，渲染在 `github.com/Serennity007` 个人页顶部。与 **Portfolio 网站**（`Serennity007/liangzhengtao-portfolio` 仓库，`serennity007.github.io/liangzhengtao-portfolio`）是两个独立资产，风格与口径必须保持一致。
- **受众 (Audience)**：首要 = 实习/校招 HR 与面试官（须在 30 秒内抓住亮点）；次要 = 开源社区用户与学术合作者。内容取舍以首要受众为准。
- **CLI 工具 (CLI Tools)**：特指发布到 npm 的 4 个命令行工具：`git-format`、`ai-commit`、`agent-trace`、`vibe-check`。页面中"工具"一词默认指这 4 个。
- **仓库总数 (Repo Count)**：GitHub 公开仓库的实时数量（2026-08-29 为 324）。展示规则：README 徽章、typing 动画、仓库描述使用实时数字；偏离展示值 ±10 以上时更新所有引用处。
- **精选项目 (Curated Projects)**：手工挑选进入 README 的项目。入选标准：与受众的相关性 > star 数。分两层：4 个 CLI 工具（首屏）+ 10 个代表仓库（折叠区）。
- **口径 (Canonical Numbers)**：`324 个开源仓库 · 4 个 npm CLI 工具 · 285+ AI prompts`。所有资产（README、terminal.svg、仓库描述、Portfolio 网站）只能使用这一套数字。历史数字 `45+ / 60+ / 300+ / 33` 已废弃，不得再出现。
- **语言版本 (Language Versions)**：仅 `README.md`（英文，默认）与 `README.zh.md`（中文）。见 ADR 0001。

## 历史决策

- [ADR 0001 — 语言版本精简为 EN + ZH](docs/adr/0001-language-reduction-en-zh.md)
