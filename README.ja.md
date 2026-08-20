[English](README.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md)

# こんにちは、Zhengtao です 👋

### AI 開発の面倒な部分を自動化する CLI ツールを作っています。

Git ワークフロー、エージェント監視、プロジェクト監査、コミット生成を処理するオープンソースツールを開発しています。開発に集中できるように、管理作業を自動化します。

[![npm downloads (git-format)](https://img.shields.io/npm/dm/git-format?label=git-format&style=flat-square)](https://www.npmjs.com/package/git-format)
[![npm downloads (ai-commit)](https://img.shields.io/npm/dm/ai-commit?label=ai-commit&style=flat-square)](https://www.npmjs.com/package/ai-commit)
[![npm downloads (agent-trace)](https://img.shields.io/npm/dm/agent-trace?label=agent-trace&style=flat-square)](https://www.npmjs.com/package/agent-trace)
[![GitHub followers](https://img.shields.io/github/followers/liangzhengtao?style=flat-square)](https://github.com/liangzhengtao)

---

## ⚡ 今すぐ 10 秒で試す

クローン不要。API キー不要。設定不要。そのまま実行。

```bash
# めちゃくちゃな Git 履歴を Conventional Commits に整形
npx git-format

# ステージした変更から AI がコミットメッセージを生成
npx ai-commit

# プロジェクトの AI 対応度をスコアリング（0-100）
npx @liangzhengtao/vibe-check
```

一つ選んで、貼り付けるだけ。すぐに結果が見えます。

---

## 🔧 作っているもの

**オリジナル CLI ツール** — インストールして実行。ベンダーロックインなし。

| ツール | 概要 | インストール |
|--------|------|-------------|
| **[git-format](https://github.com/liangzhengtao/git-format)** | めちゃくちゃなコミット履歴を[Conventional Commits](https://www.conventionalcommits.org/)に変換 | `npx git-format` |
| **[ai-commit](https://github.com/liangzhengtao/ai-commit)** | `git diff` から AI がコミットメッセージを生成 | `npx ai-commit` |
| **[agent-trace](https://github.com/liangzhengtao/agent-trace)** | AI エージェントのコスト・トークン・ツール呼び出し・セッションタイムラインを追跡 | `npx agent-trace` |
| **[vibe-check](https://github.com/liangzhengtao/vibe-check)** | リポジトリの AI コーディングアシスタント対応度を監査（0-100 スコア） | `npx @liangzhengtao/vibe-check` |

**キュレーテッドコレクション** — 実戦で検証済みの設定とリソース。

| コレクション | 内容 |
|-------------|------|
| **[awesome-ai-rules](https://github.com/liangzhengtao/awesome-ai-rules)** | Cursor・Claude・Kimi Code 向け 20 のプロダクション AI コーディングルール |
| **[awesome-mcp-servers](https://github.com/liangzhengtao/awesome-mcp-servers)** | 実際の AI アシスタントで検証済みの MCP サーバー設定 9 件 |
| **[awesome-prompts](https://github.com/liangzhengtao/awesome-prompts)** | コーディング・執筆・研究・クリエイティブ向け 285+ の AI プロンプト |

---

## 📂 全プロジェクト（33 件）

<details>
<summary><strong>AI 開発ツール（6 件）</strong></summary>

| プロジェクト | 概要 |
|-------------|------|
| [agent-trace](https://github.com/liangzhengtao/agent-trace) | AI エージェントを追跡 — コスト・トークン・ツール健全性・セッションタイムライン |
| [awesome-ai-rules](https://github.com/liangzhengtao/awesome-ai-rules) | 20 のプロダクション AI コーディングルール（Cursor・Claude・Kimi Code） |
| [vibe-check](https://github.com/liangzhengtao/vibe-check) | プロジェクトの AI 対応度をスコアリング（0-100） |
| [commit-ai](https://github.com/liangzhengtao/ai-commit) | AI がコミットメッセージを生成、API キー不要 |
| [awesome-mcp-servers](https://github.com/liangzhengtao/awesome-mcp-servers) | AI コーディングアシスタント向け検証済み MCP サーバー 9 件 |
| [awesome-ai-agents](https://github.com/liangzhengtao/awesome-ai-agents) | プロダクション AI エージェント構築のための 12 スキル |

</details>

<details>
<summary><strong>研究・キャリア（7 件）</strong></summary>

| プロジェクト | 概要 |
|-------------|------|
| [awesome-skills](https://github.com/liangzhengtao/awesome-skills) | 12 の研究スキル（LaTeX・統計・文献レビュー） |
| [awesome-research-figures](https://github.com/liangzhengtao/awesome-research-figures) | 出版品質の科学図表 |
| [awesome-interview-skills](https://github.com/liangzhengtao/awesome-interview-skills) | 理想の職を得るための 14 スキル |
| [system-design-interview](https://github.com/liangzhengtao/system-design-interview) | ASCII ダイアグラム付きシステム設計面接対策 |
| [awesome-developer-roadmap](https://github.com/liangzhengtao/awesome-developer-roadmap) | 10 のキャリアロードマップ（ジュニア→スタッフ） |
| [build-your-own-x-cn](https://github.com/liangzhengtao/build-your-own-x-cn) | 技術をゼロから構築（10 チュートリアル、中国語） |
| [leetcode-patterns-cn](https://github.com/liangzhengtao/leetcode-patterns-cn) | 8 アルゴリズムパターン、72 問題（中国語） |

</details>

<details>
<summary><strong>動画・クリエイティブ（7 件）</strong></summary>

| プロジェクト | 概要 |
|-------------|------|
| [awesome-video-prompts](https://github.com/liangzhengtao/awesome-video-prompts) | Sora・Runway・Pika・Kling 向け 200+ のプロンプト |
| [awesome-video-to-text](https://github.com/liangzhengtao/awesome-video-to-text) | 転写・ノート・字幕の 12 スキル |
| [awesome-video-creation](https://github.com/liangzhengtao/awesome-video-creation) | 動画制作フルワークフローの 14 スキル |
| [awesome-video-skills](https://github.com/liangzhengtao/awesome-video-skills) | 動画編集の 10 スキル |
| [awesome-creative-skills](https://github.com/liangzhengtao/awesome-creative-skills) | クリエイティブ 10 スキル（ポスター・ロゴ・写真） |
| [awesome-writing-skills](https://github.com/liangzhengtao/awesome-writing-skills) | 執筆 12 スキル（ブログ・SEO・コピーライティング） |
| [awesome-prompts](https://github.com/liangzhengtao/awesome-prompts) | あらゆるタスク向け 285+ の AI プロンプト |

</details>

<details>
<summary><strong>開発者リソース（8 件）</strong></summary>

| プロジェクト | 概要 |
|-------------|------|
| [awesome-dev-tools](https://github.com/liangzhengtao/awesome-dev-tools) | カテゴリ別 50+ の開発者ツール |
| [awesome-devops-skills](https://github.com/liangzhengtao/awesome-devops-skills) | 12 の DevOps スキル（CI/CD・K8s・クラウド） |
| [awesome-security-skills](https://github.com/liangzhengtao/awesome-security-skills) | 12 のサイバーセキュリティスキル |
| [awesome-startup-skills](https://github.com/liangzhengtao/awesome-startup-skills) | ファウンダー向け 12 スキル |
| [ai-agent-architectures](https://github.com/liangzhengtao/ai-agent-architectures) | プロダクションコード付き AI エージェントアーキテクチャ 7 パターン |
| [open-source-llm-guide](https://github.com/liangzhengtao/open-source-llm-guide) | 自身のハードウェアで LLM を実行 |
| [github-stars-analysis](https://github.com/liangzhengtao/github-stars-analysis) | GitHub スターのトレンド分析 |
| [awesome-chinese-developer-tools](https://github.com/liangzhengtao/awesome-chinese-developer-tools) | 中国語開発者ツール（8 カテゴリ） |

</details>

<details>
<summary><strong>個人プロジェクト（4 件）</strong></summary>

| プロジェクト | 概要 |
|-------------|------|
| [my-dotfiles](https://github.com/liangzhengtao/my-dotfiles) | 開発環境設定（Zsh・Git・VS Code・Neovim） |
| [guizhou-exam-papers](https://github.com/liangzhengtao/guizhou-exam-papers) | 貴州省の過去問（学生向け無料） |
| [blog](https://github.com/liangzhengtao/blog) | 技術ブログ |
| [git-format](https://github.com/liangzhengtao/git-format) | Git コミットを Conventional Commits にフォーマット |

</details>

---

## 💬 こんな使い方をしています

```bash
# PR 前 — コミット履歴をきれいに
git rebase -i main
npx git-format

# 開発中 — コミットメッセージを AI に任せる
git add .
npx ai-commit

# オンボーディング — リポジトリの AI 対応度をチェック
git clone <repo> && cd <repo>
npx @liangzhengtao/vibe-check

# デバッグ — AI エージェントの実際の動作を確認
npx agent-trace --last-session
```

---

## 🤝 つながる

- **GitHub**: [liangzhengtao](https://github.com/liangzhengtao) — 新ツールのリリースをフォロー
- **Blog**: [liangzhengtao/blog](https://github.com/liangzhengtao/blog) — 技術ブログ

---

**注目のツール 7 件。全 33 プロジェクト。すべてオープンソース。**

役に立ったなら、一番使ったリポジトリに [スターを付けてください](https://github.com/liangzhengtao/git-format)。
