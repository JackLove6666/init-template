#!/usr/bin/env python3
"""Generate a plain-language Chinese summary from GitHub monthly top-100 JSON."""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

# Hand-tuned通俗一句话（按仓库全名）；没有命中再用规则兜底
PLAIN_MAP: dict[str, str] = {
    "calesthio/OpenMontage": "把 AI 编程助手变成整套视频制作工作室（多流水线+大量技能包）",
    "MadsLorentzen/ai-job-search": "跑在本机的 AI 求职框架：筛岗位、改简历、写求职信、准备面试",
    "drawdb-io/drawdb": "免费好用的在线数据库绘图与 SQL 生成器",
    "Panniantong/Agent-Reach": "给 AI 装眼睛：读搜 Twitter/Reddit/B站/小红书等，基本不用付 API 费",
    "DeusData/codebase-memory-mcp": "超快代码知识图谱 MCP，让 AI 查代码少烧 Token",
    "Leonxlnx/taste-skill": "教 AI 更有审美，少产出千篇一律的「AI 味」内容",
    "firecrawl/firecrawl": "把任意网页变成干净、结构化数据，方便给 AI 用",
    "asgeirtj/system_prompts_leaks": "汇总各大 AI（Claude/GPT/Gemini/Grok 等）系统提示词泄露内容",
    "usestrix/strix": "开源 AI 渗透测试工具，帮你找应用漏洞",
    "ZhuLinsen/daily_stock_analysis": "LLM 驱动的多市场股票智能分析：行情+新闻+看板+自动推送",
    "iptv-org/iptv": "全球公开 IPTV 直播源合集，想看电视频道的人都在用",
    "stablyai/orca": "同时调度一堆编程 Agent 的桌面/手机 ADE",
    "JCodesMore/ai-website-cloner-template": "一条命令让 AI 编程助手克隆任意网站",
    "Zackriya-Solutions/meetily": "本地隐私优先的 AI 会议助手：实时转写+说话人分离+总结",
    "jamiepine/voicebox": "开源 AI 语音工作室：克隆声音、听写、创作",
    "diegosouzapw/OmniRoute": "免费 AI 网关：一个入口接 200+ 厂商，还能省 Token",
    "ogulcancelik/herdr": "终端里的 Agent 多路复用器，同时盯多个智能体",
    "HKUDS/Vibe-Trading": "属于你自己的个人交易 Agent",
    "OpenCut-app/OpenCut": "开源版剪映（CapCut）替代品",
    "mukul975/Anthropic-Cybersecurity-Skills": "给 AI Agent 用的 800+ 结构化网络安全技能包",
    "topoteretes/cognee": "给 AI Agent 装长期记忆的开源知识图谱平台",
    "NVIDIA/SkillSpector": "扫描 AI Agent 技能包里的漏洞与恶意模式",
    "pbakaus/impeccable": "设计语言规范，让 AI 做设计更靠谱",
    "alibaba/page-agent": "页面内 GUI 智能体：用自然语言操控网页界面",
    "yt-dlp/yt-dlp": "功能很全的命令行音视频下载器",
    "openai/codex-plugin-cc": "在 Claude Code 里调用 Codex：审代码或委派任务",
    "simplex-chat/simplex-chat": "不靠用户 ID 的私密即时通讯网络",
    "openai/codex": "跑在终端里的轻量编程 Agent（OpenAI Codex）",
    "Stirling-Tools/Stirling-PDF": "在线/本地都能用的全能 PDF 编辑神器",
    "GoogleCloudPlatform/knowledge-catalog": "Google Cloud 知识目录相关工具与样例",
    "microsoft/SkillOpt": "用轨迹优化给冻结大模型 Agent「训练」可复用技能",
    "google-research/timesfm": "谷歌的时间序列基础模型，专门做预测",
    "bradautomates/claude-video": "让 Claude 能「看视频」：下载、抽帧、转写一并交给它",
    "lfnovo/open-notebook": "开源 NotebookLM 替代：更灵活的笔记+问答笔记本",
    "koala73/worldmonitor": "全球实时情报看板：AI 聚合新闻与地缘/基建监测",
    "NanmiCoder/MediaCrawler": "小红书/抖音/B站/微博等主流平台媒体爬虫",
    "alibaba/zvec": "轻量高速的进程内向量数据库",
    "kunchenguid/no-mistakes": "减少 git push 出错的小工具/工作流",
    "t8y2/dbx": "约 20MB 的跨平台轻量数据库客户端（多引擎）",
    "mauriceboe/TREK": "可自托管的旅行规划器：协作地图、预算、行李清单",
    "interviewstreet/hiring-agent": "用 AI 自动评估简历、打分的招聘助手",
    "immich-app/immich": "高性能自托管相册：照片视频自己管",
    "makeplane/plane": "开源项目管理：对标 Jira/Linear/ClickUp",
    "TencentCloud/CubeSandbox": "给 AI Agent 用的轻量安全沙箱：即开即跑",
    "tursodatabase/turso": "兼容 SQLite 的进程内 SQL 数据库",
    "tt-a1i/archify": "Agent 技能：一键生成好看的架构图并可导出",
    "ChromeDevTools/chrome-devtools-mcp": "给编程 Agent 用的 Chrome DevTools MCP",
    "n0-computer/iroh": "给应用加上 QUIC + NAT 穿透，用密钥拨号而不是 IP",
    "cjpais/Handy": "完全离线的开源语音转文字应用",
    "googleworkspace/cli": "一条命令行搞定 Drive/Gmail/日历/表格等 Workspace",
    "IceWhaleTech/CasaOS": "简单好看的开源个人云/家庭 NAS 系统",
    "infiniflow/ragflow": "开源 RAG 引擎：检索增强生成+Agent 能力",
    "rommapp/romm": "好看又好用的自托管 ROM 管理与模拟器播放器",
    "kenn-io/agentsview": "本地优先：搜索/分析编程 Agent 会话与 Token 消耗",
    "every-app/open-seo": "开源 SEO 工具，对标 Semrush/Ahrefs",
    "krahets/hello-algo": "动画图解的数据结构与算法教程（多语言）",
    "wonderwhy-er/DesktopCommanderMCP": "给 Claude 装终端/文件/diff 能力的 MCP 服务",
    "rust-lang/rust": "Rust 语言本体：可靠、高效的系统级编程",
    "Tencent/WeKnora": "腾讯开源 LLM 知识平台：文档变 RAG+推理 Agent",
    "kubernetes/kubernetes": "生产级容器编排与集群管理系统",
    "LMCache/LMCache": "给大模型加速的 KV Cache 层",
    "juanfont/headscale": "自托管版 Tailscale 控制面",
    "worldwonderer/oh-story-claudecode": "网文写作全流程 Skill：扫榜、拆文、去 AI 味、封面",
    "Universal-Debloater-Alliance/universal-android-debloater-next-generation": "一键精简安卓预装应用，提升隐私与性能",
    "openai/plugins": "OpenAI 插件相关开源能力",
    "tailscale/tailscale": "最简单好用的 WireGuard 组网（含 2FA）",
    "Kong/insomnia": "开源跨平台 API 客户端（REST/GraphQL/gRPC 等）",
    "BurntSushi/ripgrep": "极速命令行正则搜索，自动尊重 .gitignore",
    "charmbracelet/crush": "好看又好用的终端编程 Agent 体验",
    "google-labs-code/stitch-skills": "配合 Stitch MCP 的 Agent Skills 技能库",
    "THUDM/slime": "面向 RL Scaling 的大模型后训练框架",
    "huggingface/speech-to-speech": "用开源模型搭本地语音对话 Agent",
    "nautechsystems/nautilus_trader": "生产级 Rust 原生量化交易引擎",
    "yorukot/superfile": "好看现代的终端文件管理器",
    "NVIDIA/skills": "NVIDIA 发布的 AI Agent 技能包",
    "denoland/deno": "现代 JavaScript/TypeScript 运行时",
    "kunchenguid/gnhf": "睡前跟 Agents 道晚安：让它们夜间继续干活",
    "cupy/cupy": "GPU 版 NumPy/SciPy，科学计算加速",
    "prometheus/prometheus": "监控与时序数据库领域的事实标准",
    "binwiederhier/ntfy": "用简单 HTTP 给手机/桌面推送通知",
    "junegunn/fzf": "命令行模糊查找神器",
    "openinterpreter/openinterpreter": "面向低成本模型的编程 Agent",
    "elastic/elasticsearch": "开源分布式搜索与分析引擎",
    "rpamis/comet": "把想法变成可评估工作流的 Agent Skill 框架",
    "hashicorp/terraform": "用代码安全、可预期地管理基础设施",
    "ilysenko/codex-desktop-linux": "非官方 Linux 版 ChatGPT/Codex 桌面客户端",
    "ocornut/imgui": "轻量级 C++ 即时模式 GUI 库",
    "Snailclimb/JavaGuide": "Java 面试与后端通关指南（含 AI 应用）",
    "swc-project/swc": "Rust 写的前端编译/打包平台",
    "keycloak/keycloak": "开源身份认证与访问管理（IAM）",
    "yuliskov/SmartTube": "Android TV 上按自己规则看媒体内容",
    "getarcaneapp/arcane": "现代、好上手的 Docker 管理界面",
    "projectdiscovery/nuclei": "基于 YAML 模板的高速漏洞扫描器",
    "skylot/jadx": "Dex 转 Java 的反编译工具",
    "agentscope-ai/agentscope-java": "用 Java 构建分布式、可长期运行的 Agent",
    "ArnasDon/wacrm": "可自托管的 WhatsApp CRM：收件箱、线索、自动化",
    "helix-editor/helix": "后模态风格的现代文本编辑器",
    "fastify/fastify": "Node.js 高性能低开销 Web 框架",
    "wealthfolio/wealthfolio": "本地优先的个人理财与投资追踪",
    "biomejs/biome": "前端工具链：格式化+Lint，Rust 实现",
    "expressjs/express": "经典精简的 Node.js Web 框架",
    "argoproj/argo-cd": "Kubernetes 声明式持续部署（GitOps）",
    "BuilderIO/agent-native": "做「智能体原生」应用的框架，让产品天生会跟 Agent 协作",
    "vercel/next.js": "最主流的 React 全栈框架（Vercel 出品）",
    "golang/go": "Go 语言本体：简单高效的后端/云原生编程语言",
    "kunchenguid/lavish-axi": "把 HTML 当 Markdown 写：面向 HTML 产物的新编辑器",
    "catchorg/Catch2": "现代 C++ 单元测试框架，支持 TDD/BDD",
    "ModernRelay/omnigraph": "湖仓原生图引擎，工作流像用 Git 一样管理",
    "chinese-poetry/chinese-poetry": "超全中华古诗词数据库：唐诗宋词一网打尽",
    "docker/compose": "用一份 YAML 定义并一键跑起多容器应用",
    "agentgateway/agentgateway": "面向 AI Agent 与 MCP 的下一代智能体代理网关",
    "iOfficeAI/OfficeCLI": "专为 AI Agent 读写 Word/Excel/PPT 的开源 Office 套件（免装 Office）",
    "Dicklesworthstone/destructive_command_guard": "拦住 Agent 乱执行危险 git/shell 命令的安全护栏",
    "harvard-edge/cs249r_book": "哈佛边缘计算课《机器学习系统》开源教材",
    "grafana/grafana": "开源可观测性与数据可视化平台（指标/日志/链路）",
    "chenyme/grok2api": "面向 Grok 多端的多账号 API 网关",
    "sharkdp/bat": "带语法高亮的猫命令增强版（cat 替代）",
    "OpenWhispr/openwhispr": "隐私优先的跨平台语音转文字听写应用",
    "bevyengine/bevy": "Rust 写的简洁数据驱动游戏引擎",
    "actions/checkout": "GitHub Actions 里检出仓库代码的官方 Action",
    "cryptomator/cryptomator": "云盘客户端加密工具，文件自己加密再上传",
    "moby/moby": "容器生态协作项目（Docker 引擎相关上游）",
    "Chocobozzz/PeerTube": "去中心化联邦式视频平台（浏览器 P2P）",
    "webtorrent/webtorrent": "网页端流式 BT 客户端",
    "spring-projects/spring-boot": "最省事的 Spring 生产级应用脚手架",
    "JuliusBrussee/caveman": "让 Claude 用「洞穴人」短句说话，少烧约 65% Token",
    "Robbyant/lingbot-map": "前馈 3D 基础模型：从流式数据重建场景",
    "rustdesk/rustdesk": "可自托管的开源远程桌面，对标 TeamViewer",
    "logto-io/logto": "给 SaaS/AI 应用的认证授权底座（OIDC/OAuth、多租户、SSO）",
    "yifanfeng97/Hyper-Extract": "一键把非结构化文本抽成图/超图/时空知识",
    "wezterm/wezterm": "GPU 加速的跨平台终端模拟器与多路复用器",
    "fatedier/frp": "内网穿透反向代理：把家里的服务暴露到公网",
    "gosom/google-maps-scraper": "抓谷歌地图店铺信息：地址电话评分评论等",
    "google-labs-code/design.md": "给编程 Agent 用的视觉品牌说明格式，让设计规范持久可执行",
    "palmier-io/palmier-pro": "专为 AI 打造的 macOS 视频剪辑器",
    "Nutlope/hallmark": "反「AI 味」设计技能：让 Claude/Cursor/Codex 做出更有品位的界面",
    "Shubhamsaboo/awesome-llm-apps": "100+ 可直接跑的 AI Agent / RAG 应用合集：克隆、改改就能上",
    "canopy-network/canopy": "Canopy 网络协议的官方 Go 实现",
    "vxcontrol/pentagi": "全自主 AI 渗透测试系统，能自己完成复杂安全评估任务",
    "HenryNdubuaku/maths-cs-ai-compendium": "想成为顶尖 AI/ML 研究工程师的数学/CS/AI 知识大全",
    "ibelick/ui-skills": "给设计工程师用的 UI 技能包，帮 Agent 做好界面",
    "basketikun/infinite-canvas": "面向 AI 创作的开源无限画布：生图、视频、多 Agent 协同",
    "stanford-oval/storm": "斯坦福开源：用 LLM 调研主题并生成带引用的长报告",
    "iflytek/skillhub": "企业自托管的 Agent 技能注册中心：发布、版本、权限管控",
    "aws/agent-toolkit-for-aws": "AWS 官方 Agent 工具包：MCP/技能/插件，帮智能体在 AWS 上干活",
    "qdrant/qdrant": "高性能大规模向量数据库与向量搜索引擎",
    "FB208/OpenBidKit_Yibiao": "开箱即用的 AI 标书工具：生成、查重、废标项检查，完全开源",
    "stalwartlabs/stalwart": "一体化开源邮件与协作服务器（邮件/日历/联系人）",
    "browser-use/video-use": "让编程 Agent 直接剪辑改视频：用代码方式做视频后期",
    "shadcn-ui/ui": "好看又无障碍的开源 UI 组件库，配代码分发平台，主流前端框架都能用",
    "schollz/croc": "简单安全地在两台电脑之间传文件（端到端加密）",
    "DioxusLabs/dioxus": "用 Rust 写全栈应用：一套代码覆盖 Web/桌面/移动端",
    "AgentWrapper/agent-orchestrator": "管一群编程 Agent 的 IDE：规划任务、开智能体、自动修 CI/冲突/审代码",
}

