# GitHub 本月热榜前100 · 通俗总结

> 数据来源：[https://github.com/trending?since=monthly](https://github.com/trending?since=monthly)  
> 抓取时间：2026-07-26 21:03（UTC: 2026-07-26T21:03:42.006351+00:00）  
> 说明：GitHub 官方月榜单页约20条；本报告按多语言月榜汇总去重后，按本月新增Star排序取前100。

---

## 一句话看懂本月风向

本月 GitHub 最热闹的，几乎都围着 **AI 干活**：AI Agent / 智能体、前端 / Web / UI、视频 / 多媒体 / 会议。
榜首前五是 **graphify**、**OmniRoute**、**orca**、**codebase-memory-mcp**、**OpenMontage**，榜首单月新增约 24,181 Star——大家在找「能替人干活的 AI 工具」，而不只是看模型本身。

## 本月热点主题（通俗版）

- **AI Agent / 智能体**（34 个）— 让 AI 自己规划、自己动手，而不是你一句一句喂指令。
- **前端 / Web / UI**（15 个）— 网页界面、用自然语言操控页面。
- **视频 / 多媒体 / 会议**（9 个）— 剪视频、开会纪要、语音直播相关。
- **网络 / 通信 / 隐私**（9 个）— 更私密的聊天、更稳的网络连接。
- **AI 编程助手 / 开发工具**（6 个）— 写代码、改代码、管一堆 Agent 一起干活的工具。
- **安全 / 渗透测试**（5 个）— 用 AI 找漏洞、做安全检测。
- **知识库 / RAG / 记忆**（4 个）— 给 AI 装长期记忆，别聊完就忘。
- **运维 / DevOps / 云**（4 个）— 部署、云原生相关工具。
- **数据库 / 存储**（4 个）— 更快的向量库、日志库等基础设施。
- **大模型 / LLM 基础设施**（3 个）— 提示词、网关、免费模型接入、省 Token 这类「底座」。
- **其他开源项目**（3 个）— 不好归类、但本月同样很火的项目。
- **语言 / 框架 / 基础库**（2 个）— 老牌好用的底层库持续被关注。
- **爬虫 / 数据采集**（1 个）— 帮 AI 或人把网页/社交内容抓干净。
- **金融 / 量化 / 股票**（1 个）— 看盘、分析行情的自动化工具。

## 语言分布（前100）

| 语言 | 项目数 | 本月新增Star合计 |
|---|---:|---:|
| TypeScript | 21 | 144,663 |
| Rust | 19 | 67,672 |
| Python | 17 | 179,933 |
| Go | 17 | 28,186 |
| JavaScript | 12 | 77,147 |
| Java | 8 | 11,123 |
| C++ | 2 | 2,146 |
| C | 1 | 20,976 |
| CSS | 1 | 14,156 |
| C# | 1 | 14,153 |
| Swift | 1 | 2,701 |

## Top 10 速览（本月最火）

### 1. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

- **本月+24,181 ★**｜累计 96,377 ★｜Fork 9,336｜语言 Python
- **通俗说**：把代码库/文档/SQL/配置/PDF 变成可查询知识图谱的 Agent Skill
- **原简介**：Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **归类**：知识库 / RAG / 记忆

### 2. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

- **本月+23,016 ★**｜累计 30,927 ★｜Fork 4,015｜语言 TypeScript
- **通俗说**：免费 AI 网关：一个入口接 200+ 厂商，还能省 Token
- **原简介**：Never stop coding. Free MIT AI gateway: one endpoint, 290+ providers (90+ free), 500+ models — Kimi, Claude, GPT, OpenAI, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 500+ contributors
- **归类**：前端 / Web / UI

### 3. [stablyai/orca](https://github.com/stablyai/orca)

- **本月+21,817 ★**｜累计 29,583 ★｜Fork 2,112｜语言 TypeScript
- **通俗说**：同时调度一堆编程 Agent 的桌面/手机 ADE
- **原简介**：Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and VPS.
- **归类**：AI Agent / 智能体

### 4. [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

- **本月+20,976 ★**｜累计 35,560 ★｜Fork 2,776｜语言 C
- **通俗说**：超快代码知识图谱 MCP，让 AI 查代码少烧 Token
- **原简介**：High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **归类**：知识库 / RAG / 记忆

### 5. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)

- **本月+20,972 ★**｜累计 42,438 ★｜Fork 5,084｜语言 Python
- **通俗说**：把 AI 编程助手变成整套视频制作工作室（多流水线+大量技能包）
- **原简介**：World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- **归类**：AI Agent / 智能体

### 6. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

- **本月+20,346 ★**｜累计 61,004 ★｜Fork 4,951｜语言 Python
- **通俗说**：给 AI 装眼睛：读搜 Twitter/Reddit/B站/小红书等，基本不用付 API 费
- **原简介**：Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.
- **归类**：AI Agent / 智能体

### 7. [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut)

- **本月+19,309 ★**｜累计 78,984 ★｜Fork 7,886｜语言 TypeScript
- **通俗说**：开源版剪映（CapCut）替代品
- **原简介**：The open-source CapCut alternative
- **归类**：视频 / 多媒体 / 会议

### 8. [usestrix/strix](https://github.com/usestrix/strix)

- **本月+18,324 ★**｜累计 44,490 ★｜Fork 4,631｜语言 Python
- **通俗说**：开源 AI 渗透测试工具，帮你找应用漏洞
- **原简介**：Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **归类**：安全 / 渗透测试

### 9. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

- **本月+17,100 ★**｜累计 67,901 ★｜Fork 4,698｜语言 JavaScript
- **通俗说**：教 AI 更有审美，少产出千篇一律的「AI 味」内容
- **原简介**：Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop
- **归类**：前端 / Web / UI

### 10. [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)

- **本月+16,655 ★**｜累计 93,193 ★｜Fork 5,315｜语言 JavaScript
- **通俗说**：让 Claude 用「洞穴人」短句说话，少烧约 65% Token
- **原简介**：🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman
- **归类**：大模型 / LLM 基础设施

## 完整前100名单

| 排名 | 仓库 | 本月+★ | 累计★ | 语言 | 通俗一句话 |
|---:|---|---:|---:|---|---|
| 1 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 24,181 | 96,377 | Python | 把代码库/文档/SQL/配置/PDF 变成可查询知识图谱的 Agent Skill |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 23,016 | 30,927 | TypeScript | 免费 AI 网关：一个入口接 200+ 厂商，还能省 Token |
| 3 | [stablyai/orca](https://github.com/stablyai/orca) | 21,817 | 29,583 | TypeScript | 同时调度一堆编程 Agent 的桌面/手机 ADE |
| 4 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 20,976 | 35,560 | C | 超快代码知识图谱 MCP，让 AI 查代码少烧 Token |
| 5 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 20,972 | 42,438 | Python | 把 AI 编程助手变成整套视频制作工作室（多流水线+大量技能包） |
| 6 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 20,346 | 61,004 | Python | 给 AI 装眼睛：读搜 Twitter/Reddit/B站/小红书等，基本不用付 API 费 |
| 7 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | 19,309 | 78,984 | TypeScript | 开源版剪映（CapCut）替代品 |
| 8 | [usestrix/strix](https://github.com/usestrix/strix) | 18,324 | 44,490 | Python | 开源 AI 渗透测试工具，帮你找应用漏洞 |
| 9 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 17,100 | 67,901 | JavaScript | 教 AI 更有审美，少产出千篇一律的「AI 味」内容 |
| 10 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 16,655 | 93,193 | JavaScript | 让 Claude 用「洞穴人」短句说话，少烧约 65% Token |
| 11 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 14,812 | 60,672 | JavaScript | 汇总各大 AI（Claude/GPT/Gemini/Grok 等）系统提示词泄露内容 |
| 12 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | 14,554 | 74,690 | TypeScript | 全球实时情报看板：AI 聚合新闻与地缘/基建监测 |
| 13 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 14,438 | 27,807 | Python | 属于你自己的个人交易 Agent |
| 14 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 14,156 | 18,160 | CSS | 反「AI 味」设计技能：让 Claude/Cursor/Codex 做出更有品位的界面 |
| 15 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | 14,153 | 22,358 | C# | 专为 AI Agent 读写 Word/Excel/PPT 的开源 Office 套件（免装 Office） |
| 16 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | 13,915 | 26,807 | Rust | 本地隐私优先的 AI 会议助手：实时转写+说话人分离+总结 |
| 17 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | 13,607 | 21,020 | Rust | 终端里的 Agent 多路复用器，同时盯多个智能体 |
| 18 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | 12,777 | 46,899 | TypeScript | 开源 AI 语音工作室：克隆声音、听写、创作 |
| 19 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | 12,519 | 14,200 | Python | AI 时代伯克希尔：用多 Agent 做价值投资研究（巴菲特等人方法论） |
| 20 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 12,459 | 127,870 | Python | 100+ 可直接跑的 AI Agent / RAG 应用合集：克隆、改改就能上 |
| 21 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | 10,333 | 30,270 | TypeScript | 一条命令让 AI 编程助手克隆任意网站 |
| 22 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 8,911 | 50,555 | JavaScript | 设计语言规范，让 AI 做设计更靠谱 |
| 23 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | 8,517 | 29,990 | JavaScript | 在 Claude Code 里调用 Codex：审代码或委派任务 |
| 24 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | 8,372 | 27,899 | TypeScript | 页面内 GUI 智能体：用自然语言操控网页界面 |
| 25 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | 8,205 | 15,543 | Python | 前馈 3D 基础模型：从流式数据重建场景 |
| 26 | [openai/codex](https://github.com/openai/codex) | 8,123 | 101,617 | Rust | 跑在终端里的轻量编程 Agent（OpenAI Codex） |
| 27 | [browser-use/video-use](https://github.com/browser-use/video-use) | 7,807 | 17,869 | Python | 让编程 Agent 直接剪辑改视频：用代码方式做视频后期 |
| 28 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | 7,596 | 26,578 | Python | 本地优先代码知识图谱：让 AI 只读关键代码，大幅省审阅上下文 |
| 29 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | 7,565 | 10,402 | Python | 让 Claude 能「看视频」：下载、抽帧、转写一并交给它 |
| 30 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | 7,408 | 29,391 | Python | 给 AI Agent 装长期记忆的开源知识图谱平台 |
| 31 | [every-app/open-seo](https://github.com/every-app/open-seo) | 5,500 | 8,207 | TypeScript | 开源 SEO 工具，对标 Semrush/Ahrefs |
| 32 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 4,857 | 30,052 | Python | 终身个性化 AI 家教：跟着你长期学、按你进度讲 |
| 33 | [t8y2/dbx](https://github.com/t8y2/dbx) | 4,647 | 11,746 | Rust | 约 20MB 的跨平台轻量数据库客户端（多引擎） |
| 34 | [immich-app/immich](https://github.com/immich-app/immich) | 4,540 | 108,886 | TypeScript | 高性能自托管相册：照片视频自己管 |
| 35 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 4,359 | 10,697 | Rust | 给 AI Agent 用的轻量安全沙箱：即开即跑 |
| 36 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 4,318 | 23,236 | Python | 超全 Claude Code 技能库：30+ Agent、70+ 命令、330+ 技能可定制 |
| 37 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | 4,305 | 7,099 | Go | 减少 git push 出错的小工具/工作流 |
| 38 | [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | 4,002 | 88,072 | Java | 在线/本地都能用的全能 PDF 编辑神器 |
| 39 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | 3,995 | 6,564 | Python | 用 AI 自动评估简历、打分的招聘助手 |
| 40 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | 3,712 | 11,641 | Rust | 更聪明的代码 Agent 运行框架（harness），专为编程智能体打造 |
| 41 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | 3,491 | 10,495 | JavaScript | 给 Agent 用的 CAD/机器人/硬件设计技能包：用自然语言做三维设计 |
| 42 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | 3,415 | 4,776 | Python | 把书、长视频、播客等高价值内容蒸馏成可执行的 Agent Skills |
| 43 | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | 3,355 | 67,314 | Rust | 面向低成本模型的编程 Agent |
| 44 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | 3,350 | 21,259 | Go | 全自主 AI 渗透测试系统，能自己完成复杂安全评估任务 |
| 45 | [schollz/croc](https://github.com/schollz/croc) | 3,142 | 38,627 | Go | 简单安全地在两台电脑之间传文件（端到端加密） |
| 46 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | 3,045 | 6,530 | TypeScript | 给设计工程师用的 UI 技能包，帮 Agent 做好界面 |
| 47 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 2,960 | 119,878 | TypeScript | 好看又无障碍的开源 UI 组件库，配代码分发平台，主流前端框架都能用 |
| 48 | [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | 2,755 | 8,869 | TypeScript | 给 Claude 装终端/文件/diff 能力的 MCP 服务 |
| 49 | [permissionlesstech/bitchat](https://github.com/permissionlesstech/bitchat) | 2,701 | 30,095 | Swift | 蓝牙 Mesh 聊天：不用网络也能近距离群聊，有点像 IRC 的感觉 |
| 50 | [cjpais/Handy](https://github.com/cjpais/Handy) | 2,655 | 27,578 | Rust | 完全离线的开源语音转文字应用 |
| 51 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | 2,586 | 7,153 | TypeScript | 想成为顶尖 AI/ML 研究工程师的数学/CS/AI 知识大全 |
| 52 | [yorukot/superfile](https://github.com/yorukot/superfile) | 2,448 | 20,141 | Go | 好看现代的终端文件管理器 |
| 53 | [Automattic/harper](https://github.com/Automattic/harper) | 2,412 | 13,613 | Rust | 离线隐私优先的语法检查器：开源、Rust 实现、又快又本地 |
| 54 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | 2,277 | 5,175 | TypeScript | 月之暗面 Kimi 的编程 Agent CLI：下一代智能体的起点 |
| 55 | [logto-io/logto](https://github.com/logto-io/logto) | 2,116 | 14,232 | TypeScript | 给 SaaS/AI 应用的认证授权底座（OIDC/OAuth、多租户、SSO） |
| 56 | [vercel/next.js](https://github.com/vercel/next.js) | 1,965 | 141,148 | JavaScript | 最主流的 React 全栈框架（Vercel 出品） |
| 57 | [DioxusLabs/dioxus](https://github.com/DioxusLabs/dioxus) | 1,854 | 38,313 | Rust | 用 Rust 写全栈应用：一套代码覆盖 Web/桌面/移动端 |
| 58 | [agegr/pi-web](https://github.com/agegr/pi-web) | 1,809 | 2,859 | TypeScript | 给 pi 编程 Agent 配的 Web 界面，浏览器里就能用 |
| 59 | [Pumpkin-MC/Pumpkin](https://github.com/Pumpkin-MC/Pumpkin) | 1,772 | 9,954 | Rust | 让人人都能轻松搭高速高效 Minecraft 服务器 |
| 60 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 1,750 | 7,823 | TypeScript | 配合 Stitch MCP 的 Agent Skills 技能库 |
| 61 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 1,646 | 18,925 | Go | 腾讯开源 LLM 知识平台：文档变 RAG+推理 Agent |
| 62 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 1,614 | 123,973 | Go | 生产级容器编排与集群管理系统 |
| 63 | [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) | 1,611 | 3,898 | TypeScript | 面向 AI 创作的开源无限画布：生图、视频、多 Agent 协同 |
| 64 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | 1,604 | 4,901 | Java | 企业自托管的 Agent 技能注册中心：发布、版本、权限管控 |
| 65 | [tailscale/tailscale](https://github.com/tailscale/tailscale) | 1,602 | 34,364 | Go | 最简单好用的 WireGuard 组网（含 2FA） |
| 66 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | 1,580 | 4,624 | JavaScript | 网文写作全流程 Skill：扫榜、拆文、去 AI 味、封面 |
| 67 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | 1,549 | 6,780 | Go | 面向 Grok 多端的多账号 API 网关 |
| 68 | [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech) | 1,528 | 6,431 | Python | 用开源模型搭本地语音对话 Agent |
| 69 | [likec4/likec4](https://github.com/likec4/likec4) | 1,457 | 5,171 | TypeScript | 从代码生成始终最新的软件架构图，方便协作与演进 |
| 70 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | 1,377 | 4,565 | Go | 本地优先：搜索/分析编程 Agent 会话与 Token 消耗 |
| 71 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | 1,376 | 71,402 | Java | NSA 开源的软件逆向工程框架，反汇编/反编译看二进制 |
| 72 | [binwiederhier/ntfy](https://github.com/binwiederhier/ntfy) | 1,296 | 32,269 | Go | 用简单 HTTP 给手机/桌面推送通知 |
| 73 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | 1,285 | 2,174 | JavaScript | 把 HTML 当 Markdown 写：面向 HTML 产物的新编辑器 |
| 74 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | 1,146 | 3,016 | JavaScript | 非官方 Linux 版 ChatGPT/Codex 桌面客户端 |
| 75 | [denoland/deno](https://github.com/denoland/deno) | 1,144 | 107,813 | Rust | 现代 JavaScript/TypeScript 运行时 |
| 76 | [ocornut/imgui](https://github.com/ocornut/imgui) | 1,131 | 75,095 | C++ | 轻量级 C++ 即时模式 GUI 库 |
| 77 | [lumina-ai-inc/chunkr](https://github.com/lumina-ai-inc/chunkr) | 1,104 | 4,048 | Rust | 把复杂文档变成 RAG/大模型能吃的干净数据（视觉文档处理） |
| 78 | [wezterm/wezterm](https://github.com/wezterm/wezterm) | 1,102 | 27,947 | Rust | GPU 加速的跨平台终端模拟器与多路复用器 |
| 79 | [Yeachan-Heo/gajae-code](https://github.com/Yeachan-Heo/gajae-code) | 1,061 | 2,232 | TypeScript | Gajae Code：面向编程场景的代码 Agent 产品（早期 MVP） |
| 80 | [kunchenguid/gnhf](https://github.com/kunchenguid/gnhf) | 1,018 | 3,409 | TypeScript | 睡前跟 Agents 道晚安：让它们夜间继续干活 |
| 81 | [catchorg/Catch2](https://github.com/catchorg/Catch2) | 1,015 | 21,353 | C++ | 现代 C++ 单元测试框架，支持 TDD/BDD |
| 82 | [junegunn/fzf](https://github.com/junegunn/fzf) | 1,014 | 81,979 | Go | 命令行模糊查找神器 |
| 83 | [prometheus/prometheus](https://github.com/prometheus/prometheus) | 1,011 | 65,316 | Go | 监控与时序数据库领域的事实标准 |
| 84 | [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | 980 | 77,600 | Java | 开源分布式搜索与分析引擎 |
| 85 | [fatedier/frp](https://github.com/fatedier/frp) | 948 | 108,358 | Go | 内网穿透反向代理：把家里的服务暴露到公网 |
| 86 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | 948 | 31,564 | Java | Android TV 上按自己规则看媒体内容 |
| 87 | [rivet-dev/agentos](https://github.com/rivet-dev/agentos) | 926 | 4,140 | Rust | 给 Agent 装操作系统：当库嵌进你现有后端，不用沙箱/虚拟机/SaaS |
| 88 | [OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr) | 886 | 4,887 | JavaScript | 隐私优先的跨平台语音转文字听写应用 |
| 89 | [jj-vcs/jj](https://github.com/jj-vcs/jj) | 870 | 30,632 | Rust | 兼容 Git、又简单又强的新一代版本控制系统 Jujutsu |
| 90 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | 813 | 30,026 | Go | 基于 YAML 模板的高速漏洞扫描器 |
| 91 | [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | 811 | 27,052 | Java | AI 驱动的数据库客户端：自然语言查库、写 SQL，支持主流数据库 |
| 92 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | 799 | 38,193 | JavaScript | 免费好用的在线数据库绘图与 SQL 生成器 |
| 93 | [gosom/google-maps-scraper](https://github.com/gosom/google-maps-scraper) | 757 | 5,284 | Go | 抓谷歌地图店铺信息：地址电话评分评论等 |
| 94 | [skylot/jadx](https://github.com/skylot/jadx) | 756 | 49,791 | Java | Dex 转 Java 的反编译工具 |
| 95 | [helix-editor/helix](https://github.com/helix-editor/helix) | 740 | 45,602 | Rust | 后模态风格的现代文本编辑器 |
| 96 | [wealthfolio/wealthfolio](https://github.com/wealthfolio/wealthfolio) | 721 | 8,385 | Rust | 本地优先的个人理财与投资追踪 |
| 97 | [kunchenguid/treehouse](https://github.com/kunchenguid/treehouse) | 686 | 1,064 | Go | 不用自己折腾 git worktree：更省心的多工作树管理 |
| 98 | [andrewrabert/jellium-desktop](https://github.com/andrewrabert/jellium-desktop) | 654 | 1,643 | Rust | 非官方 Jellyfin 桌面客户端：把家庭影院搬到桌面上 |
| 99 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | 646 | 10,054 | Java | 把 GitHub Copilot Agent 嵌进自己应用/服务的多端 SDK |
| 100 | [argoproj/argo-cd](https://github.com/argoproj/argo-cd) | 628 | 23,730 | Go | Kubernetes 声明式持续部署（GitOps） |

---

## 怎么读这份榜

1. **先看主题**：本月风向比单个仓库名更重要。
2. **再看本月+★**：比累计 Star 更能反映「最近谁在爆」。
3. **按语言筛**：想学某门语言，可直接在语言分布里找入口。
4. **官方页只有约20条**：本文件是多语言月榜拼出来的扩展 Top100。

