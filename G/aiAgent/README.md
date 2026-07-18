# G:\aiAgent · GitHub 本月热榜

对应本机目录请求路径：`G:\aiAgent`（云端 Linux 无真实 G 盘，落盘在仓库 `G/aiAgent/`，并镜像到 `G盘/aiAgent/`）。

## 最新文件

- `GitHub本月热榜前100通俗总结.md` — 通俗中文总结（含主题、语言分布、Top10、完整前100）
- `GitHub本月热榜前100.json` — 结构化原始数据
- 带日期后缀的文件为当日快照（如 `*_20260718.*`）

## 刷新方式

```bash
cd G/aiAgent
python3 fetch_github_trending_monthly.py
# 如有 Missing PLAIN_MAP，先补 generate_summary.py 再运行：
python3 generate_summary.py
cp -a . ../../G盘/aiAgent/
```

数据来源：https://github.com/trending?since=monthly  
说明：官方单页约 20 条；脚本按多语言月榜汇总去重后按本月新增 Star 取前 100。
