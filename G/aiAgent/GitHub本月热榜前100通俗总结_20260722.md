# GitHub 本月热榜前100 · 通俗总结

> 数据来源：[https://github.com/trending?since=monthly](https://github.com/trending?since=monthly)  
> 抓取时间：2026-07-22 21:02（UTC: 2026-07-22T21:02:24.078582+00:00）  
> 说明：GitHub 官方月榜单页约20条；本报告按多语言月榜汇总去重后，按本月新增Star排序取前100。

---

## 一句话看懂本月风向

本月 GitHub 最热闹的，几乎都围着 **AI 干活**：AI Agent / 智能体、前端 / Web / UI、视频 / 多媒体 / 会议。
榜首前五是 **OpenMontage**、**codebase-memory-mcp**、**Agent-Reach**、**ai-job-search**、**orca**，榜首单月新增约 33,415 Star——大家在找「能替人干活的 AI 工具」，而不只是看模型本身。

## 本月热点主题（通俗版）

- **AI Agent / 智能体**（34 个）— 让 AI 自己规划、自己动手，而不是你一句一句喂指令。
- **前端 / Web / UI**（13 个）— 网页界面、用自然语言操控页面。
- **网络 / 通信 / 隐私**（9 个）— 更私密的聊天、更稳的网络连接。
- **视频 / 多媒体 / 会议**（8 个）— 剪视频、开会纪要、语音直播相关。
- **AI 编程助手 / 开发工具**（7 个）— 写代码、改代码、管一堆 Agent 一起干活的工具。
- **数据库 / 存储**（6 个）— 更快的向量库、日志库等基础设施。
- **安全 / 渗透测试**（4 个）— 用 AI 找漏洞、做安全检测。
- **运维 / DevOps / 云**（4 个）— 部署、云原生相关工具。
- **大模型 / LLM 基础设施**（3 个）— 提示词、网关、免费模型接入、省 Token 这类「底座」。
- **其他开源项目**（3 个）— 不好归类、但本月同样很火的项目。
- **语言 / 框架 / 基础库**（3 个）— 老牌好用的底层库持续被关注。
- **知识库 / RAG / 记忆**（2 个）— 给 AI 装长期记忆，别聊完就忘。
- **金融 / 量化 / 股票**（2 个）— 看盘、分析行情的自动化工具。
- **爬虫 / 数据采集**（2 个）— 帮 AI 或人把网页/社交内容抓干净。

## 语言分布（前100）

| 语言 | 项目数 | 本月新增Star合计 |
|---|---:|---:|
| TypeScript | 20 | 158,237 |
| Rust | 19 | 64,339 |
| Python | 18 | 176,236 |
| Go | 16 | 28,932 |
| JavaScript | 13 | 77,660 |
| Java | 8 | 12,831 |
| C++ | 2 | 2,044 |
| C | 1 | 23,966 |
| C# | 1 | 13,004 |
| CSS | 1 | 11,449 |
| Haskell | 1 | 7,799 |

## Top 10 速览（本月最火）

### 1. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)

- **本月+33,415 ★**｜累计 41,214 ★｜Fork 4,876｜语言 Python
- **通俗说**：把 AI 编程助手变成整套视频制作工作室（多流水线+大量技能包）
- **原简介**：World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- **归类**：AI Agent / 智能体

### 2. [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

- **本月+23,966 ★**｜累计 34,134 ★｜Fork 2,620｜语言 C
- **通俗说**：超快代码知识图谱 MCP，让 AI 查代码少烧 Token
- **原简介**：High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **归类**：知识库 / RAG / 记忆

### 3. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

- **本月+23,075 ★**｜累计 59,664 ★｜Fork 4,782｜语言 Python
- **通俗说**：给 AI 装眼睛：读搜 Twitter/Reddit/B站/小红书等，基本不用付 API 费
- **原简介**：Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.
- **归类**：AI Agent / 智能体

### 4. [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)

- **本月+21,332 ★**｜累计 25,259 ★｜Fork 8,258｜语言 TypeScript
- **通俗说**：跑在本机的 AI 求职框架：筛岗位、改简历、写求职信、准备面试
- **原简介**：The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it.
- **归类**：AI Agent / 智能体

### 5. [stablyai/orca](https://github.com/stablyai/orca)

- **本月+18,867 ★**｜累计 25,981 ★｜Fork 1,871｜语言 TypeScript
- **通俗说**：同时调度一堆编程 Agent 的桌面/手机 ADE
- **原简介**：Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and VPS.
- **归类**：AI Agent / 智能体

### 6. [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut)

- **本月+18,592 ★**｜累计 77,529 ★｜Fork 7,758｜语言 TypeScript
- **通俗说**：开源版剪映（CapCut）替代品
- **原简介**：The open-source CapCut alternative
- **归类**：视频 / 多媒体 / 会议

### 7. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

- **本月+18,115 ★**｜累计 66,375 ★｜Fork 4,583｜语言 JavaScript
- **通俗说**：教 AI 更有审美，少产出千篇一律的「AI 味」内容
- **原简介**：Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop
- **归类**：前端 / Web / UI

### 8. [usestrix/strix](https://github.com/usestrix/strix)

- **本月+17,358 ★**｜累计 43,403 ★｜Fork 4,484｜语言 Python
- **通俗说**：开源 AI 渗透测试工具，帮你找应用漏洞
- **原简介**：Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **归类**：安全 / 渗透测试

### 9. [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)

- **本月+16,861 ★**｜累计 92,073 ★｜Fork 5,224｜语言 JavaScript
- **通俗说**：让 Claude 用「洞穴人」短句说话，少烧约 65% Token
- **原简介**：🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman
- **归类**：大模型 / LLM 基础设施

### 10. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

- **本月+16,353 ★**｜累计 25,040 ★｜Fork 3,339｜语言 TypeScript
- **通俗说**：免费 AI 网关：一个入口接 200+ 厂商，还能省 Token
- **原简介**：Never stop coding. Free MIT AI gateway: one endpoint, 268+ providers (50+ free), 500+ models — Kimi, Claude, GPT, OpenAI, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 500+ contributors
- **归类**：前端 / Web / UI

## 完整前100名单

| 排名 | 仓库 | 本月+★ | 累计★ | 语言 | 通俗一句话 |
|---:|---|---:|---:|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 33,415 | 41,214 | Python | 把 AI 编程助手变成整套视频制作工作室（多流水线+大量技能包） |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 23,966 | 34,134 | C | 超快代码知识图谱 MCP，让 AI 查代码少烧 Token |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 23,075 | 59,664 | Python | 给 AI 装眼睛：读搜 Twitter/Reddit/B站/小红书等，基本不用付 API 费 |
| 4 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | 21,332 | 25,259 | TypeScript | 跑在本机的 AI 求职框架：筛岗位、改简历、写求职信、准备面试 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | 18,867 | 25,981 | TypeScript | 同时调度一堆编程 Agent 的桌面/手机 ADE |
| 6 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | 18,592 | 77,529 | TypeScript | 开源版剪映（CapCut）替代品 |
| 7 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 18,115 | 66,375 | JavaScript | 教 AI 更有审美，少产出千篇一律的「AI 味」内容 |
| 8 | [usestrix/strix](https://github.com/usestrix/strix) | 17,358 | 43,403 | Python | 开源 AI 渗透测试工具，帮你找应用漏洞 |
| 9 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 16,861 | 92,073 | JavaScript | 让 Claude 用「洞穴人」短句说话，少烧约 65% Token |
| 10 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 16,353 | 25,040 | TypeScript | 免费 AI 网关：一个入口接 200+ 厂商，还能省 Token |
| 11 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 15,756 | 59,730 | JavaScript | 汇总各大 AI（Claude/GPT/Gemini/Grok 等）系统提示词泄露内容 |
| 12 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | 14,286 | 58,304 | Python | LLM 驱动的多市场股票智能分析：行情+新闻+看板+自动推送 |
| 13 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | 13,769 | 45,664 | TypeScript | 开源 AI 语音工作室：克隆声音、听写、创作 |
| 14 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 13,399 | 26,460 | Python | 属于你自己的个人交易 Agent |
| 15 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | 13,297 | 26,085 | Rust | 本地隐私优先的 AI 会议助手：实时转写+说话人分离+总结 |
| 16 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | 13,004 | 21,040 | C# | 专为 AI Agent 读写 Word/Excel/PPT 的开源 Office 套件（免装 Office） |
| 17 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | 12,612 | 19,508 | Rust | 终端里的 Agent 多路复用器，同时盯多个智能体 |
| 18 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | 12,350 | 29,662 | TypeScript | 一条命令让 AI 编程助手克隆任意网站 |
| 19 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 11,449 | 15,537 | CSS | 反「AI 味」设计技能：让 Claude/Cursor/Codex 做出更有品位的界面 |
| 20 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 10,837 | 126,281 | Python | 100+ 可直接跑的 AI Agent / RAG 应用合集：克隆、改改就能上 |
| 21 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | 10,695 | 29,159 | Python | 给 AI Agent 装长期记忆的开源知识图谱平台 |
| 22 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | 10,382 | 26,240 | TypeScript | 给编程 Agent 用的视觉品牌说明格式，让设计规范持久可执行 |
| 23 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 9,094 | 26,359 | Python | 给 AI Agent 用的 800+ 结构化网络安全技能包 |
| 24 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | 9,092 | 68,653 | TypeScript | 全球实时情报看板：AI 聚合新闻与地缘/基建监测 |
| 25 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | 8,951 | 27,489 | TypeScript | 页面内 GUI 智能体：用自然语言操控网页界面 |
| 26 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 8,759 | 48,758 | JavaScript | 设计语言规范，让 AI 做设计更靠谱 |
| 27 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | 8,367 | 29,659 | JavaScript | 在 Claude Code 里调用 Codex：审代码或委派任务 |
| 28 | [openai/codex](https://github.com/openai/codex) | 8,276 | 100,680 | Rust | 跑在终端里的轻量编程 Agent（OpenAI Codex） |
| 29 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | 7,799 | 18,897 | Haskell | 不靠用户 ID 的私密即时通讯网络 |
| 30 | [browser-use/video-use](https://github.com/browser-use/video-use) | 7,641 | 17,534 | Python | 让编程 Agent 直接剪辑改视频：用代码方式做视频后期 |
| 31 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | 7,459 | 14,885 | Python | 前馈 3D 基础模型：从流式数据重建场景 |
| 32 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | 7,327 | 9,631 | Python | 让 Claude 能「看视频」：下载、抽帧、转写一并交给它 |
| 33 | [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | 5,995 | 87,764 | Java | 在线/本地都能用的全能 PDF 编辑神器 |
| 34 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 5,655 | 57,114 | Python | 小红书/抖音/B站/微博等主流平台媒体爬虫 |
| 35 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | 5,364 | 6,889 | Go | 减少 git push 出错的小工具/工作流 |
| 36 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | 5,255 | 6,406 | Python | 用 AI 自动评估简历、打分的招聘助手 |
| 37 | [t8y2/dbx](https://github.com/t8y2/dbx) | 4,597 | 11,199 | Rust | 约 20MB 的跨平台轻量数据库客户端（多引擎） |
| 38 | [immich-app/immich](https://github.com/immich-app/immich) | 4,568 | 108,484 | TypeScript | 高性能自托管相册：照片视频自己管 |
| 39 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 4,329 | 10,602 | Rust | 给 AI Agent 用的轻量安全沙箱：即开即跑 |
| 40 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 4,238 | 29,086 | Python | 终身个性化 AI 家教：跟着你长期学、按你进度讲 |
| 41 | [every-app/open-seo](https://github.com/every-app/open-seo) | 4,229 | 7,089 | TypeScript | 开源 SEO 工具，对标 Semrush/Ahrefs |
| 42 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | 3,267 | 21,107 | Go | 全自主 AI 渗透测试系统，能自己完成复杂安全评估任务 |
| 43 | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | 3,148 | 67,129 | Rust | 面向低成本模型的编程 Agent |
| 44 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 2,989 | 119,572 | TypeScript | 好看又无障碍的开源 UI 组件库，配代码分发平台，主流前端框架都能用 |
| 45 | [IceWhaleTech/CasaOS](https://github.com/IceWhaleTech/CasaOS) | 2,793 | 36,812 | Go | 简单好看的开源个人云/家庭 NAS 系统 |
| 46 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | 2,778 | 29,907 | Rust | 一条命令行搞定 Drive/Gmail/日历/表格等 Workspace |
| 47 | [cjpais/Handy](https://github.com/cjpais/Handy) | 2,760 | 27,208 | Rust | 完全离线的开源语音转文字应用 |
| 48 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | 2,754 | 27,548 | Python | 哈佛边缘计算课《机器学习系统》开源教材 |
| 49 | [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | 2,611 | 8,732 | TypeScript | 给 Claude 装终端/文件/diff 能力的 MCP 服务 |
| 50 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | 2,567 | 5,980 | TypeScript | 给设计工程师用的 UI 技能包，帮 Agent 做好界面 |
| 51 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | 2,565 | 3,829 | TypeScript | 做「智能体原生」应用的框架，让产品天生会跟 Agent 协作 |
| 52 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | 2,526 | 7,082 | TypeScript | 想成为顶尖 AI/ML 研究工程师的数学/CS/AI 知识大全 |
| 53 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 2,229 | 18,739 | Go | 腾讯开源 LLM 知识平台：文档变 RAG+推理 Agent |
| 54 | [vercel/next.js](https://github.com/vercel/next.js) | 2,224 | 141,072 | JavaScript | 最主流的 React 全栈框架（Vercel 出品） |
| 55 | [rust-lang/rust](https://github.com/rust-lang/rust) | 2,081 | 114,747 | Rust | Rust 语言本体：可靠、高效的系统级编程 |
| 56 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | 1,865 | 4,569 | TypeScript | 月之暗面 Kimi 的编程 Agent CLI：下一代智能体的起点 |
| 57 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 1,855 | 123,881 | Go | 生产级容器编排与集群管理系统 |
| 58 | [juanfont/headscale](https://github.com/juanfont/headscale) | 1,799 | 41,977 | Go | 自托管版 Tailscale 控制面 |
| 59 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 1,744 | 7,766 | TypeScript | 配合 Stitch MCP 的 Agent Skills 技能库 |
| 60 | [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) | 1,715 | 3,671 | TypeScript | 面向 AI 创作的开源无限画布：生图、视频、多 Agent 协同 |
| 61 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | 1,622 | 4,474 | JavaScript | 网文写作全流程 Skill：扫榜、拆文、去 AI 味、封面 |
| 62 | [tailscale/tailscale](https://github.com/tailscale/tailscale) | 1,602 | 34,197 | Go | 最简单好用的 WireGuard 组网（含 2FA） |
| 63 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | 1,540 | 4,504 | Go | 本地优先：搜索/分析编程 Agent 会话与 Token 消耗 |
| 64 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | 1,510 | 4,888 | Java | 企业自托管的 Agent 技能注册中心：发布、版本、权限管控 |
| 65 | [n0-computer/iroh](https://github.com/n0-computer/iroh) | 1,495 | 11,801 | Rust | 给应用加上 QUIC + NAT 穿透，用密钥拨号而不是 IP |
| 66 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | 1,477 | 2,085 | JavaScript | 把 HTML 当 Markdown 写：面向 HTML 产物的新编辑器 |
| 67 | [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech) | 1,433 | 6,281 | Python | 用开源模型搭本地语音对话 Agent |
| 68 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) | 1,406 | 66,425 | Rust | 极速命令行正则搜索，自动尊重 .gitignore |
| 69 | [yorukot/superfile](https://github.com/yorukot/superfile) | 1,297 | 18,735 | Go | 好看现代的终端文件管理器 |
| 70 | [schollz/croc](https://github.com/schollz/croc) | 1,279 | 37,477 | Go | 简单安全地在两台电脑之间传文件（端到端加密） |
| 71 | [denoland/deno](https://github.com/denoland/deno) | 1,257 | 107,760 | Rust | 现代 JavaScript/TypeScript 运行时 |
| 72 | [binwiederhier/ntfy](https://github.com/binwiederhier/ntfy) | 1,252 | 32,128 | Go | 用简单 HTTP 给手机/桌面推送通知 |
| 73 | [cupy/cupy](https://github.com/cupy/cupy) | 1,200 | 12,186 | Python | GPU 版 NumPy/SciPy，科学计算加速 |
| 74 | [wezterm/wezterm](https://github.com/wezterm/wezterm) | 1,180 | 27,848 | Rust | GPU 加速的跨平台终端模拟器与多路复用器 |
| 75 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | 1,178 | 128,706 | Java | 动画图解的数据结构与算法教程（多语言） |
| 76 | [kunchenguid/gnhf](https://github.com/kunchenguid/gnhf) | 1,170 | 3,346 | TypeScript | 睡前跟 Agents 道晚安：让它们夜间继续干活 |
| 77 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | 1,115 | 2,881 | JavaScript | 非官方 Linux 版 ChatGPT/Codex 桌面客户端 |
| 78 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | 1,115 | 2,063 | Python | AWS 官方 Agent 工具包：MCP/技能/插件，帮智能体在 AWS 上干活 |
| 79 | [junegunn/fzf](https://github.com/junegunn/fzf) | 1,114 | 81,913 | Go | 命令行模糊查找神器 |
| 80 | [prometheus/prometheus](https://github.com/prometheus/prometheus) | 1,106 | 65,260 | Go | 监控与时序数据库领域的事实标准 |
| 81 | [DioxusLabs/dioxus](https://github.com/DioxusLabs/dioxus) | 1,097 | 37,968 | Rust | 用 Rust 写全栈应用：一套代码覆盖 Web/桌面/移动端 |
| 82 | [ocornut/imgui](https://github.com/ocornut/imgui) | 1,092 | 74,936 | C++ | 轻量级 C++ 即时模式 GUI 库 |
| 83 | [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | 1,063 | 77,574 | Java | 开源分布式搜索与分析引擎 |
| 84 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | 1,047 | 2,049 | JavaScript | 开箱即用的 AI 标书工具：生成、查重、废标项检查，完全开源 |
| 85 | [qdrant/qdrant](https://github.com/qdrant/qdrant) | 1,033 | 33,504 | Rust | 高性能大规模向量数据库与向量搜索引擎 |
| 86 | [catchorg/Catch2](https://github.com/catchorg/Catch2) | 952 | 21,279 | C++ | 现代 C++ 单元测试框架，支持 TDD/BDD |
| 87 | [fatedier/frp](https://github.com/fatedier/frp) | 923 | 108,276 | Go | 内网穿透反向代理：把家里的服务暴露到公网 |
| 88 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | 888 | 31,456 | Java | Android TV 上按自己规则看媒体内容 |
| 89 | [OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr) | 843 | 4,754 | JavaScript | 隐私优先的跨平台语音转文字听写应用 |
| 90 | [sharkdp/bat](https://github.com/sharkdp/bat) | 822 | 59,840 | Rust | 带语法高亮的猫命令增强版（cat 替代） |
| 91 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | 816 | 35,796 | Java | 开源身份认证与访问管理（IAM） |
| 92 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | 783 | 38,157 | JavaScript | 免费好用的在线数据库绘图与 SQL 生成器 |
| 93 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | 762 | 29,914 | Go | 基于 YAML 模板的高速漏洞扫描器 |
| 94 | [gosom/google-maps-scraper](https://github.com/gosom/google-maps-scraper) | 750 | 5,216 | Go | 抓谷歌地图店铺信息：地址电话评分评论等 |
| 95 | [helix-editor/helix](https://github.com/helix-editor/helix) | 739 | 45,550 | Rust | 后模态风格的现代文本编辑器 |
| 96 | [skylot/jadx](https://github.com/skylot/jadx) | 725 | 49,735 | Java | Dex 转 Java 的反编译工具 |
| 97 | [ModernRelay/omnigraph](https://github.com/ModernRelay/omnigraph) | 724 | 952 | Rust | 湖仓原生图引擎，工作流像用 Git 一样管理 |
| 98 | [wealthfolio/wealthfolio](https://github.com/wealthfolio/wealthfolio) | 708 | 8,352 | Rust | 本地优先的个人理财与投资追踪 |
| 99 | [chinese-poetry/chinese-poetry](https://github.com/chinese-poetry/chinese-poetry) | 691 | 52,785 | JavaScript | 超全中华古诗词数据库：唐诗宋词一网打尽 |
| 100 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | 656 | 10,042 | Java | 把 GitHub Copilot Agent 嵌进自己应用/服务的多端 SDK |

---

## 怎么读这份榜

1. **先看主题**：本月风向比单个仓库名更重要。
2. **再看本月+★**：比累计 Star 更能反映「最近谁在爆」。
3. **按语言筛**：想学某门语言，可直接在语言分布里找入口。
4. **官方页只有约20条**：本文件是多语言月榜拼出来的扩展 Top100。

