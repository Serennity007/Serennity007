[English](README.md) | [中文](README.zh.md)

<img src=".github/terminal.svg" width="100%" alt="Zhengtao Liang · AI research and open-source engineering" />

# 梁正涛 | AI 研究与开源工程

**[开源项目导航](https://github.com/Serennity007/repo-catalog/blob/main/README.zh-CN.md)** · [按用途找工具](https://github.com/Serennity007/repo-catalog/blob/main/README.zh-CN.md#按用途直达) · [全部公开仓库分类](https://github.com/Serennity007/repo-catalog/blob/main/docs/catalog.md)

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

**[31 个原创 Skills · 33 个 Python 脚本](https://github.com/Serennity007/awesome-stock-quant-skills)** — 2026-10-30 核对源码清单。

- 自主开发 31 个原创 Agent Skills、33 个 Python 脚本，实现 23 套投资方法参考框架，覆盖价值、成长、动量、宏观周期与资产配置。
- 串联财务筛选、因子评分、跨框架共识与含成本回测，输出分项得分、换手、持仓明细和输入哈希。
- 项目[验证记录](https://github.com/Serennity007/awesome-stock-quant-skills/blob/main/docs/validation.md)记录了 60 项本地测试通过；一条命令运行离线示例，生成报告、CSV 与日志。
- 真实取数：2026-10-24 使用 AKShare 1.19.3 完成 600519 筛选，覆盖 2021–2025 年报。
- [项目拆解与实测](https://serennity007.github.io/Serennity007-portfolio/project-quant.html) · [运行离线演示](https://github.com/Serennity007/awesome-stock-quant-skills/blob/main/docs/quickstart.md) · [验证记录](https://github.com/Serennity007/awesome-stock-quant-skills/blob/main/docs/validation.md) · [真实取数原始记录](https://github.com/Serennity007/awesome-stock-quant-skills/blob/c46da26575289ddaab5587d31e7f718f9ac22a2e/examples/verification/2026-10-24/buffett-check.json)

<!-- featured-projects:start -->
## 从六个代表项目开始

人工选定的维护重点。首次运行指南列出输入、输出、环境和适用边界。

| 项目 | 解决什么问题 | 开始使用 |
| --- | --- | --- |
| [awesome-stock-quant-skills](https://github.com/Serennity007/awesome-stock-quant-skills) | 把财务筛选、共识排序和含成本回测串成可复核的研究流程。 | [首次运行](https://github.com/Serennity007/repo-catalog/blob/main/docs/projects.md#quant) |
| [xss-audit-desktop](https://github.com/Serennity007/xss-audit-desktop) | 让安全审查保留源码位置、有限流向证据和人工复核结论。 | [首次运行](https://github.com/Serennity007/repo-catalog/blob/main/docs/projects.md#audit) |
| [agent-trace](https://github.com/Serennity007/agent-trace) | 从编码 Agent 的本地日志查看 token、工具调用和成本估算。 | [首次运行](https://github.com/Serennity007/repo-catalog/blob/main/docs/projects.md#agent-trace) |
| [paper-zh-translation](https://github.com/Serennity007/paper-zh-translation) | 在保留论文版面坐标的前提下，把已有中文译文写回 PDF 并检查。 | [首次运行](https://github.com/Serennity007/repo-catalog/blob/main/docs/projects.md#paper) |
| [beiligong-ppt-skill](https://github.com/Serennity007/beiligong-ppt-skill) | 把字号、底色、标题与院标调整变成可复跑的课件改版流程。 | [首次运行](https://github.com/Serennity007/repo-catalog/blob/main/docs/projects.md#ppt) |
| [taotao-futures-research](https://github.com/Serennity007/taotao-futures-research) | 在共同区间、信息时点与样本覆盖明确的条件下比较产业板块。 | [首次运行](https://github.com/Serennity007/repo-catalog/blob/main/docs/projects.md#futures) |

[Portfolio / 作品集](https://serennity007.github.io/Serennity007-portfolio/#featured-projects) · [All projects / 全量索引](https://github.com/Serennity007/repo-catalog)
<!-- featured-projects:end -->

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
