# GitHub 本月热榜前100 · 通俗总结

> 数据来源：[https://github.com/trending?since=monthly](https://github.com/trending?since=monthly)  
> 抓取时间：2026-07-14 21:04（UTC: 2026-07-14T21:04:43.064266+00:00）  
> 说明：GitHub 官方月榜单页约20条；本报告按多语言月榜汇总去重后，按本月新增Star排序取前100。

---

## 一句话看懂本月风向

本月 GitHub 最热闹的，几乎都围着 **AI 干活**：AI Agent / 智能体、视频 / 多媒体 / 会议、知识库 / RAG / 记忆。
榜首前五是 **OpenMontage**、**Agent-Reach**、**codebase-memory-mcp**、**taste-skill**、**firecrawl**，榜首单月新增约 33,392 Star——大家在找「能替人干活的 AI 工具」，而不只是看模型本身。

## 本月热点主题（通俗版）

- **AI Agent / 智能体**（28 个）— 让 AI 自己规划、自己动手，而不是你一句一句喂指令。
- **网络 / 通信 / 隐私**（10 个）— 更私密的聊天、更稳的网络连接。
- **前端 / Web / UI**（9 个）— 网页界面、用自然语言操控页面。
- **视频 / 多媒体 / 会议**（8 个）— 剪视频、开会纪要、语音直播相关。
- **大模型 / LLM 基础设施**（8 个）— 提示词、网关、免费模型接入、省 Token 这类「底座」。
- **运维 / DevOps / 云**（7 个）— 部署、云原生相关工具。
- **AI 编程助手 / 开发工具**（6 个）— 写代码、改代码、管一堆 Agent 一起干活的工具。
- **数据库 / 存储**（5 个）— 更快的向量库、日志库等基础设施。
- **知识库 / RAG / 记忆**（4 个）— 给 AI 装长期记忆，别聊完就忘。
- **安全 / 渗透测试**（4 个）— 用 AI 找漏洞、做安全检测。
- **其他开源项目**（4 个）— 不好归类、但本月同样很火的项目。
- **爬虫 / 数据采集**（3 个）— 帮 AI 或人把网页/社交内容抓干净。
- **金融 / 量化 / 股票**（2 个）— 看盘、分析行情的自动化工具。
- **语言 / 框架 / 基础库**（2 个）— 老牌好用的底层库持续被关注。

## 语言分布（前100）

| 语言 | 项目数 | 本月新增Star合计 |
|---|---:|---:|
| Python | 20 | 177,581 |
| TypeScript | 20 | 134,965 |
| Rust | 19 | 61,191 |
| Go | 17 | 28,190 |
| JavaScript | 12 | 62,623 |
| Java | 7 | 12,584 |
| C++ | 2 | 5,999 |
| C | 1 | 27,660 |
| Haskell | 1 | 7,461 |
| HTML | 1 | 6,484 |

## Top 10 速览（本月最火）

### 1. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)

- **本月+33,392 ★**｜累计 38,481 ★｜Fork 4,664｜语言 Python
- **通俗说**：把 AI 编程助手变成整套视频制作工作室（多流水线+大量技能包）
- **原简介**：World's first open-source, agentic video production system. 12 pipelines, 52 tools, 500+ agent skills. Turn your AI coding assistant into a full video production studio.
- **归类**：AI Agent / 智能体

### 2. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

- **本月+28,900 ★**｜累计 56,211 ★｜Fork 4,624｜语言 Python
- **通俗说**：给 AI 装眼睛：读搜 Twitter/Reddit/B站/小红书等，基本不用付 API 费
- **原简介**：Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.
- **归类**：AI Agent / 智能体

### 3. [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

- **本月+27,660 ★**｜累计 31,489 ★｜Fork 2,507｜语言 C
- **通俗说**：超快代码知识图谱 MCP，让 AI 查代码少烧 Token
- **原简介**：High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **归类**：知识库 / RAG / 记忆

### 4. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

- **本月+20,264 ★**｜累计 63,462 ★｜Fork 4,484｜语言 JavaScript
- **通俗说**：教 AI 更有审美，少产出千篇一律的「AI 味」内容
- **原简介**：Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop
- **归类**：前端 / Web / UI

### 5. [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)

- **本月+18,851 ★**｜累计 150,984 ★｜Fork 8,623｜语言 TypeScript
- **通俗说**：把任意网页变成干净、结构化数据，方便给 AI 用
- **原简介**：The API to search, scrape, and interact with the web at scale. 🔥
- **归类**：爬虫 / 数据采集

### 6. [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks)

- **本月+15,390 ★**｜累计 57,728 ★｜Fork 9,548｜语言 JavaScript
- **通俗说**：汇总各大 AI（Claude/GPT/Gemini/Grok 等）系统提示词泄露内容
- **原简介**：Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT GPT-5.6, Codex GPT-5.6, GPT-5.5. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly.
- **归类**：网络 / 通信 / 隐私

### 7. [usestrix/strix](https://github.com/usestrix/strix)

- **本月+15,337 ★**｜累计 41,466 ★｜Fork 4,362｜语言 Python
- **通俗说**：开源 AI 渗透测试工具，帮你找应用漏洞
- **原简介**：Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **归类**：安全 / 渗透测试

### 8. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)

- **本月+14,992 ★**｜累计 57,203 ★｜Fork 49,218｜语言 Python
- **通俗说**：LLM 驱动的多市场股票智能分析：行情+新闻+看板+自动推送
- **原简介**：LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs.
- **归类**：金融 / 量化 / 股票

### 9. [iptv-org/iptv](https://github.com/iptv-org/iptv)

- **本月+14,736 ★**｜累计 132,971 ★｜Fork 7,590｜语言 TypeScript
- **通俗说**：全球公开 IPTV 直播源合集，想看电视频道的人都在用
- **原简介**：Collection of publicly available IPTV channels from all over the world
- **归类**：视频 / 多媒体 / 会议

### 10. [stablyai/orca](https://github.com/stablyai/orca)

- **本月+13,222 ★**｜累计 19,036 ★｜Fork 1,488｜语言 TypeScript
- **通俗说**：同时调度一堆编程 Agent 的桌面/手机 ADE
- **原简介**：Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop and mobile.
- **归类**：AI Agent / 智能体

## 完整前100名单

| 排名 | 仓库 | 本月+★ | 累计★ | 语言 | 通俗一句话 |
|---:|---|---:|---:|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 33,392 | 38,481 | Python | 把 AI 编程助手变成整套视频制作工作室（多流水线+大量技能包） |
| 2 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 28,900 | 56,211 | Python | 给 AI 装眼睛：读搜 Twitter/Reddit/B站/小红书等，基本不用付 API 费 |
| 3 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 27,660 | 31,489 | C | 超快代码知识图谱 MCP，让 AI 查代码少烧 Token |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 20,264 | 63,462 | JavaScript | 教 AI 更有审美，少产出千篇一律的「AI 味」内容 |
| 5 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 18,851 | 150,984 | TypeScript | 把任意网页变成干净、结构化数据，方便给 AI 用 |
| 6 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 15,390 | 57,728 | JavaScript | 汇总各大 AI（Claude/GPT/Gemini/Grok 等）系统提示词泄露内容 |
| 7 | [usestrix/strix](https://github.com/usestrix/strix) | 15,337 | 41,466 | Python | 开源 AI 渗透测试工具，帮你找应用漏洞 |
| 8 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | 14,992 | 57,203 | Python | LLM 驱动的多市场股票智能分析：行情+新闻+看板+自动推送 |
| 9 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 14,736 | 132,971 | TypeScript | 全球公开 IPTV 直播源合集，想看电视频道的人都在用 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca) | 13,222 | 19,036 | TypeScript | 同时调度一堆编程 Agent 的桌面/手机 ADE |
| 11 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | 11,369 | 28,268 | TypeScript | 一条命令让 AI 编程助手克隆任意网站 |
| 12 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | 11,340 | 24,595 | Rust | 本地隐私优先的 AI 会议助手：实时转写+说话人分离+总结 |
| 13 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | 11,302 | 41,276 | TypeScript | 开源 AI 语音工作室：克隆声音、听写、创作 |
| 14 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 10,603 | 17,285 | TypeScript | 免费 AI 网关：一个入口接 200+ 厂商，还能省 Token |
| 15 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | 10,569 | 16,452 | Rust | 终端里的 Agent 多路复用器，同时盯多个智能体 |
| 16 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 10,374 | 22,751 | Python | 属于你自己的个人交易 Agent |
| 17 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | 10,100 | 69,021 | TypeScript | 开源版剪映（CapCut）替代品 |
| 18 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 10,039 | 25,568 | Python | 给 AI Agent 用的 800+ 结构化网络安全技能包 |
| 19 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | 10,013 | 27,865 | Python | 给 AI Agent 装长期记忆的开源知识图谱平台 |
| 20 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | 8,987 | 13,168 | Python | 扫描 AI Agent 技能包里的漏洞与恶意模式 |
| 21 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 8,434 | 46,679 | JavaScript | 设计语言规范，让 AI 做设计更靠谱 |
| 22 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | 8,001 | 26,601 | TypeScript | 页面内 GUI 智能体：用自然语言操控网页界面 |
| 23 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 7,880 | 177,994 | Python | 功能很全的命令行音视频下载器 |
| 24 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | 7,632 | 28,617 | JavaScript | 在 Claude Code 里调用 Codex：审代码或委派任务 |
| 25 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | 7,461 | 18,625 | Haskell | 不靠用户 ID 的私密即时通讯网络 |
| 26 | [openai/codex](https://github.com/openai/codex) | 7,187 | 98,047 | Rust | 跑在终端里的轻量编程 Agent（OpenAI Codex） |
| 27 | [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | 6,503 | 87,091 | Java | 在线/本地都能用的全能 PDF 编辑神器 |
| 28 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | 6,484 | 7,009 | HTML | Google Cloud 知识目录相关工具与样例 |
| 29 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | 6,421 | 12,704 | Python | 用轨迹优化给冻结大模型 Agent「训练」可复用技能 |
| 30 | [google-research/timesfm](https://github.com/google-research/timesfm) | 6,286 | 26,866 | Python | 谷歌的时间序列基础模型，专门做预测 |
| 31 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | 6,081 | 8,434 | Python | 让 Claude 能「看视频」：下载、抽帧、转写一并交给它 |
| 32 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | 5,751 | 35,654 | TypeScript | 开源 NotebookLM 替代：更灵活的笔记+问答笔记本 |
| 33 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | 5,627 | 61,852 | TypeScript | 全球实时情报看板：AI 聚合新闻与地缘/基建监测 |
| 34 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 5,285 | 56,499 | Python | 小红书/抖音/B站/微博等主流平台媒体爬虫 |
| 35 | [alibaba/zvec](https://github.com/alibaba/zvec) | 5,124 | 14,892 | C++ | 轻量高速的进程内向量数据库 |
| 36 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | 4,819 | 6,196 | Go | 减少 git push 出错的小工具/工作流 |
| 37 | [t8y2/dbx](https://github.com/t8y2/dbx) | 4,768 | 10,010 | Rust | 约 20MB 的跨平台轻量数据库客户端（多引擎） |
| 38 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | 4,688 | 10,334 | TypeScript | 可自托管的旅行规划器：协作地图、预算、行李清单 |
| 39 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | 4,624 | 5,835 | Python | 用 AI 自动评估简历、打分的招聘助手 |
| 40 | [immich-app/immich](https://github.com/immich-app/immich) | 4,533 | 107,673 | TypeScript | 高性能自托管相册：照片视频自己管 |
| 41 | [makeplane/plane](https://github.com/makeplane/plane) | 3,809 | 54,467 | TypeScript | 开源项目管理：对标 Jira/Linear/ClickUp |
| 42 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 3,705 | 10,151 | Rust | 给 AI Agent 用的轻量安全沙箱：即开即跑 |
| 43 | [tursodatabase/turso](https://github.com/tursodatabase/turso) | 3,687 | 22,853 | Rust | 兼容 SQLite 的进程内 SQL 数据库 |
| 44 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | 3,515 | 4,516 | JavaScript | Agent 技能：一键生成好看的架构图并可导出 |
| 45 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 3,511 | 46,929 | TypeScript | 给编程 Agent 用的 Chrome DevTools MCP |
| 46 | [n0-computer/iroh](https://github.com/n0-computer/iroh) | 2,981 | 11,705 | Rust | 给应用加上 QUIC + NAT 穿透，用密钥拨号而不是 IP |
| 47 | [cjpais/Handy](https://github.com/cjpais/Handy) | 2,878 | 26,520 | Rust | 完全离线的开源语音转文字应用 |
| 48 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | 2,718 | 29,687 | Rust | 一条命令行搞定 Drive/Gmail/日历/表格等 Workspace |
| 49 | [IceWhaleTech/CasaOS](https://github.com/IceWhaleTech/CasaOS) | 2,634 | 36,660 | Go | 简单好看的开源个人云/家庭 NAS 系统 |
| 50 | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 2,516 | 85,039 | Go | 开源 RAG 引擎：检索增强生成+Agent 能力 |
| 51 | [rommapp/romm](https://github.com/rommapp/romm) | 2,182 | 11,144 | Python | 好看又好用的自托管 ROM 管理与模拟器播放器 |
| 52 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | 2,158 | 4,406 | Go | 本地优先：搜索/分析编程 Agent 会话与 Token 消耗 |
| 53 | [every-app/open-seo](https://github.com/every-app/open-seo) | 2,123 | 4,314 | TypeScript | 开源 SEO 工具，对标 Semrush/Ahrefs |
| 54 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | 2,056 | 128,508 | Java | 动画图解的数据结构与算法教程（多语言） |
| 55 | [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | 2,055 | 8,249 | TypeScript | 给 Claude 装终端/文件/diff 能力的 MCP 服务 |
| 56 | [rust-lang/rust](https://github.com/rust-lang/rust) | 2,054 | 114,718 | Rust | Rust 语言本体：可靠、高效的系统级编程 |
| 57 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 2,042 | 18,281 | Go | 腾讯开源 LLM 知识平台：文档变 RAG+推理 Agent |
| 58 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 1,855 | 123,782 | Go | 生产级容器编排与集群管理系统 |
| 59 | [LMCache/LMCache](https://github.com/LMCache/LMCache) | 1,772 | 10,550 | Python | 给大模型加速的 KV Cache 层 |
| 60 | [juanfont/headscale](https://github.com/juanfont/headscale) | 1,733 | 41,721 | Go | 自托管版 Tailscale 控制面 |
| 61 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | 1,684 | 4,101 | JavaScript | 网文写作全流程 Skill：扫榜、拆文、去 AI 味、封面 |
| 62 | [Universal-Debloater-Alliance/universal-android-debloater-next-generation](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation) | 1,642 | 8,415 | Rust | 一键精简安卓预装应用，提升隐私与性能 |
| 63 | [openai/plugins](https://github.com/openai/plugins) | 1,623 | 4,577 | JavaScript | OpenAI 插件相关开源能力 |
| 64 | [tailscale/tailscale](https://github.com/tailscale/tailscale) | 1,499 | 33,960 | Go | 最简单好用的 WireGuard 组网（含 2FA） |
| 65 | [Kong/insomnia](https://github.com/Kong/insomnia) | 1,484 | 39,898 | TypeScript | 开源跨平台 API 客户端（REST/GraphQL/gRPC 等） |
| 66 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) | 1,370 | 66,119 | Rust | 极速命令行正则搜索，自动尊重 .gitignore |
| 67 | [charmbracelet/crush](https://github.com/charmbracelet/crush) | 1,364 | 26,559 | Go | 好看又好用的终端编程 Agent 体验 |
| 68 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 1,363 | 7,376 | TypeScript | 配合 Stitch MCP 的 Agent Skills 技能库 |
| 69 | [THUDM/slime](https://github.com/THUDM/slime) | 1,345 | 7,457 | Python | 面向 RL Scaling 的大模型后训练框架 |
| 70 | [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech) | 1,281 | 6,152 | Python | 用开源模型搭本地语音对话 Agent |
| 71 | [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | 1,276 | 24,694 | Rust | 生产级 Rust 原生量化交易引擎 |
| 72 | [yorukot/superfile](https://github.com/yorukot/superfile) | 1,266 | 18,732 | Go | 好看现代的终端文件管理器 |
| 73 | [NVIDIA/skills](https://github.com/NVIDIA/skills) | 1,249 | 2,496 | Python | NVIDIA 发布的 AI Agent 技能包 |
| 74 | [denoland/deno](https://github.com/denoland/deno) | 1,224 | 107,784 | Rust | 现代 JavaScript/TypeScript 运行时 |
| 75 | [kunchenguid/gnhf](https://github.com/kunchenguid/gnhf) | 1,161 | 3,202 | TypeScript | 睡前跟 Agents 道晚安：让它们夜间继续干活 |
| 76 | [cupy/cupy](https://github.com/cupy/cupy) | 1,141 | 12,137 | Python | GPU 版 NumPy/SciPy，科学计算加速 |
| 77 | [prometheus/prometheus](https://github.com/prometheus/prometheus) | 1,123 | 65,211 | Go | 监控与时序数据库领域的事实标准 |
| 78 | [binwiederhier/ntfy](https://github.com/binwiederhier/ntfy) | 1,119 | 31,850 | Go | 用简单 HTTP 给手机/桌面推送通知 |
| 79 | [junegunn/fzf](https://github.com/junegunn/fzf) | 1,089 | 81,716 | Go | 命令行模糊查找神器 |
| 80 | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | 1,063 | 64,982 | Rust | 面向低成本模型的编程 Agent |
| 81 | [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | 1,061 | 77,613 | Java | 开源分布式搜索与分析引擎 |
| 82 | [rpamis/comet](https://github.com/rpamis/comet) | 1,027 | 2,272 | JavaScript | 把想法变成可评估工作流的 Agent Skill 框架 |
| 83 | [hashicorp/terraform](https://github.com/hashicorp/terraform) | 962 | 49,461 | Go | 用代码安全、可预期地管理基础设施 |
| 84 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | 953 | 2,539 | JavaScript | 非官方 Linux 版 ChatGPT/Codex 桌面客户端 |
| 85 | [ocornut/imgui](https://github.com/ocornut/imgui) | 875 | 74,655 | C++ | 轻量级 C++ 即时模式 GUI 库 |
| 86 | [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | 864 | 157,031 | JavaScript | Java 面试与后端通关指南（含 AI 应用） |
| 87 | [swc-project/swc](https://github.com/swc-project/swc) | 820 | 34,247 | Rust | Rust 写的前端编译/打包平台 |
| 88 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | 805 | 35,653 | Java | 开源身份认证与访问管理（IAM） |
| 89 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | 785 | 31,318 | Java | Android TV 上按自己规则看媒体内容 |
| 90 | [getarcaneapp/arcane](https://github.com/getarcaneapp/arcane) | 726 | 6,433 | Go | 现代、好上手的 Docker 管理界面 |
| 91 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | 693 | 29,830 | Go | 基于 YAML 模板的高速漏洞扫描器 |
| 92 | [skylot/jadx](https://github.com/skylot/jadx) | 692 | 49,690 | Java | Dex 转 Java 的反编译工具 |
| 93 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | 682 | 4,463 | Java | 用 Java 构建分布式、可长期运行的 Agent |
| 94 | [ArnasDon/wacrm](https://github.com/ArnasDon/wacrm) | 676 | 1,547 | TypeScript | 可自托管的 WhatsApp CRM：收件箱、线索、自动化 |
| 95 | [helix-editor/helix](https://github.com/helix-editor/helix) | 668 | 45,422 | Rust | 后模态风格的现代文本编辑器 |
| 96 | [fastify/fastify](https://github.com/fastify/fastify) | 644 | 36,814 | JavaScript | Node.js 高性能低开销 Web 框架 |
| 97 | [wealthfolio/wealthfolio](https://github.com/wealthfolio/wealthfolio) | 644 | 8,247 | Rust | 本地优先的个人理财与投资追踪 |
| 98 | [biomejs/biome](https://github.com/biomejs/biome) | 597 | 25,409 | Rust | 前端工具链：格式化+Lint，Rust 实现 |
| 99 | [expressjs/express](https://github.com/expressjs/express) | 593 | 69,369 | JavaScript | 经典精简的 Node.js Web 框架 |
| 100 | [argoproj/argo-cd](https://github.com/argoproj/argo-cd) | 592 | 23,699 | Go | Kubernetes 声明式持续部署（GitOps） |

---

## 怎么读这份榜

1. **先看主题**：本月风向比单个仓库名更重要。
2. **再看本月+★**：比累计 Star 更能反映「最近谁在爆」。
3. **按语言筛**：想学某门语言，可直接在语言分布里找入口。
4. **官方页只有约20条**：本文件是多语言月榜拼出来的扩展 Top100。

