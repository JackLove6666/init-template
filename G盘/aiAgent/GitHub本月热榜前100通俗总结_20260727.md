# GitHub 本月热榜前100 · 通俗总结

> 数据来源：[https://github.com/trending?since=monthly](https://github.com/trending?since=monthly)  
> 抓取时间：2026-07-27 21:02（UTC: 2026-07-27T21:02:12.754947+00:00）  
> 说明：GitHub 官方月榜单页约20条；本报告按多语言月榜汇总去重后，按本月新增Star排序取前100。

---

## 一句话看懂本月风向

本月 GitHub 最热闹的，几乎都围着 **AI 干活**：AI Agent / 智能体、前端 / Web / UI、视频 / 多媒体 / 会议。
榜首前五是 **graphify**、**OmniRoute**、**orca**、**codebase-memory-mcp**、**OpenMontage**，榜首单月新增约 24,320 Star——大家在找「能替人干活的 AI 工具」，而不只是看模型本身。

## 本月热点主题（通俗版）

- **AI Agent / 智能体**（36 个）— 让 AI 自己规划、自己动手，而不是你一句一句喂指令。
- **前端 / Web / UI**（16 个）— 网页界面、用自然语言操控页面。
- **视频 / 多媒体 / 会议**（10 个）— 剪视频、开会纪要、语音直播相关。
- **网络 / 通信 / 隐私**（9 个）— 更私密的聊天、更稳的网络连接。
- **AI 编程助手 / 开发工具**（6 个）— 写代码、改代码、管一堆 Agent 一起干活的工具。
- **安全 / 渗透测试**（4 个）— 用 AI 找漏洞、做安全检测。
- **数据库 / 存储**（4 个）— 更快的向量库、日志库等基础设施。
- **知识库 / RAG / 记忆**（3 个）— 给 AI 装长期记忆，别聊完就忘。
- **大模型 / LLM 基础设施**（3 个）— 提示词、网关、免费模型接入、省 Token 这类「底座」。
- **运维 / DevOps / 云**（3 个）— 部署、云原生相关工具。
- **其他开源项目**（3 个）— 不好归类、但本月同样很火的项目。
- **语言 / 框架 / 基础库**（1 个）— 老牌好用的底层库持续被关注。
- **爬虫 / 数据采集**（1 个）— 帮 AI 或人把网页/社交内容抓干净。
- **金融 / 量化 / 股票**（1 个）— 看盘、分析行情的自动化工具。

## 语言分布（前100）

| 语言 | 项目数 | 本月新增Star合计 |
|---|---:|---:|
| TypeScript | 21 | 158,411 |
| Python | 18 | 179,522 |
| Rust | 18 | 67,449 |
| Go | 16 | 27,678 |
| JavaScript | 11 | 75,464 |
| Java | 8 | 11,392 |
| C++ | 2 | 2,191 |
| C | 1 | 20,672 |
| Unknown | 1 | 17,930 |
| HTML | 1 | 16,816 |
| CSS | 1 | 14,649 |
| C# | 1 | 14,295 |
| Swift | 1 | 3,386 |

## Top 10 速览（本月最火）

### 1. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

- **本月+24,320 ★**｜累计 97,089 ★｜Fork 9,400｜语言 Python
- **通俗说**：把代码库/文档/SQL/配置/PDF 变成可查询知识图谱的 Agent Skill
- **原简介**：Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **归类**：知识库 / RAG / 记忆

### 2. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

- **本月+23,805 ★**｜累计 32,040 ★｜Fork 4,157｜语言 TypeScript
- **通俗说**：免费 AI 网关：一个入口接 200+ 厂商，还能省 Token
- **原简介**：Never stop coding. Free MIT AI gateway: one endpoint, 290+ providers (90+ free), 500+ models — Kimi, Claude, GPT, OpenAI, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 500+ contributors
- **归类**：前端 / Web / UI

### 3. [stablyai/orca](https://github.com/stablyai/orca)

- **本月+21,857 ★**｜累计 30,703 ★｜Fork 2,181｜语言 TypeScript
- **通俗说**：同时调度一堆编程 Agent 的桌面/手机 ADE
- **原简介**：Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and VPS.
- **归类**：AI Agent / 智能体

### 4. [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

- **本月+20,672 ★**｜累计 35,886 ★｜Fork 2,807｜语言 C
- **通俗说**：超快代码知识图谱 MCP，让 AI 查代码少烧 Token
- **原简介**：High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **归类**：知识库 / RAG / 记忆

### 5. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)

- **本月+19,568 ★**｜累计 42,691 ★｜Fork 5,148｜语言 Python
- **通俗说**：把 AI 编程助手变成整套视频制作工作室（多流水线+大量技能包）
- **原简介**：World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- **归类**：AI Agent / 智能体

### 6. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

- **本月+19,417 ★**｜累计 61,246 ★｜Fork 4,969｜语言 Python
- **通俗说**：给 AI 装眼睛：读搜 Twitter/Reddit/B站/小红书等，基本不用付 API 费
- **原简介**：Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.
- **归类**：AI Agent / 智能体

### 7. [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut)

- **本月+19,272 ★**｜累计 79,266 ★｜Fork 7,908｜语言 TypeScript
- **通俗说**：开源版剪映（CapCut）替代品
- **原简介**：The open-source CapCut alternative
- **归类**：视频 / 多媒体 / 会议

### 8. [usestrix/strix](https://github.com/usestrix/strix)

- **本月+18,515 ★**｜累计 44,944 ★｜Fork 4,708｜语言 Python
- **通俗说**：开源 AI 渗透测试工具，帮你找应用漏洞
- **原简介**：Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **归类**：安全 / 渗透测试

### 9. [emilkowalski/skills](https://github.com/emilkowalski/skills)

- **本月+17,930 ★**｜累计 21,535 ★｜Fork 1,168｜语言 Unknown
- **通俗说**：给设计工程师用的 Skills 合集，让 AI 更懂设计和前端审美
- **原简介**：Skills for Design Engineers.
- **归类**：前端 / Web / UI

### 10. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

- **本月+16,858 ★**｜累计 68,247 ★｜Fork 4,717｜语言 JavaScript
- **通俗说**：教 AI 更有审美，少产出千篇一律的「AI 味」内容
- **原简介**：Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop
- **归类**：前端 / Web / UI

## 完整前100名单

| 排名 | 仓库 | 本月+★ | 累计★ | 语言 | 通俗一句话 |
|---:|---|---:|---:|---|---|
| 1 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 24,320 | 97,089 | Python | 把代码库/文档/SQL/配置/PDF 变成可查询知识图谱的 Agent Skill |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 23,805 | 32,040 | TypeScript | 免费 AI 网关：一个入口接 200+ 厂商，还能省 Token |
| 3 | [stablyai/orca](https://github.com/stablyai/orca) | 21,857 | 30,703 | TypeScript | 同时调度一堆编程 Agent 的桌面/手机 ADE |
| 4 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 20,672 | 35,886 | C | 超快代码知识图谱 MCP，让 AI 查代码少烧 Token |
| 5 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 19,568 | 42,691 | Python | 把 AI 编程助手变成整套视频制作工作室（多流水线+大量技能包） |
| 6 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 19,417 | 61,246 | Python | 给 AI 装眼睛：读搜 Twitter/Reddit/B站/小红书等，基本不用付 API 费 |
| 7 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | 19,272 | 79,266 | TypeScript | 开源版剪映（CapCut）替代品 |
| 8 | [usestrix/strix](https://github.com/usestrix/strix) | 18,515 | 44,944 | Python | 开源 AI 渗透测试工具，帮你找应用漏洞 |
| 9 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | 17,930 | 21,535 | Unknown | 给设计工程师用的 Skills 合集，让 AI 更懂设计和前端审美 |
| 10 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 16,858 | 68,247 | JavaScript | 教 AI 更有审美，少产出千篇一律的「AI 味」内容 |
| 11 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | 16,816 | 17,167 | HTML | 1324 个健身动作数据集：GIF动画、肌群/器械标签、六语种步骤说明 |
| 12 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 16,561 | 93,510 | JavaScript | 让 Claude 用「洞穴人」短句说话，少烧约 65% Token |
| 13 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | 14,798 | 75,288 | TypeScript | 全球实时情报看板：AI 聚合新闻与地缘/基建监测 |
| 14 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 14,718 | 60,934 | JavaScript | 汇总各大 AI（Claude/GPT/Gemini/Grok 等）系统提示词泄露内容 |
| 15 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 14,649 | 18,714 | CSS | 反「AI 味」设计技能：让 Claude/Cursor/Codex 做出更有品位的界面 |
| 16 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 14,550 | 28,070 | Python | 属于你自己的个人交易 Agent |
| 17 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | 14,295 | 22,618 | C# | 专为 AI Agent 读写 Word/Excel/PPT 的开源 Office 套件（免装 Office） |
| 18 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | 14,057 | 26,994 | Rust | 本地隐私优先的 AI 会议助手：实时转写+说话人分离+总结 |
| 19 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | 13,743 | 21,431 | Rust | 终端里的 Agent 多路复用器，同时盯多个智能体 |
| 20 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | 12,680 | 47,055 | TypeScript | 开源 AI 语音工作室：克隆声音、听写、创作 |
| 21 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 12,568 | 128,097 | Python | 100+ 可直接跑的 AI Agent / RAG 应用合集：克隆、改改就能上 |
| 22 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | 11,499 | 14,427 | Python | AI 时代伯克希尔：用多 Agent 做价值投资研究（巴菲特等人方法论） |
| 23 | [facebook/astryx](https://github.com/facebook/astryx) | 10,552 | 10,867 | TypeScript | 可深度定制、对 Agent 友好的开源设计系统（Meta/Facebook） |
| 24 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | 9,389 | 30,360 | TypeScript | 一条命令让 AI 编程助手克隆任意网站 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 9,127 | 51,442 | JavaScript | 设计语言规范，让 AI 做设计更靠谱 |
| 26 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | 8,532 | 30,111 | JavaScript | 在 Claude Code 里调用 Codex：审代码或委派任务 |
| 27 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | 8,326 | 15,676 | Python | 前馈 3D 基础模型：从流式数据重建场景 |
| 28 | [openai/codex](https://github.com/openai/codex) | 8,080 | 101,872 | Rust | 跑在终端里的轻量编程 Agent（OpenAI Codex） |
| 29 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | 7,959 | 27,988 | TypeScript | 页面内 GUI 智能体：用自然语言操控网页界面 |
| 30 | [browser-use/video-use](https://github.com/browser-use/video-use) | 7,793 | 17,935 | Python | 让编程 Agent 直接剪辑改视频：用代码方式做视频后期 |
| 31 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | 7,759 | 10,989 | Python | 让 Claude 能「看视频」：下载、抽帧、转写一并交给它 |
| 32 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | 7,741 | 26,897 | Python | 本地优先代码知识图谱：让 AI 只读关键代码，大幅省审阅上下文 |
| 33 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | 6,823 | 29,454 | Python | 给 AI Agent 装长期记忆的开源知识图谱平台 |
| 34 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | 5,773 | 6,188 | TypeScript | 开源可视化 CMS：对标 Webflow/Framer/WordPress，输出干净静态页 |
| 35 | [every-app/open-seo](https://github.com/every-app/open-seo) | 5,191 | 8,594 | TypeScript | 开源 SEO 工具，对标 Semrush/Ahrefs |
| 36 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 5,122 | 30,498 | Python | 终身个性化 AI 家教：跟着你长期学、按你进度讲 |
| 37 | [immich-app/immich](https://github.com/immich-app/immich) | 4,606 | 108,983 | TypeScript | 高性能自托管相册：照片视频自己管 |
| 38 | [t8y2/dbx](https://github.com/t8y2/dbx) | 4,534 | 11,973 | Rust | 约 20MB 的跨平台轻量数据库客户端（多引擎） |
| 39 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 4,359 | 10,718 | Rust | 给 AI Agent 用的轻量安全沙箱：即开即跑 |
| 40 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 4,291 | 23,302 | Python | 超全 Claude Code 技能库：30+ Agent、70+ 命令、330+ 技能可定制 |
| 41 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | 3,937 | 7,128 | Go | 减少 git push 出错的小工具/工作流 |
| 42 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | 3,918 | 12,003 | Rust | 更聪明的代码 Agent 运行框架（harness），专为编程智能体打造 |
| 43 | [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | 3,840 | 88,153 | Java | 在线/本地都能用的全能 PDF 编辑神器 |
| 44 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | 3,793 | 6,593 | Python | 用 AI 自动评估简历、打分的招聘助手 |
| 45 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | 3,538 | 10,811 | JavaScript | 给 Agent 用的 CAD/机器人/硬件设计技能包：用自然语言做三维设计 |
| 46 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | 3,480 | 4,858 | Python | 把书、长视频、播客等高价值内容蒸馏成可执行的 Agent Skills |
| 47 | [permissionlesstech/bitchat](https://github.com/permissionlesstech/bitchat) | 3,386 | 32,107 | Swift | 蓝牙 Mesh 聊天：不用网络也能近距离群聊，有点像 IRC 的感觉 |
| 48 | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | 3,384 | 67,345 | Rust | 面向低成本模型的编程 Agent |
| 49 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | 3,361 | 21,295 | Go | 全自主 AI 渗透测试系统，能自己完成复杂安全评估任务 |
| 50 | [schollz/croc](https://github.com/schollz/croc) | 3,296 | 38,840 | Go | 简单安全地在两台电脑之间传文件（端到端加密） |
| 51 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | 3,168 | 6,603 | TypeScript | 给设计工程师用的 UI 技能包，帮 Agent 做好界面 |
| 52 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 2,964 | 119,950 | TypeScript | 好看又无障碍的开源 UI 组件库，配代码分发平台，主流前端框架都能用 |
| 53 | [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | 2,796 | 8,894 | TypeScript | 给 Claude 装终端/文件/diff 能力的 MCP 服务 |
| 54 | [Automattic/harper](https://github.com/Automattic/harper) | 2,729 | 13,695 | Rust | 离线隐私优先的语法检查器：开源、Rust 实现、又快又本地 |
| 55 | [cjpais/Handy](https://github.com/cjpais/Handy) | 2,666 | 27,662 | Rust | 完全离线的开源语音转文字应用 |
| 56 | [yorukot/superfile](https://github.com/yorukot/superfile) | 2,646 | 20,810 | Go | 好看现代的终端文件管理器 |
| 57 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | 2,593 | 7,161 | TypeScript | 想成为顶尖 AI/ML 研究工程师的数学/CS/AI 知识大全 |
| 58 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | 2,376 | 5,348 | TypeScript | 月之暗面 Kimi 的编程 Agent CLI：下一代智能体的起点 |
| 59 | [rommapp/romm](https://github.com/rommapp/romm) | 2,354 | 11,450 | Python | 好看又好用的自托管 ROM 管理与模拟器播放器 |
| 60 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 2,322 | 15,280 | TypeScript | Theo 出品的极简 Web GUI：统一操控 Codex/Claude/Cursor 等编程 Agent |
| 61 | [Pumpkin-MC/Pumpkin](https://github.com/Pumpkin-MC/Pumpkin) | 2,088 | 10,197 | Rust | 让人人都能轻松搭高速高效 Minecraft 服务器 |
| 62 | [vercel/next.js](https://github.com/vercel/next.js) | 1,944 | 141,163 | JavaScript | 最主流的 React 全栈框架（Vercel 出品） |
| 63 | [agegr/pi-web](https://github.com/agegr/pi-web) | 1,939 | 2,997 | TypeScript | 给 pi 编程 Agent 配的 Web 界面，浏览器里就能用 |
| 64 | [DioxusLabs/dioxus](https://github.com/DioxusLabs/dioxus) | 1,863 | 38,335 | Rust | 用 Rust 写全栈应用：一套代码覆盖 Web/桌面/移动端 |
| 65 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 1,739 | 7,830 | TypeScript | 配合 Stitch MCP 的 Agent Skills 技能库 |
| 66 | [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) | 1,640 | 4,028 | TypeScript | 面向 AI 创作的开源无限画布：生图、视频、多 Agent 协同 |
| 67 | [tailscale/tailscale](https://github.com/tailscale/tailscale) | 1,623 | 34,415 | Go | 最简单好用的 WireGuard 组网（含 2FA） |
| 68 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 1,612 | 19,001 | Go | 腾讯开源 LLM 知识平台：文档变 RAG+推理 Agent |
| 69 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | 1,611 | 4,919 | Java | 企业自托管的 Agent 技能注册中心：发布、版本、权限管控 |
| 70 | [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech) | 1,603 | 6,574 | Python | 用开源模型搭本地语音对话 Agent |
| 71 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 1,574 | 124,011 | Go | 生产级容器编排与集群管理系统 |
| 72 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | 1,570 | 6,840 | Go | 面向 Grok 多端的多账号 API 网关 |
| 73 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | 1,385 | 71,447 | Java | NSA 开源的软件逆向工程框架，反汇编/反编译看二进制 |
| 74 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | 1,350 | 4,580 | Go | 本地优先：搜索/分析编程 Agent 会话与 Token 消耗 |
| 75 | [binwiederhier/ntfy](https://github.com/binwiederhier/ntfy) | 1,341 | 32,307 | Go | 用简单 HTTP 给手机/桌面推送通知 |
| 76 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | 1,260 | 2,229 | JavaScript | 把 HTML 当 Markdown 写：面向 HTML 产物的新编辑器 |
| 77 | [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | 1,208 | 27,445 | Java | AI 驱动的数据库客户端：自然语言查库、写 SQL，支持主流数据库 |
| 78 | [ocornut/imgui](https://github.com/ocornut/imgui) | 1,158 | 75,179 | C++ | 轻量级 C++ 即时模式 GUI 库 |
| 79 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | 1,150 | 3,056 | JavaScript | 非官方 Linux 版 ChatGPT/Codex 桌面客户端 |
| 80 | [denoland/deno](https://github.com/denoland/deno) | 1,130 | 107,830 | Rust | 现代 JavaScript/TypeScript 运行时 |
| 81 | [wezterm/wezterm](https://github.com/wezterm/wezterm) | 1,097 | 27,970 | Rust | GPU 加速的跨平台终端模拟器与多路复用器 |
| 82 | [catchorg/Catch2](https://github.com/catchorg/Catch2) | 1,033 | 21,375 | C++ | 现代 C++ 单元测试框架，支持 TDD/BDD |
| 83 | [junegunn/fzf](https://github.com/junegunn/fzf) | 1,015 | 81,999 | Go | 命令行模糊查找神器 |
| 84 | [prometheus/prometheus](https://github.com/prometheus/prometheus) | 1,006 | 65,336 | Go | 监控与时序数据库领域的事实标准 |
| 85 | [kunchenguid/gnhf](https://github.com/kunchenguid/gnhf) | 992 | 3,430 | TypeScript | 睡前跟 Agents 道晚安：让它们夜间继续干活 |
| 86 | [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | 979 | 77,616 | Java | 开源分布式搜索与分析引擎 |
| 87 | [hashicorp/terraform](https://github.com/hashicorp/terraform) | 972 | 49,308 | Go | 用代码安全、可预期地管理基础设施 |
| 88 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | 965 | 31,584 | Java | Android TV 上按自己规则看媒体内容 |
| 89 | [fatedier/frp](https://github.com/fatedier/frp) | 942 | 108,387 | Go | 内网穿透反向代理：把家里的服务暴露到公网 |
| 90 | [rivet-dev/agentos](https://github.com/rivet-dev/agentos) | 896 | 4,176 | Rust | 给 Agent 装操作系统：当库嵌进你现有后端，不用沙箱/虚拟机/SaaS |
| 91 | [chinese-poetry/chinese-poetry](https://github.com/chinese-poetry/chinese-poetry) | 892 | 52,908 | JavaScript | 超全中华古诗词数据库：唐诗宋词一网打尽 |
| 92 | [OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr) | 884 | 4,915 | JavaScript | 隐私优先的跨平台语音转文字听写应用 |
| 93 | [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) | 766 | 4,657 | Rust | 终端里追踪各 AI 编程 Agent 的 Token 用量，还有全球用量排行榜 |
| 94 | [skylot/jadx](https://github.com/skylot/jadx) | 755 | 49,806 | Java | Dex 转 Java 的反编译工具 |
| 95 | [gosom/google-maps-scraper](https://github.com/gosom/google-maps-scraper) | 752 | 5,298 | Go | 抓谷歌地图店铺信息：地址电话评分评论等 |
| 96 | [helix-editor/helix](https://github.com/helix-editor/helix) | 744 | 45,620 | Rust | 后模态风格的现代文本编辑器 |
| 97 | [wealthfolio/wealthfolio](https://github.com/wealthfolio/wealthfolio) | 727 | 8,401 | Rust | 本地优先的个人理财与投资追踪 |
| 98 | [kunchenguid/treehouse](https://github.com/kunchenguid/treehouse) | 681 | 1,080 | Go | 不用自己折腾 git worktree：更省心的多工作树管理 |
| 99 | [andrewrabert/jellium-desktop](https://github.com/andrewrabert/jellium-desktop) | 668 | 1,658 | Rust | 非官方 Jellyfin 桌面客户端：把家庭影院搬到桌面上 |
| 100 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | 649 | 10,052 | Java | 把 GitHub Copilot Agent 嵌进自己应用/服务的多端 SDK |

---

## 怎么读这份榜

1. **先看主题**：本月风向比单个仓库名更重要。
2. **再看本月+★**：比累计 Star 更能反映「最近谁在爆」。
3. **按语言筛**：想学某门语言，可直接在语言分布里找入口。
4. **官方页只有约20条**：本文件是多语言月榜拼出来的扩展 Top100。