CATEGORY_RULES: list[tuple[str, list[str]]] = [
    ("AI Agent / 智能体", ["agent", "智能体", "orchestrat", "multiplex", "fleet", "ade for", "vibe-trading", "hiring-agent", "openinterpreter", "crush", "gnhf", "comet", "agentscope", "speech-to-speech", "agent-native", "agentgateway", "omnigraph", "skillhub", "agent-toolkit", "pentagi", "storm", "awesome-llm-apps", "ai-job-search", "job application"]),
    ("知识库 / RAG / 记忆", ["memory", "rag", "knowledge", "记忆", "cognee", "ragflow", "weknora", "open-notebook", "hyper-extract", "compendium"]),
    ("爬虫 / 数据采集", ["scrape", "crawl", "firecrawl", "spider", "采集", "mediacrawler", "yt-dlp", "google-maps-scraper"]),
    ("安全 / 渗透测试", ["secur", "pentest", "vulnerab", "hack", "渗透", "strix", "nuclei", "skillspector", "cybersecurity", "debloat", "pentagi"]),
    ("视频 / 多媒体 / 会议", ["video", "meeting", "iptv", "transcri", "montage", "media", "会议", "直播", "opencut", "voicebox", "romm", "smarttube", "immich", "claude-video", "peertube", "webtorrent", "openwhispr", "bevy", "lingbot-map", "palmier", "video-use"]),
    ("网络 / 通信 / 隐私", ["chat", "privacy", "quic", "nat", "messaging", "iroh", "simplex", "隐私", "tailscale", "headscale", "ntfy", "cryptomator", "rustdesk", "frp", "canopy", "stalwart", "schollz/croc", "croc"]),
    ("数据库 / 存储", ["database", "vector", "storage", "zvec", "sql", "向量库", "turso", "dbx", "elasticsearch", "qdrant"]),
    ("运维 / DevOps / 云", ["devops", "kubernetes", "docker", "cloud", "deploy", "infra", "terraform", "prometheus", "argo", "casaos", "arcane", "keycloak", "compose", "grafana", "moby", "actions/checkout", "logto"]),
    ("金融 / 量化 / 股票", ["stock", "trading", "finance", "quant", "股票", "wealthfolio", "nautilus", "vibe-trading"]),
    ("前端 / Web / UI", ["ui", "frontend", "web", "css", "react", "vue", "imgui", "page-agent", "taste", "impeccable", "fastify", "express", "swc", "biome", "insomnia", "open-seo", "hallmark", "ui-skills", "design.md", "infinite-canvas", "shadcn"]),
    ("移动 / 跨端", ["android", "ios", "mobile", "flutter", "react-native", "跨端", "smarttube", "dioxus"]),
    ("大模型 / LLM 基础设施", ["llm", "prompt", "gateway", "token", "model", "openai", "claude", "gpt", "gemini", "inference", "omniroute", "lmcache", "timesfm", "slime", "skillopt", "system_prompts", "grok2api", "caveman"]),
    ("AI 编程助手 / 开发工具", ["coding", "code", "ide", "copilot", "cursor", "developer", "mcp", "cli", "devtools", "codex", "ripgrep", "fzf", "helix", "deno", "jadx", "archify", "no-mistakes", "desktopcommander", "chrome-devtools", "stitch-skills", "plugins", "officecli", "destructive_command", "sharkdp/bat", "wezterm", "openbidkit", "yibiao", "agent-orchestrator"]),
    ("语言 / 框架 / 基础库", ["library", "framework", "logging", "spdlog", "compiler", "runtime", "rust-lang/rust", "cupy", "hello-algo", "javaguide", "golang/go", "catch2", "next.js", "chinese-poetry", "spring-boot", "cs249r"]),
]


