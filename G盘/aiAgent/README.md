# G:\aiAgent — GitHub 本月热榜通俗总结

对应本机目录：`G:\aiAgent`

## 文件说明

| 文件 | 说明 |
|---|---|
| `GitHub本月热榜前100通俗总结.md` | 中文通俗总结（最新） |
| `GitHub本月热榜前100.json` | 结构化原始数据（最新） |
| `*_YYYYMMDD.*` | 按日期存档 |
| `fetch_github_trending_monthly.py` | 多语言月榜爬取脚本 |
| `generate_summary.py` | 生成通俗总结 |

## 数据来源

- 官网：https://github.com/trending?since=monthly
- 说明：官方页约 20 条；本目录按多语言月榜去重后按「本月新增 Star」取前 100

## 刷新

```bash
python3 fetch_github_trending_monthly.py
python3 generate_summary.py
```

## 最近刷新

- 2026-08-03：多语言月榜汇总 138 → Top100；榜首 OmniRoute（+27721）；前五 graphify / orca / OpenCut / skills；新增 PLAIN_MAP：blader/humanizer、MoonshotAI/kimi-cli、NomaDamas/k-skill、saadeghi/daisyui
- 2026-08-02：多语言月榜汇总 139 → Top100；榜首 OmniRoute（+27829）；前五 graphify / orca / OpenCut / skills；新增 PLAIN_MAP：Emily2040/seedance-2.0、rustfs/rustfs、dottxt-ai/outlines
- 2026-08-01：多语言月榜汇总 140 → Top100；榜首 OmniRoute（+27829）；前五 graphify / orca / OpenCut / skills
- 2026-07-30：多语言月榜汇总 134 → Top100；榜首 OmniRoute；前五 graphify / orca / OpenCut / strix
- 2026-07-28：多语言月榜汇总 134 → Top100；榜首 OmniRoute（+24936）；前五含 graphify / orca / codebase-memory-mcp / OpenCut；新增 PLAIN_MAP：earendil-works/pi、kyutai-labs/pocket-tts、nodejs/node、pocketbase/pocketbase、jenkinsci/jenkins
- 2026-07-27：多语言月榜汇总 135 → Top100；榜首 graphify；前五含 OmniRoute / orca / codebase-memory-mcp / OpenMontage
- 2026-07-26：多语言月榜汇总 133 → Top100；榜首 graphify；前五含 OmniRoute / orca / codebase-memory-mcp / OpenMontage
