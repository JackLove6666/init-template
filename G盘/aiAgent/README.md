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

- 2026-07-21：多语言月榜汇总 133 → Top100；榜首 OpenMontage
