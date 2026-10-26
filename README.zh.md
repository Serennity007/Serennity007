[English](README.md) | [中文](README.zh.md)

<img src=".github/terminal.svg" width="100%" alt="Zhengtao Liang · AI research and open-source engineering" />

# 梁正涛 | AI 研究与开源工程

**北京理工大学**智能科学与技术硕士在读（2026 级），研究方向为智能体协作研究、智能体安全、多模态大模型安全研究，同时开发 AI 工具和应用系统。

**KSEM（CCF-C）会议论文已中稿** · 华为 ICT 大赛国家一等奖

[作品集](https://serennity007.github.io/Serennity007-portfolio/) · [中文简历](https://serennity007.github.io/Serennity007-portfolio/resume.html) · [English Resume](https://serennity007.github.io/Serennity007-portfolio/resume-en.html) · [Email](mailto:1392452425a@gmail.com)

直接下载：[中文 PDF](https://serennity007.github.io/Serennity007-portfolio/assets/resumes/Liang-Zhengtao-Resume-ZH.pdf) · [English PDF](https://serennity007.github.io/Serennity007-portfolio/assets/resumes/Liang-Zhengtao-Resume-EN.pdf)

## 科研与背景

- **KSEM · CCF-C**: 会议论文已中稿。[CCF 会议分类](https://www.ccf.org.cn/c/2017-04-25/592085.shtml)。
- **研究方向**: 智能体协作研究、智能体安全、多模态大模型安全研究。
- **教育背景**: 贵州大学人工智能本科，专业排名 **1/69**，GPA **4.14/5**；北京理工大学硕士在读。
- **荣誉与交流**: 国家奖学金；华为 ICT 国家一等奖；新加坡国立大学交流；雅思 6.5。

## 重点项目：AI 选股与量化投研工具链

**[41 Stars · 8 Forks（2026-10-24）](https://github.com/Serennity007/awesome-stock-quant-skills)**

- 自主开发 30 个原创 Agent Skills、32 个 Python 脚本，实现 23 套投资方法参考框架，覆盖价值、成长、动量、宏观周期与资产配置。
- 串联财务筛选、因子评分、跨框架共识与含成本回测，输出分项得分、换手、持仓明细和输入哈希。
- 功能验证：40 项本地测试通过（2026-10-25）；一条命令运行离线示例，生成报告、CSV 与日志。
- 真实取数：2026-10-24 使用 AKShare 1.19.3 完成 600519 筛选，覆盖 2021–2025 年报。
- [项目拆解与实测](https://serennity007.github.io/Serennity007-portfolio/project-quant.html) · [运行离线演示](https://github.com/Serennity007/awesome-stock-quant-skills/blob/main/docs/quickstart.md) · [验证记录](https://github.com/Serennity007/awesome-stock-quant-skills/blob/main/docs/validation.md) · [真实取数原始记录](https://github.com/Serennity007/awesome-stock-quant-skills/blob/c46da26575289ddaab5587d31e7f718f9ac22a2e/examples/verification/2026-10-24/buffett-check.json)

## 代表项目

精选具备具体功能、源码或可复用工作流的项目。

| 项目 | 做了什么 | 技术栈 |
|---|---|---|
| **[AI 选股与量化投研工具链](https://github.com/Serennity007/awesome-stock-quant-skills)**<br>`awesome-stock-quant-skills` | 默认分支包含 30 个原创 Skill，覆盖财务筛选、共识排序与含成本回测；41 Stars / 8 Forks（截至 2026-10-24），附真实数据实跑和 40 项本地测试记录（2026-10-25）。 | Python · akshare · pandas · Agent Skills |
| **[GhostTrack · IP 与域名信息查询工作台](https://github.com/Serennity007/GhostTrack)** | 基于 GhostTrack 扩展 Windows、Android 与 Web 工作台，整合 IP/ASN、RDAP、DNS、HTTPS/TLS 查询，支持来源状态、快照对比、脱敏和报告导出。 | Python · Tkinter · Android · Web |
| **[XSS Audit Desktop · 源码安全审查工作台](https://github.com/Serennity007/xss-audit-desktop)** | 基于 xss-audit 审计方法扩展双语桌面端与 CLI，支持本地及公开 GitHub 导入、JS/TS/Python AST 证据、人工分诊与 HTML/SARIF 报告。 | Python · Tree-sitter · Tkinter · SARIF |
| **[AI Agent 会话分析 CLI](https://github.com/Serennity007/agent-trace)**<br>`agent-trace` | 解析多种编码 Agent 的本地会话日志，汇总 token 用量、成本估算与工具调用；提供终端报告与 JSON 输出。 | Node.js · JavaScript · CLI |
| **[财经 RSS 阅读器与摘要工具](https://github.com/Serennity007/serenity-stock-rss)**<br>`serenity-stock-rss` | 基于 Qiaomu AI RSS 改造 Obsidian 财经阅读器，内置 45 个源，支持文章转 Markdown、日记摘录与 OPML；另开发飞书摘要工具，支持消息去重、分组卡片和分批发送。 | TypeScript · Obsidian API · Node.js |

[仓库分类索引](https://github.com/Serennity007/repo-catalog) · [全部仓库](https://github.com/Serennity007/?tab=repositories)

## CLI 工具

| 工具 | 用途 | 使用入口 |
|---|---|---|
| [agent-trace](https://github.com/Serennity007/agent-trace) | 本地 Agent 会话分析 | `npx @liangzhengtao/agent-trace` |
| [git-format](https://github.com/Serennity007/git-format) | 按规则生成规范提交信息 | `npx @liangzhengtao/git-format --dry-run` |
| [ai-commit](https://github.com/Serennity007/ai-commit) | 根据 Git diff 生成提交信息 | `npx @liangzhengtao/commit-ai` |
| [vibe-check](https://github.com/Serennity007/vibe-check) | 检查 AI 编码配置 | `npx @liangzhengtao/vibe-check` |

## 工程能力

**AI / Data**: Python · PyTorch · Transformers · RAG · Milvus · pandas<br>
**Applications**: TypeScript · JavaScript · React · Flask · FastAPI · SQLite<br>
**Workflows**: Git · Node.js CLI · Agent Skills · GitHub Actions

<details>
<summary>GitHub 活跃记录</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/Serennity007/Serennity007@output/animal-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://cdn.jsdelivr.net/gh/Serennity007/Serennity007@output/animal-snake.svg" />
  <img alt="GitHub contribution animation" src="https://cdn.jsdelivr.net/gh/Serennity007/Serennity007@output/animal-snake-dark.svg" width="100%" />
</picture>

</details>

---

科研合作与 AI 工程交流： [1392452425a@gmail.com](mailto:1392452425a@gmail.com).