def classify(repo: dict) -> str:
    text = f"{repo.get('full_name', '')} {repo.get('description', '')} {repo.get('language', '')}".lower()
    name = (repo.get("full_name") or "").lower()
    for label, keywords in CATEGORY_RULES:
        if any(k.lower() in text or k.lower() in name for k in keywords):
            return label
    return "其他开源项目"


def plain_summary(repo: dict) -> str:
    full = repo.get("full_name") or ""
    if full in PLAIN_MAP:
        return PLAIN_MAP[full]

    desc = (repo.get("description") or "").strip()
    if not desc:
        return f"{full}：本月热度很高的开源项目"

    # Prefer Chinese portion if present
    cn = re.findall(r"[\u4e00-\u9fff][^A-Za-z]{4,80}", desc)
    if cn:
        return cn[0].strip(" ：:，,。.|")

    clean = re.sub(r"\s+", " ", desc).strip()
    if len(clean) > 72:
        clean = clean[:69] + "..."
    return f"一句话：{clean}"


def wind_sentence(top: list[dict], cats: Counter) -> str:
    top5 = "、".join(f"**{r['full_name'].split('/')[-1]}**" for r in top[:5])
    # Prefer star-weighted themes for the headline
    star_by_cat: Counter = Counter()
    for r in top:
        star_by_cat[r["category"]] += int(r.get("stars_this_month") or 0)
    hot = [name for name, _ in star_by_cat.most_common(3)]
    hot_txt = "、".join(hot) if hot else "、".join(n for n, _ in cats.most_common(3))
    s1 = top[0]["stars_this_month"] if top else 0
    return (
        f"本月 GitHub 最热闹的，几乎都围着 **AI 干活**：{hot_txt}。\n"
        f"榜首前五是 {top5}，"
        f"榜首单月新增约 {s1:,} Star——"
        f"大家在找「能替人干活的 AI 工具」，而不只是看模型本身。"
    )


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    json_path = out_dir / "GitHub本月热榜前100.json"
    data = json.loads(json_path.read_text(encoding="utf-8"))
    repos = data["repos"]
    fetched_at = data.get("fetched_at", "")
    try:
        dt = datetime.fromisoformat(fetched_at.replace("Z", "+00:00"))
        local_label = dt.strftime("%Y-%m-%d %H:%M")
    except Exception:  # noqa: BLE001
        local_label = fetched_at

    classified = []
    cats: Counter = Counter()
    for repo in repos:
        cat = classify(repo)
        cats[cat] += 1
        item = dict(repo)
        item["category"] = cat
        item["plain"] = plain_summary(repo)
        classified.append(item)

    lang_stats: dict[str, list[int]] = {}
    for repo in classified:
        lang = repo.get("language") or "Unknown"
        stars_m = int(repo.get("stars_this_month") or 0)
        if lang not in lang_stats:
            lang_stats[lang] = [0, 0]
        lang_stats[lang][0] += 1
        lang_stats[lang][1] += stars_m
    lang_rows = sorted(lang_stats.items(), key=lambda x: (-x[1][0], -x[1][1]))

    lines: list[str] = []
    lines.append("# GitHub 本月热榜前100 · 通俗总结")
    lines.append("")
    lines.append(
        "> 数据来源：[https://github.com/trending?since=monthly]"
        "(https://github.com/trending?since=monthly)  "
    )
    lines.append(f"> 抓取时间：{local_label}（UTC: {fetched_at}）  ")
    lines.append(
        "> 说明：GitHub 官方月榜单页约20条；本报告按多语言月榜汇总去重后，"
        "按本月新增Star排序取前100。"
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 一句话看懂本月风向")
    lines.append("")
    lines.append(wind_sentence(classified, cats))
    lines.append("")
    lines.append("## 本月热点主题（通俗版）")
    lines.append("")
    tips = {
        "AI Agent / 智能体": "让 AI 自己规划、自己动手，而不是你一句一句喂指令。",
        "AI 编程助手 / 开发工具": "写代码、改代码、管一堆 Agent 一起干活的工具。",
        "大模型 / LLM 基础设施": "提示词、网关、免费模型接入、省 Token 这类「底座」。",
        "其他开源项目": "不好归类、但本月同样很火的项目。",
        "前端 / Web / UI": "网页界面、用自然语言操控页面。",
        "爬虫 / 数据采集": "帮 AI 或人把网页/社交内容抓干净。",
        "网络 / 通信 / 隐私": "更私密的聊天、更稳的网络连接。",
        "安全 / 渗透测试": "用 AI 找漏洞、做安全检测。",
        "视频 / 多媒体 / 会议": "剪视频、开会纪要、语音直播相关。",
        "知识库 / RAG / 记忆": "给 AI 装长期记忆，别聊完就忘。",
        "运维 / DevOps / 云": "部署、云原生相关工具。",
        "数据库 / 存储": "更快的向量库、日志库等基础设施。",
        "移动 / 跨端": "手机端、跨平台应用。",
        "语言 / 框架 / 基础库": "老牌好用的底层库持续被关注。",
        "金融 / 量化 / 股票": "看盘、分析行情的自动化工具。",
    }
    for name, count in cats.most_common():
        tip = tips.get(name, "本月热度较高的开源方向。")
        lines.append(f"- **{name}**（{count} 个）— {tip}")
    lines.append("")
    lines.append("## 语言分布（前100）")
    lines.append("")
    lines.append("| 语言 | 项目数 | 本月新增Star合计 |")
    lines.append("|---|---:|---:|")
    for lang, (count, stars) in lang_rows:
        lines.append(f"| {lang} | {count} | {stars:,} |")
    lines.append("")
    lines.append("## Top 10 速览（本月最火）")
    lines.append("")
    for i, repo in enumerate(classified[:10], 1):
        lines.append(f"### {i}. [{repo['full_name']}]({repo['url']})")
        lines.append("")
        lines.append(
            f"- **本月+{repo['stars_this_month']:,} ★**｜累计 {repo['stars']:,} ★｜"
            f"Fork {repo['forks']:,}｜语言 {repo.get('language') or 'Unknown'}"
        )
        lines.append(f"- **通俗说**：{repo['plain']}")
        desc = repo.get("description") or "（无简介）"
        lines.append(f"- **原简介**：{desc}")
        lines.append(f"- **归类**：{repo['category']}")
        lines.append("")

    lines.append("## 完整前100名单")
    lines.append("")
    lines.append("| 排名 | 仓库 | 本月+★ | 累计★ | 语言 | 通俗一句话 |")
    lines.append("|---:|---|---:|---:|---|---|")
    for i, repo in enumerate(classified, 1):
        plain = repo["plain"].replace("|", "\\|")
        lines.append(
            f"| {i} | [{repo['full_name']}]({repo['url']}) | "
            f"{repo['stars_this_month']:,} | {repo['stars']:,} | "
            f"{repo.get('language') or 'Unknown'} | {plain} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 怎么读这份榜")
    lines.append("")
    lines.append("1. **先看主题**：本月风向比单个仓库名更重要。")
    lines.append("2. **再看本月+★**：比累计 Star 更能反映「最近谁在爆」。")
    lines.append("3. **按语言筛**：想学某门语言，可直接在语言分布里找入口。")
    lines.append("4. **官方页只有约20条**：本文件是多语言月榜拼出来的扩展 Top100。")
    lines.append("")

    date_tag = datetime.now().strftime("%Y%m%d")
    latest = out_dir / "GitHub本月热榜前100通俗总结.md"
    dated = out_dir / f"GitHub本月热榜前100通俗总结_{date_tag}.md"
    text = "\n".join(lines) + "\n"
    for path in (latest, dated):
        path.write_text(text, encoding="utf-8")
        print(f"Wrote {path}")

    missing = [r["full_name"] for r in classified if r["full_name"] not in PLAIN_MAP]
    if missing:
        print("Missing PLAIN_MAP:", ", ".join(missing))


if __name__ == "__main__":
    main()
