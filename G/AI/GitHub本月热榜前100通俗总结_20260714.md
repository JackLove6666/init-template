# GitHub 本月热榜前100 · 通俗总结

> 数据来源：[https://github.com/trending?since=monthly](https://github.com/trending?since=monthly)  
> 抓取时间：2026-07-14 16:12（UTC: 2026-07-14T16:12:54.133785+00:00）  
> 说明：GitHub 官方月榜单页约20条；本报告按多语言月榜汇总去重后，按本月新增Star排序取前100。

---

## 一句话看懂本月风向

本月 GitHub 最热闹的，几乎都围着 **AI 干活**：视频制作、代码记忆、上网搜索、安全测试、并行编程助手。榜首前五是 **OpenMontage**、**Agent-Reach**、**codebase-memory-mcp**、**taste-skill**、**firecrawl**，单月新增 Star 轻松过万——大家在找「能替人干活的 AI 工具」，而不只是看模型本身。

## 本月热点主题（通俗版）

- **AI Agent / 智能体**（28 个）— 让 AI 自己规划、自己动手，而不是你一句一句喂指令。
- **AI 编程助手 / 开发工具**（12 个）— 写代码、改代码、管一堆 Agent 一起干活的工具。
- **大模型 / LLM 基础设施**（9 个）— 提示词、网关、免费模型接入、省 Token 这类「底座」。
- **其他开源项目**（15 个）— 不好归类、但本月同样很火的项目。
- **前端 / Web / UI**（6 个）— 网页界面、用自然语言操控页面。
- **爬虫 / 数据采集**（2 个）— 帮 AI 或人把网页/社交内容抓干净。
- **网络 / 通信 / 隐私**（6 个）— 更私密的聊天、更稳的网络连接。
- **安全 / 渗透测试**（4 个）— 用 AI 找漏洞、做安全检测。
- **视频 / 多媒体 / 会议**（2 个）— 剪视频、开会纪要、语音直播相关。
- **知识库 / RAG / 记忆**（3 个）— 给 AI 装长期记忆，别聊完就忘。
- **运维 / DevOps / 云**（6 个）— 部署、云原生相关工具。
- **数据库 / 存储**（3 个）— 更快的向量库、日志库等基础设施。
- **移动 / 跨端**（1 个）— 手机端、跨平台应用。
- **语言 / 框架 / 基础库**（2 个）— 老牌好用的底层库持续被关注。
- **金融 / 量化 / 股票**（1 个）— 看盘、分析行情的自动化工具。

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

- **本月+33,392 ★**｜累计 38,420 ★｜Fork 4,659｜语言 Python
- **通俗说**：把 AI 编程助手变成整套视频制作工作室（多流水线+大量技能包）
- **原简介**：World's first open-source, agentic video production system. 12 pipelines, 52 tools, 500+ agent skills. Turn your AI coding assistant into a full video production studio.
- **归类**：AI Agent / 智能体

### 2. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

- **本月+28,900 ★**｜累计 56,144 ★｜Fork 4,630｜语言 Python
- **通俗说**：给 AI 装眼睛：读搜 Twitter/Reddit/B站/小红书等，基本不用付 API 费
- **原简介**：Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.
- **归类**：AI Agent / 智能体

### 3. [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

- **本月+27,660 ★**｜累计 31,427 ★｜Fork 2,509｜语言 C
- **通俗说**：超快代码知识图谱 MCP，让 AI 查代码少烧 Token
- **原简介**：High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **归类**：大模型 / LLM 基础设施

### 4. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

- **本月+20,264 ★**｜累计 63,397 ★｜Fork 4,487｜语言 JavaScript
- **通俗说**：教 AI 更有审美，少产出千篇一律的「AI 味」内容
- **原简介**：Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop
- **归类**：前端 / Web / UI

### 5. [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)

- **本月+18,851 ★**｜累计 150,876 ★｜Fork 8,615｜语言 TypeScript
- **通俗说**：把任意网页变成干净、结构化数据，方便给 AI 用
- **原简介**：The API to search, scrape, and interact with the web at scale. 🔥
- **归类**：爬虫 / 数据采集

### 6. [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks)

- **本月+15,390 ★**｜累计 57,663 ★｜Fork 9,536｜语言 JavaScript
- **通俗说**：汇总各大 AI（Claude/GPT/Gemini/Grok 等）系统提示词泄露内容
- **原简介**：Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT GPT-5.6, Codex GPT-5.6, GPT-5.5. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly.
- **归类**：AI 编程助手 / 开发工具

### 7. [usestrix/strix](https://github.com/usestrix/strix)

- **本月+15,337 ★**｜累计 41,408 ★｜Fork 4,362｜语言 Python
- **通俗说**：开源 AI 渗透测试工具，帮你找应用漏洞
- **原简介**：Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **归类**：安全 / 渗透测试

### 8. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)

- **本月+14,992 ★**｜累计 57,194 ★｜Fork 49,208｜语言 Python
- **通俗说**：每日股票分析自动化相关开源项目
- **原简介**：LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs.
- **归类**：大模型 / LLM 基础设施

### 9. [iptv-org/iptv](https://github.com/iptv-org/iptv)

- **本月+14,736 ★**｜累计 132,929 ★｜Fork 7,591｜语言 TypeScript
- **通俗说**：全球 IPTV 直播源合集，想看电视频道的人都在用
- **原简介**：Collection of publicly available IPTV channels from all over the world
- **归类**：视频 / 多媒体 / 会议

### 10. [stablyai/orca](https://github.com/stablyai/orca)

- **本月+13,222 ★**｜累计 18,946 ★｜Fork 1,488｜语言 TypeScript
- **通俗说**：同时调度一堆编程 Agent 的桌面/手机 ADE
- **原简介**：Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop and mobile.
- **归类**：AI Agent / 智能体

## 完整前100名单

| 排名 | 仓库 | 本月+★ | 累计★ | 语言 | 通俗一句话 |
|---:|---|---:|---:|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 33,392 | 38,420 | Python | 把 AI 编程助手变成整套视频制作工作室（多流水线+大量技能包） |
| 2 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 28,900 | 56,144 | Python | 给 AI 装眼睛：读搜 Twitter/Reddit/B站/小红书等，基本不用付 API 费 |
| 3 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 27,660 | 31,427 | C | 超快代码知识图谱 MCP，让 AI 查代码少烧 Token |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 20,264 | 63,397 | JavaScript | 教 AI 更有审美，少产出千篇一律的「AI 味」内容 |
| 5 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 18,851 | 150,876 | TypeScript | 把任意网页变成干净、结构化数据，方便给 AI 用 |
| 6 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 15,390 | 57,663 | JavaScript | 汇总各大 AI（Claude/GPT/Gemini/Grok 等）系统提示词泄露内容 |
| 7 | [usestrix/strix](https://github.com/usestrix/strix) | 15,337 | 41,408 | Python | 开源 AI 渗透测试工具，帮你找应用漏洞 |
| 8 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | 14,992 | 57,194 | Python | 每日股票分析自动化相关开源项目 |
| 9 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 14,736 | 132,929 | TypeScript | 全球 IPTV 直播源合集，想看电视频道的人都在用 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca) | 13,222 | 18,946 | TypeScript | 同时调度一堆编程 Agent 的桌面/手机 ADE |
| 11 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | 11,369 | 28,254 | TypeScript | 用 AI 快速克隆网站的模板 |
| 12 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | 11,340 | 24,529 | Rust | 本地跑的 AI 会议助手：转写+纪要，不上传云端 |
| 13 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | 11,302 | 41,216 | TypeScript | 语音相关开源工具，本月热度很高 |
| 14 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 10,603 | 17,221 | TypeScript | 免费 AI 网关：一个入口接 200+ 模型，还省 Token |
| 15 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | 10,569 | 16,393 | Rust | 终端里的 Agent 多路复用器，同时管多个智能体 |
| 16 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 10,374 | 22,621 | Python | "Vibe-Trading: Your Personal Trading Agent" |
| 17 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | 10,100 | 68,844 | TypeScript | The open-source CapCut alternative |
| 18 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 10,039 | 25,561 | Python | 817 structured cybersecurity skills for AI agents · Mapped to 6 fra... |
| 19 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | 10,013 | 27,841 | Python | 给 Agent 做长期记忆的开源知识图谱引擎 |
| 20 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | 8,987 | 13,156 | Python | Security scanner for AI agent skills. Detect vulnerabilities, malic... |
| 21 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 8,434 | 46,612 | JavaScript | The design language that makes your AI harness better at design. |
| 22 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | 8,001 | 26,587 | TypeScript | 用自然语言直接操控网页界面的前端 Agent |
| 23 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 7,880 | 177,952 | Python | A feature-rich command-line audio/video downloader |
| 24 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | 7,632 | 28,581 | JavaScript | Use Codex from Claude Code to review code or delegate tasks. |
| 25 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | 7,461 | 18,621 | Haskell | 没有用户 ID 的私密即时通讯，强调隐私 |
| 26 | [openai/codex](https://github.com/openai/codex) | 7,187 | 98,016 | Rust | Lightweight coding agent that runs in your terminal |
| 27 | [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | 6,503 | 87,080 | Java | #1 PDF Application on GitHub that lets you edit PDFs on any device ... |
| 28 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | 6,484 | 6,973 | HTML | 谷歌云知识目录相关工具与示例 |
| 29 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | 6,421 | 12,687 | Python | SkillOpt is a text-space optimizer that trains reusable natural-lan... |
| 30 | [google-research/timesfm](https://github.com/google-research/timesfm) | 6,286 | 26,862 | Python | TimesFM (Time Series Foundation Model) is a pretrained time-series ... |
| 31 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | 6,081 | 8,397 | Python | Give Claude the ability to watch any video. /watch downloads, extra... |
| 32 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | 5,751 | 35,653 | TypeScript | An Open Source implementation of Notebook LM with more flexibility ... |
| 33 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | 5,627 | 61,844 | TypeScript | Real-time global intelligence dashboard. AI-powered news aggregatio... |
| 34 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 5,285 | 56,489 | Python | 小红书笔记 \| 评论爬虫、抖音视频 \| 评论爬虫、快手视频 \| 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖... |
| 35 | [alibaba/zvec](https://github.com/alibaba/zvec) | 5,124 | 14,883 | C++ | 轻量高速的进程内向量数据库 |
| 36 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | 4,819 | 6,176 | Go | 减少 git push 失误的小工具 |
| 37 | [t8y2/dbx](https://github.com/t8y2/dbx) | 4,768 | 10,003 | Rust | 20MB, lightweight, cross-platform database client. Supports MySQL, ... |
| 38 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | 4,688 | 10,323 | TypeScript | A self-hosted travel/trip planner with real-time collaboration, int... |
| 39 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | 4,624 | 5,825 | Python | AI 自动评估、打分简历 |
| 40 | [immich-app/immich](https://github.com/immich-app/immich) | 4,533 | 107,660 | TypeScript | High performance self-hosted photo and video management solution. |
| 41 | [makeplane/plane](https://github.com/makeplane/plane) | 3,809 | 54,457 | TypeScript | 🔥🔥🔥 Open-source Jira, Linear, Monday, and ClickUp alternative. Plan... |
| 42 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 3,705 | 10,147 | Rust | Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents. |
| 43 | [tursodatabase/turso](https://github.com/tursodatabase/turso) | 3,687 | 22,850 | Rust | Turso is an in-process SQL database, compatible with SQLite. |
| 44 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | 3,515 | 4,462 | JavaScript | Any agent Skill: generate beautiful architecture diagrams with dark... |
| 45 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 3,511 | 46,922 | TypeScript | Chrome DevTools for coding agents |
| 46 | [n0-computer/iroh](https://github.com/n0-computer/iroh) | 2,981 | 11,699 | Rust | 用 QUIC+NAT 穿透让应用更好连网 |
| 47 | [cjpais/Handy](https://github.com/cjpais/Handy) | 2,878 | 26,502 | Rust | A free, open source, and extensible speech-to-text application that... |
| 48 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | 2,718 | 29,683 | Rust | Google Workspace CLI — one command-line tool for Drive, Gmail, Cale... |
| 49 | [IceWhaleTech/CasaOS](https://github.com/IceWhaleTech/CasaOS) | 2,634 | 36,650 | Go | CasaOS - A simple, easy-to-use, elegant open-source Personal Cloud ... |
| 50 | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 2,516 | 85,032 | Go | RAGFlow is a leading open-source Retrieval-Augmented Generation (RA... |
| 51 | [rommapp/romm](https://github.com/rommapp/romm) | 2,182 | 11,145 | Python | A beautiful, powerful, self-hosted rom manager and player. |
| 52 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | 2,158 | 4,405 | Go | Local-first session search, analytics, insights, and token use stat... |
| 53 | [every-app/open-seo](https://github.com/every-app/open-seo) | 2,123 | 4,310 | TypeScript | Open source alternative to Semrush and Ahrefs |
| 54 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | 2,056 | 128,506 | Java | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、English、日本語，提供 Python, Java,... |
| 55 | [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | 2,055 | 8,234 | TypeScript | 给 Claude 终端/文件系统控制能力的 MCP |
| 56 | [rust-lang/rust](https://github.com/rust-lang/rust) | 2,054 | 114,723 | Rust | Empowering everyone to build reliable and efficient software. |
| 57 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 2,042 | 18,279 | Go | Open-source LLM knowledge platform: turn raw documents into a query... |
| 58 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 1,855 | 123,793 | Go | Production-Grade Container Scheduling and Management |
| 59 | [LMCache/LMCache](https://github.com/LMCache/LMCache) | 1,772 | 10,547 | Python | LMCache: Supercharge Your LLM with the Fastest KV Cache Layer |
| 60 | [juanfont/headscale](https://github.com/juanfont/headscale) | 1,733 | 41,711 | Go | An open source, self-hosted implementation of the Tailscale control... |
| 61 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | 1,684 | 4,095 | JavaScript | 网文/小说写作 skill 包，覆盖长篇与短篇网络小说的扫榜、拆文、写作、去AI味、封面图全流程 |
| 62 | [Universal-Debloater-Alliance/universal-android-debloater-next-generation](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation) | 1,642 | 8,415 | Rust | Cross-platform GUI written in Rust using ADB to debloat non-rooted ... |
| 63 | [openai/plugins](https://github.com/openai/plugins) | 1,623 | 4,574 | JavaScript | OpenAI Plugins |
| 64 | [tailscale/tailscale](https://github.com/tailscale/tailscale) | 1,499 | 33,961 | Go | The easiest, most secure way to use WireGuard and 2FA. |
| 65 | [Kong/insomnia](https://github.com/Kong/insomnia) | 1,484 | 39,898 | TypeScript | The open-source, cross-platform API client for GraphQL, REST, WebSo... |
| 66 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) | 1,370 | 66,113 | Rust | ripgrep recursively searches directories for a regex pattern while ... |
| 67 | [charmbracelet/crush](https://github.com/charmbracelet/crush) | 1,364 | 26,555 | Go | Glamourous agentic coding for all 💘 |
| 68 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 1,363 | 7,374 | TypeScript | A library of Agent Skills designed to work with the Stitch MCP serv... |
| 69 | [THUDM/slime](https://github.com/THUDM/slime) | 1,345 | 7,456 | Python | slime is an LLM post-training framework for RL Scaling. |
| 70 | [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech) | 1,281 | 6,156 | Python | Build local voice agents with open-source models |
| 71 | [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | 1,276 | 24,692 | Rust | Production-grade Rust-native trading engine with deterministic even... |
| 72 | [yorukot/superfile](https://github.com/yorukot/superfile) | 1,266 | 18,733 | Go | Pretty fancy and modern terminal file manager |
| 73 | [NVIDIA/skills](https://github.com/NVIDIA/skills) | 1,249 | 2,491 | Python | AI agent skills published by NVIDIA |
| 74 | [denoland/deno](https://github.com/denoland/deno) | 1,224 | 107,792 | Rust | A modern runtime for JavaScript and TypeScript. |
| 75 | [kunchenguid/gnhf](https://github.com/kunchenguid/gnhf) | 1,161 | 3,199 | TypeScript | Before I go to bed, I tell my agents: good night, have fun |
| 76 | [cupy/cupy](https://github.com/cupy/cupy) | 1,141 | 12,133 | Python | NumPy & SciPy for GPU |
| 77 | [prometheus/prometheus](https://github.com/prometheus/prometheus) | 1,123 | 65,209 | Go | The Prometheus monitoring system and time series database. |
| 78 | [binwiederhier/ntfy](https://github.com/binwiederhier/ntfy) | 1,119 | 31,843 | Go | Send push notifications to your phone or desktop using PUT/POST |
| 79 | [junegunn/fzf](https://github.com/junegunn/fzf) | 1,089 | 81,713 | Go | 🌸 A command-line fuzzy finder |
| 80 | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | 1,063 | 64,947 | Rust | A lightweight coding agent, optimized for open models like GLM, Dee... |
| 81 | [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | 1,061 | 77,618 | Java | Free and Open Source, Distributed, RESTful Search Engine |
| 82 | [rpamis/comet](https://github.com/rpamis/comet) | 1,027 | 2,269 | JavaScript | Comet: agent skill harness for turning ideas into evaluated workflows |
| 83 | [hashicorp/terraform](https://github.com/hashicorp/terraform) | 962 | 49,471 | Go | Terraform enables you to safely and predictably create, change, and... |
| 84 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | 953 | 2,532 | JavaScript | Unofficial ChatGPT desktop app for Linux (formerly the Codex app), ... |
| 85 | [ocornut/imgui](https://github.com/ocornut/imgui) | 875 | 74,646 | C++ | 轻量级 C++ 即时模式 GUI 库 Dear ImGui |
| 86 | [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | 864 | 157,031 | JavaScript | Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发 |
| 87 | [swc-project/swc](https://github.com/swc-project/swc) | 820 | 34,255 | Rust | Rust-based platform for the Web |
| 88 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | 805 | 35,650 | Java | Open Source Identity and Access Management For Modern Applications ... |
| 89 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | 785 | 31,317 | Java | Browse media content with your own rules on Android TV |
| 90 | [getarcaneapp/arcane](https://github.com/getarcaneapp/arcane) | 726 | 6,433 | Go | Modern Docker Management, Designed for Everyone |
| 91 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | 693 | 29,833 | Go | Nuclei is a fast, customizable vulnerability scanner powered by the... |
| 92 | [skylot/jadx](https://github.com/skylot/jadx) | 692 | 49,693 | Java | Dex to Java decompiler |
| 93 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | 682 | 4,462 | Java | Build distributed, production-grade, long-running agents. |
| 94 | [ArnasDon/wacrm](https://github.com/ArnasDon/wacrm) | 676 | 1,542 | TypeScript | Self-hostable CRM template for WhatsApp — shared inbox, contacts, s... |
| 95 | [helix-editor/helix](https://github.com/helix-editor/helix) | 668 | 45,416 | Rust | A post-modern modal text editor. |
| 96 | [fastify/fastify](https://github.com/fastify/fastify) | 644 | 36,817 | JavaScript | Fast and low overhead web framework, for Node.js |
| 97 | [wealthfolio/wealthfolio](https://github.com/wealthfolio/wealthfolio) | 644 | 8,244 | Rust | A beautiful, private, local-first personal finance tracker. Investm... |
| 98 | [biomejs/biome](https://github.com/biomejs/biome) | 597 | 25,420 | Rust | A toolchain for web projects, aimed to provide functionalities to m... |
| 99 | [expressjs/express](https://github.com/expressjs/express) | 593 | 69,375 | JavaScript | Fast, unopinionated, minimalist web framework for node. |
| 100 | [argoproj/argo-cd](https://github.com/argoproj/argo-cd) | 592 | 23,698 | Go | Declarative Continuous Deployment for Kubernetes |

## 给普通人的结论

1. **AI 正在从「聊天」变成「干活」**：视频流水线、会议纪要、招聘筛简历、渗透测试，都在榜上。
2. **开发者最缺的是「省心」**：代码记忆、Agent 编排、免费模型网关、一键克隆网站，本质都是提效。
3. **隐私与本地化仍有市场**：本地会议助手、无账号私密聊天等项目持续吸星。
4. **老牌基建没有消失**：日志库、GUI 库、网络库仍在榜，说明「好用的底层」永远有人用。

---

*本文件由自动化任务根据 GitHub Trending 月榜多语言页面汇总生成，排名按「本月新增 Star」降序。云端无真实 G: 盘，文件保存在仓库 `G盘/AI` 目录。*