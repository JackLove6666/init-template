# GitHub 本月热榜前100 · 通俗总结

> 数据来源：[https://github.com/trending?since=monthly](https://github.com/trending?since=monthly)  
> 抓取时间：2026-07-24 21:03（UTC: 2026-07-24T21:03:11.623434+00:00）  
> 说明：GitHub 官方月榜单页约20条；本报告按多语言月榜汇总去重后，按本月新增Star排序取前100。

---

## 一句话看懂本月风向

本月 GitHub 最热闹的，几乎都围着 **AI 干活**：AI Agent / 智能体、前端 / Web / UI、视频 / 多媒体 / 会议。
榜首前五是 **OpenMontage**、**graphify**、**codebase-memory-mcp**、**Agent-Reach**、**ai-job-search**，榜首单月新增约 27,748 Star——大家在找「能替人干活的 AI 工具」，而不只是看模型本身。

## 本月热点主题（通俗版）

- **AI Agent / 智能体**（31 个）— 让 AI 自己规划、自己动手，而不是你一句一句喂指令。
- **前端 / Web / UI**（15 个）— 网页界面、用自然语言操控页面。
- **网络 / 通信 / 隐私**（9 个）— 更私密的聊天、更稳的网络连接。
- **视频 / 多媒体 / 会议**（8 个）— 剪视频、开会纪要、语音直播相关。
- **AI 编程助手 / 开发工具**（7 个）— 写代码、改代码、管一堆 Agent 一起干活的工具。
- **数据库 / 存储**（6 个）— 更快的向量库、日志库等基础设施。
- **安全 / 渗透测试**（4 个）— 用 AI 找漏洞、做安全检测。
- **运维 / DevOps / 云**（4 个）— 部署、云原生相关工具。
- **其他开源项目**（4 个）— 不好归类、但本月同样很火的项目。
- **语言 / 框架 / 基础库**（4 个）— 老牌好用的底层库持续被关注。
- **知识库 / RAG / 记忆**（3 个）— 给 AI 装长期记忆，别聊完就忘。
- **大模型 / LLM 基础设施**（3 个）— 提示词、网关、免费模型接入、省 Token 这类「底座」。
- **爬虫 / 数据采集**（2 个）— 帮 AI 或人把网页/社交内容抓干净。

## 语言分布（前100）

| 语言 | 项目数 | 本月新增Star合计 |
|---|---:|---:|
| TypeScript | 20 | 160,631 |
| Python | 19 | 194,182 |
| Go | 19 | 33,400 |
| Rust | 17 | 63,154 |
| JavaScript | 13 | 76,452 |
| Java | 6 | 9,678 |
| C++ | 2 | 2,063 |
| C | 1 | 22,464 |
| C# | 1 | 13,655 |
| CSS | 1 | 12,692 |
| Haskell | 1 | 7,880 |

## Top 10 速览（本月最火）

### 1. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)

- **本月+27,748 ★**｜累计 41,956 ★｜Fork 4,999｜语言 Python
- **通俗说**：把 AI 编程助手变成整套视频制作工作室（多流水线+大量技能包）
- **原简介**：World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- **归类**：AI Agent / 智能体

### 2. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

- **本月+23,835 ★**｜累计 95,183 ★｜Fork 9,219｜语言 Python
- **通俗说**：把代码库/文档/SQL/配置/PDF 变成可查询知识图谱的 Agent Skill
- **原简介**：Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **归类**：知识库 / RAG / 记忆

### 3. [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

- **本月+22,464 ★**｜累计 34,931 ★｜Fork 2,703｜语言 C
- **通俗说**：超快代码知识图谱 MCP，让 AI 查代码少烧 Token
- **原简介**：High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **归类**：知识库 / RAG / 记忆

### 4. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

- **本月+22,184 ★**｜累计 60,591 ★｜Fork 4,873｜语言 Python
- **通俗说**：给 AI 装眼睛：读搜 Twitter/Reddit/B站/小红书等，基本不用付 API 费
- **原简介**：Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.
- **归类**：AI Agent / 智能体

### 5. [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)

- **本月+22,183 ★**｜累计 26,298 ★｜Fork 8,603｜语言 TypeScript
- **通俗说**：跑在本机的 AI 求职框架：筛岗位、改简历、写求职信、准备面试
- **原简介**：The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it.
- **归类**：AI Agent / 智能体

### 6. [stablyai/orca](https://github.com/stablyai/orca)

- **本月+20,972 ★**｜累计 28,277 ★｜Fork 2,004｜语言 TypeScript
- **通俗说**：同时调度一堆编程 Agent 的桌面/手机 ADE
- **原简介**：Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and VPS.
- **归类**：AI Agent / 智能体

### 7. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

- **本月+19,755 ★**｜累计 28,679 ★｜Fork 3,761｜语言 TypeScript
- **通俗说**：免费 AI 网关：一个入口接 200+ 厂商，还能省 Token
- **原简介**：Never stop coding. Free MIT AI gateway: one endpoint, 290+ providers (90+ free), 500+ models — Kimi, Claude, GPT, OpenAI, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 500+ contributors
- **归类**：前端 / Web / UI

### 8. [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut)

- **本月+19,270 ★**｜累计 78,380 ★｜Fork 7,827｜语言 TypeScript
- **通俗说**：开源版剪映（CapCut）替代品
- **原简介**：The open-source CapCut alternative
- **归类**：视频 / 多媒体 / 会议

### 9. [usestrix/strix](https://github.com/usestrix/strix)

- **本月+17,842 ★**｜累计 43,972 ★｜Fork 4,540｜语言 Python
- **通俗说**：开源 AI 渗透测试工具，帮你找应用漏洞
- **原简介**：Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **归类**：安全 / 渗透测试

### 10. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

- **本月+17,643 ★**｜累计 67,233 ★｜Fork 4,623｜语言 JavaScript
- **通俗说**：教 AI 更有审美，少产出千篇一律的「AI 味」内容
- **原简介**：Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop
- **归类**：前端 / Web / UI

## 完整前100名单

| 排名 | 仓库 | 本月+★ | 累计★ | 语言 | 通俗一句话 |
|---:|---|---:|---:|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 27,748 | 41,956 | Python | 把 AI 编程助手变成整套视频制作工作室（多流水线+大量技能包） |
| 2 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 23,835 | 95,183 | Python | 把代码库/文档/SQL/配置/PDF 变成可查询知识图谱的 Agent Skill |
| 3 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 22,464 | 34,931 | C | 超快代码知识图谱 MCP，让 AI 查代码少烧 Token |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 22,184 | 60,591 | Python | 给 AI 装眼睛：读搜 Twitter/Reddit/B站/小红书等，基本不用付 API 费 |
| 5 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | 22,183 | 26,298 | TypeScript | 跑在本机的 AI 求职框架：筛岗位、改简历、写求职信、准备面试 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | 20,972 | 28,277 | TypeScript | 同时调度一堆编程 Agent 的桌面/手机 ADE |
| 7 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 19,755 | 28,679 | TypeScript | 免费 AI 网关：一个入口接 200+ 厂商，还能省 Token |
| 8 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | 19,270 | 78,380 | TypeScript | 开源版剪映（CapCut）替代品 |
| 9 | [usestrix/strix](https://github.com/usestrix/strix) | 17,842 | 43,972 | Python | 开源 AI 渗透测试工具，帮你找应用漏洞 |
| 10 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 17,643 | 67,233 | JavaScript | 教 AI 更有审美，少产出千篇一律的「AI 味」内容 |
| 11 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 16,794 | 92,728 | JavaScript | 让 Claude 用「洞穴人」短句说话，少烧约 65% Token |
| 12 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 14,994 | 60,286 | JavaScript | 汇总各大 AI（Claude/GPT/Gemini/Grok 等）系统提示词泄露内容 |
| 13 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 13,875 | 27,278 | Python | 属于你自己的个人交易 Agent |
| 14 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | 13,655 | 21,905 | C# | 专为 AI Agent 读写 Word/Excel/PPT 的开源 Office 套件（免装 Office） |
| 15 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | 13,587 | 26,446 | Rust | 本地隐私优先的 AI 会议助手：实时转写+说话人分离+总结 |
| 16 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | 13,469 | 46,473 | TypeScript | 开源 AI 语音工作室：克隆声音、听写、创作 |
| 17 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | 13,100 | 20,379 | Rust | 终端里的 Agent 多路复用器，同时盯多个智能体 |
| 18 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | 13,031 | 13,874 | Python | AI 时代伯克希尔：用多 Agent 做价值投资研究（巴菲特等人方法论） |
| 19 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 12,692 | 16,990 | CSS | 反「AI 味」设计技能：让 Claude/Cursor/Codex 做出更有品位的界面 |
| 20 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | 12,432 | 73,149 | TypeScript | 全球实时情报看板：AI 聚合新闻与地缘/基建监测 |
| 21 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | 11,907 | 30,071 | TypeScript | 一条命令让 AI 编程助手克隆任意网站 |
| 22 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 11,830 | 127,317 | Python | 100+ 可直接跑的 AI Agent / RAG 应用合集：克隆、改改就能上 |
| 23 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | 9,729 | 29,266 | Python | 给 AI Agent 装长期记忆的开源知识图谱平台 |
| 24 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | 8,657 | 27,713 | TypeScript | 页面内 GUI 智能体：用自然语言操控网页界面 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 8,649 | 49,604 | JavaScript | 设计语言规范，让 AI 做设计更靠谱 |
| 26 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | 8,513 | 29,862 | JavaScript | 在 Claude Code 里调用 Codex：审代码或委派任务 |
| 27 | [openai/codex](https://github.com/openai/codex) | 8,307 | 101,237 | Rust | 跑在终端里的轻量编程 Agent（OpenAI Codex） |
| 28 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | 7,880 | 18,980 | Haskell | 不靠用户 ID 的私密即时通讯网络 |
| 29 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | 7,873 | 15,266 | Python | 前馈 3D 基础模型：从流式数据重建场景 |
| 30 | [browser-use/video-use](https://github.com/browser-use/video-use) | 7,768 | 17,749 | Python | 让编程 Agent 直接剪辑改视频：用代码方式做视频后期 |
| 31 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | 7,386 | 9,908 | Python | 让 Claude 能「看视频」：下载、抽帧、转写一并交给它 |
| 32 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | 7,361 | 26,191 | Python | 本地优先代码知识图谱：让 AI 只读关键代码，大幅省审阅上下文 |
| 33 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 5,526 | 57,241 | Python | 小红书/抖音/B站/微博等主流平台媒体爬虫 |
| 34 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | 5,370 | 7,035 | Go | 减少 git push 出错的小工具/工作流 |
| 35 | [every-app/open-seo](https://github.com/every-app/open-seo) | 5,190 | 7,700 | TypeScript | 开源 SEO 工具，对标 Semrush/Ahrefs |
| 36 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | 4,897 | 6,528 | Python | 用 AI 自动评估简历、打分的招聘助手 |
| 37 | [t8y2/dbx](https://github.com/t8y2/dbx) | 4,843 | 11,611 | Rust | 约 20MB 的跨平台轻量数据库客户端（多引擎） |
| 38 | [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | 4,549 | 87,924 | Java | 在线/本地都能用的全能 PDF 编辑神器 |
| 39 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 4,541 | 29,553 | Python | 终身个性化 AI 家教：跟着你长期学、按你进度讲 |
| 40 | [immich-app/immich](https://github.com/immich-app/immich) | 4,535 | 108,663 | TypeScript | 高性能自托管相册：照片视频自己管 |
| 41 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 4,350 | 10,659 | Rust | 给 AI Agent 用的轻量安全沙箱：即开即跑 |
| 42 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 3,431 | 47,534 | TypeScript | 给编程 Agent 用的 Chrome DevTools MCP |
| 43 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | 3,317 | 21,205 | Go | 全自主 AI 渗透测试系统，能自己完成复杂安全评估任务 |
| 44 | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | 3,301 | 67,248 | Rust | 面向低成本模型的编程 Agent |
| 45 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | 3,301 | 4,613 | Python | 把书、长视频、播客等高价值内容蒸馏成可执行的 Agent Skills |
| 46 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 2,987 | 119,739 | TypeScript | 好看又无障碍的开源 UI 组件库，配代码分发平台，主流前端框架都能用 |
| 47 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | 2,829 | 6,291 | TypeScript | 给设计工程师用的 UI 技能包，帮 Agent 做好界面 |
| 48 | [schollz/croc](https://github.com/schollz/croc) | 2,809 | 38,283 | Go | 简单安全地在两台电脑之间传文件（端到端加密） |
| 49 | [IceWhaleTech/CasaOS](https://github.com/IceWhaleTech/CasaOS) | 2,761 | 36,838 | Go | 简单好看的开源个人云/家庭 NAS 系统 |
| 50 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | 2,753 | 27,569 | Python | 哈佛边缘计算课《机器学习系统》开源教材 |
| 51 | [cjpais/Handy](https://github.com/cjpais/Handy) | 2,703 | 27,403 | Rust | 完全离线的开源语音转文字应用 |
| 52 | [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | 2,694 | 8,806 | TypeScript | 给 Claude 装终端/文件/diff 能力的 MCP 服务 |
| 53 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | 2,562 | 7,127 | TypeScript | 想成为顶尖 AI/ML 研究工程师的数学/CS/AI 知识大全 |
| 54 | [vercel/next.js](https://github.com/vercel/next.js) | 2,207 | 141,104 | JavaScript | 最主流的 React 全栈框架（Vercel 出品） |
| 55 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | 2,077 | 4,927 | TypeScript | 月之暗面 Kimi 的编程 Agent CLI：下一代智能体的起点 |
| 56 | [rust-lang/rust](https://github.com/rust-lang/rust) | 2,065 | 114,801 | Rust | Rust 语言本体：可靠、高效的系统级编程 |
| 57 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 1,857 | 123,916 | Go | 生产级容器编排与集群管理系统 |
| 58 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 1,825 | 18,870 | Go | 腾讯开源 LLM 知识平台：文档变 RAG+推理 Agent |
| 59 | [juanfont/headscale](https://github.com/juanfont/headscale) | 1,804 | 42,061 | Go | 自托管版 Tailscale 控制面 |
| 60 | [Automattic/harper](https://github.com/Automattic/harper) | 1,791 | 12,968 | Rust | 离线隐私优先的语法检查器：开源、Rust 实现、又快又本地 |
| 61 | [DioxusLabs/dioxus](https://github.com/DioxusLabs/dioxus) | 1,790 | 38,270 | Rust | 用 Rust 写全栈应用：一套代码覆盖 Web/桌面/移动端 |
| 62 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 1,759 | 7,801 | TypeScript | 配合 Stitch MCP 的 Agent Skills 技能库 |
| 63 | [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) | 1,660 | 3,777 | TypeScript | 面向 AI 创作的开源无限画布：生图、视频、多 Agent 协同 |
| 64 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | 1,605 | 4,563 | JavaScript | 网文写作全流程 Skill：扫榜、拆文、去 AI 味、封面 |
| 65 | [tailscale/tailscale](https://github.com/tailscale/tailscale) | 1,597 | 34,286 | Go | 最简单好用的 WireGuard 组网（含 2FA） |
| 66 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | 1,583 | 4,866 | Java | 企业自托管的 Agent 技能注册中心：发布、版本、权限管控 |
| 67 | [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech) | 1,482 | 6,313 | Python | 用开源模型搭本地语音对话 Agent |
| 68 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | 1,482 | 4,541 | Go | 本地优先：搜索/分析编程 Agent 会话与 Token 消耗 |
| 69 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | 1,450 | 6,710 | Go | 面向 Grok 多端的多账号 API 网关 |
| 70 | [yorukot/superfile](https://github.com/yorukot/superfile) | 1,434 | 19,476 | Go | 好看现代的终端文件管理器 |
| 71 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) | 1,400 | 66,501 | Rust | 极速命令行正则搜索，自动尊重 .gitignore |
| 72 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | 1,384 | 2,147 | JavaScript | 把 HTML 当 Markdown 写：面向 HTML 产物的新编辑器 |
| 73 | [binwiederhier/ntfy](https://github.com/binwiederhier/ntfy) | 1,261 | 32,176 | Go | 用简单 HTTP 给手机/桌面推送通知 |
| 74 | [cupy/cupy](https://github.com/cupy/cupy) | 1,220 | 12,209 | Python | GPU 版 NumPy/SciPy，科学计算加速 |
| 75 | [denoland/deno](https://github.com/denoland/deno) | 1,203 | 107,779 | Rust | 现代 JavaScript/TypeScript 运行时 |
| 76 | [likec4/likec4](https://github.com/likec4/likec4) | 1,170 | 4,983 | TypeScript | 从代码生成始终最新的软件架构图，方便协作与演进 |
| 77 | [wezterm/wezterm](https://github.com/wezterm/wezterm) | 1,140 | 27,906 | Rust | GPU 加速的跨平台终端模拟器与多路复用器 |
| 78 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | 1,124 | 2,958 | JavaScript | 非官方 Linux 版 ChatGPT/Codex 桌面客户端 |
| 79 | [kunchenguid/gnhf](https://github.com/kunchenguid/gnhf) | 1,092 | 3,381 | TypeScript | 睡前跟 Agents 道晚安：让它们夜间继续干活 |
| 80 | [junegunn/fzf](https://github.com/junegunn/fzf) | 1,083 | 81,954 | Go | 命令行模糊查找神器 |
| 81 | [ocornut/imgui](https://github.com/ocornut/imgui) | 1,079 | 75,016 | C++ | 轻量级 C++ 即时模式 GUI 库 |
| 82 | [prometheus/prometheus](https://github.com/prometheus/prometheus) | 1,068 | 65,291 | Go | 监控与时序数据库领域的事实标准 |
| 83 | [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | 1,049 | 77,594 | Java | 开源分布式搜索与分析引擎 |
| 84 | [qdrant/qdrant](https://github.com/qdrant/qdrant) | 1,032 | 33,563 | Rust | 高性能大规模向量数据库与向量搜索引擎 |
| 85 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | 1,025 | 2,085 | JavaScript | 开箱即用的 AI 标书工具：生成、查重、废标项检查，完全开源 |
| 86 | [catchorg/Catch2](https://github.com/catchorg/Catch2) | 984 | 21,312 | C++ | 现代 C++ 单元测试框架，支持 TDD/BDD |
| 87 | [fatedier/frp](https://github.com/fatedier/frp) | 953 | 108,321 | Go | 内网穿透反向代理：把家里的服务暴露到公网 |
| 88 | [Pumpkin-MC/Pumpkin](https://github.com/Pumpkin-MC/Pumpkin) | 936 | 9,289 | Rust | 让人人都能轻松搭高速高效 Minecraft 服务器 |
| 89 | [AgentWrapper/agent-orchestrator](https://github.com/AgentWrapper/agent-orchestrator) | 932 | 8,550 | Go | 管一群编程 Agent 的 IDE：规划任务、开智能体、自动修 CI/冲突/审代码 |
| 90 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | 923 | 31,500 | Java | Android TV 上按自己规则看媒体内容 |
| 91 | [Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai) | 880 | 5,041 | Go | Gentleman Programming 出品的 AI 相关开源项目 |
| 92 | [OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr) | 868 | 4,848 | JavaScript | 隐私优先的跨平台语音转文字听写应用 |
| 93 | [jj-vcs/jj](https://github.com/jj-vcs/jj) | 867 | 30,586 | Rust | 兼容 Git、又简单又强的新一代版本控制系统 Jujutsu |
| 94 | [chinese-poetry/chinese-poetry](https://github.com/chinese-poetry/chinese-poetry) | 861 | 52,865 | JavaScript | 超全中华古诗词数据库：唐诗宋词一网打尽 |
| 95 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | 831 | 35,825 | Java | 开源身份认证与访问管理（IAM） |
| 96 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | 785 | 38,185 | JavaScript | 免费好用的在线数据库绘图与 SQL 生成器 |
| 97 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | 779 | 29,976 | Go | 基于 YAML 模板的高速漏洞扫描器 |
| 98 | [skylot/jadx](https://github.com/skylot/jadx) | 743 | 49,762 | Java | Dex 转 Java 的反编译工具 |
| 99 | [helix-editor/helix](https://github.com/helix-editor/helix) | 739 | 45,581 | Rust | 后模态风格的现代文本编辑器 |
| 100 | [gosom/google-maps-scraper](https://github.com/gosom/google-maps-scraper) | 738 | 5,260 | Go | 抓谷歌地图店铺信息：地址电话评分评论等 |

---

## 怎么读这份榜

1. **先看主题**：本月风向比单个仓库名更重要。
2. **再看本月+★**：比累计 Star 更能反映「最近谁在爆」。
3. **按语言筛**：想学某门语言，可直接在语言分布里找入口。
4. **官方页只有约20条**：本文件是多语言月榜拼出来的扩展 Top100。

