#!/usr/bin/env python3
"""Fetch GitHub monthly trending across languages, keep top 100 by stars this month."""

from __future__ import annotations

import html
import json
import re
import time
import urllib.request
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path

UA = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}
LANGS = [
    "",
    "python",
    "javascript",
    "typescript",
    "go",
    "rust",
    "java",
    "c++",
    "c",
    "c%23",
    "php",
    "ruby",
    "swift",
    "kotlin",
    "dart",
    "shell",
    "html",
    "vue",
    "jupyter-notebook",
    "lua",
    "scala",
    "haskell",
    "zig",
    "elixir",
    "powershell",
]


def fetch(url: str, retries: int = 3) -> str | None:
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=45) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except Exception as exc:  # noqa: BLE001
            print(f"  retry {i + 1}: {exc}")
            time.sleep(2 * (i + 1))
    return None


def parse_int(value: str) -> int:
    if not value:
        return 0
    value = value.strip().replace(",", "").replace(" ", "")
    match = re.search(r"([\d.]+)([kKmM]?)", value)
    if not match:
        return 0
    number = float(match.group(1))
    suffix = match.group(2).lower()
    if suffix == "k":
        number *= 1000
    elif suffix == "m":
        number *= 1_000_000
    return int(number)


def parse_page(content: str, lang_label: str) -> list[dict]:
    articles = re.findall(r'<article class="Box-row".*?</article>', content, re.S)
    repos: list[dict] = []
    for article in articles:
        heading = re.search(r"<h2[\s\S]*?</h2>", article)
        if not heading:
            continue
        href = re.search(r'href="(/[^/]+/[^/"?#]+)"', heading.group(0))
        if not href:
            continue
        path = href.group(1)
        owner, name = path.strip("/").split("/", 1)
        owner = html.unescape(owner).strip()
        name = html.unescape(name).strip()

        desc_match = re.search(r'<p class="col-9[^"]*"[^>]*>(.*?)</p>', article, re.S)
        description = ""
        if desc_match:
            description = re.sub(r"<[^>]+>", "", desc_match.group(1))
            description = html.unescape(re.sub(r"\s+", " ", description)).strip()

        lang_match = re.search(r'itemprop="programmingLanguage"[^>]*>([^<]+)', article)
        language = lang_match.group(1).strip() if lang_match else (lang_label or "Unknown")

        stars_match = re.search(r'/stargazers"[\s\S]*?</svg>\s*([\d,\.]+)', article)
        forks_match = re.search(r'/forks"[\s\S]*?</svg>\s*([\d,\.]+)', article)
        monthly_match = re.search(r"([\d,\.]+)\s+stars?\s+this\s+month", article, re.I)

        repos.append(
            {
                "full_name": f"{owner}/{name}",
                "url": f"https://github.com{path}",
                "description": description,
                "language": language,
                "stars": parse_int(stars_match.group(1) if stars_match else "0"),
                "forks": parse_int(forks_match.group(1) if forks_match else "0"),
                "stars_this_month": parse_int(
                    monthly_match.group(1) if monthly_match else "0"
                ),
                "source_lang_filter": lang_label or "all",
            }
        )
    return repos


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    collected: OrderedDict[str, dict] = OrderedDict()

    for lang in LANGS:
        if lang:
            url = f"https://github.com/trending/{lang}?since=monthly"
            label = urllib.request.unquote(lang)
        else:
            url = "https://github.com/trending?since=monthly"
            label = "all"

        print(f"Fetching {label} ...", flush=True)
        content = fetch(url)
        if not content:
            continue

        for repo in parse_page(content, label if label != "all" else ""):
            key = repo["full_name"].lower()
            if key not in collected:
                collected[key] = repo
            else:
                current = collected[key]
                if repo["stars_this_month"] > current["stars_this_month"]:
                    collected[key] = repo
                elif repo["stars"] > current["stars"]:
                    current["stars"] = repo["stars"]
                    current["forks"] = max(current["forks"], repo["forks"])

        print(f"  unique={len(collected)}")
        time.sleep(0.5)
        if len(collected) >= 120:
            break

    top = sorted(
        collected.values(),
        key=lambda item: (-item["stars_this_month"], -item["stars"]),
    )[:100]
    payload = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "source": "https://github.com/trending?since=monthly",
        "note": (
            "GitHub 官方月榜单页约20条；本脚本按多语言月榜汇总去重后，"
            "按本月新增Star排序取前100。"
        ),
        "count": len(top),
        "repos": top,
    }

    date_tag = datetime.now().strftime("%Y%m%d")
    json_latest = out_dir / "GitHub本月热榜前100.json"
    json_dated = out_dir / f"GitHub本月热榜前100_{date_tag}.json"
    for path in (json_latest, json_dated):
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
