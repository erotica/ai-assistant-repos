#!/usr/bin/env python3
"""GitHub에서 '개인 AI 비서' 관련 저장소를 수집해 Markdown/JSON으로 저장한다.

사용:
    python3 scripts/collect_repos.py [--out docs] [--limit 20]

인증 없이 실행 가능(검색 API는 분당 10회 제한)이라 쿼리 사이에 대기한다.
GITHUB_TOKEN 환경변수가 있으면 그 토큰을 사용한다(제한 상향).
"""
from __future__ import annotations

import argparse
import json
import os
import time
import urllib.parse
import urllib.request

QUERIES = [
    '"personal AI assistant" in:description',
    "topic:personal-agent",
    "topic:ai-assistant stars:>1500",
    '"computer use" agent in:description stars:>500',
    "topic:computer-use",
    '"self-hosted" "AI assistant" in:description stars:>300',
    "muse ai assistant in:name,description stars:>50",
    "pickle ai assistant in:name,description",
    "org:facebookresearch agent",
]


def search(query: str, limit: int = 20) -> dict:
    url = (
        "https://api.github.com/search/repositories?q="
        + urllib.parse.quote(query)
        + f"&sort=stars&order=desc&per_page={limit}"
    )
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "ai-assistant-repos-collector"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=40) as resp:
        return json.load(resp)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="docs")
    ap.add_argument("--limit", type=int, default=20)
    args = ap.parse_args()

    seen: dict[str, dict] = {}
    for q in QUERIES:
        try:
            data = search(q, args.limit)
        except Exception as exc:  # rate limit 등
            print(f"[skip] {q}: {exc}")
            time.sleep(20)
            continue
        print(f"[ok] {q} total={data.get('total_count')}")
        for it in data.get("items", []):
            seen[it["full_name"]] = {
                "name": it["full_name"],
                "stars": it["stargazers_count"],
                "desc": (it.get("description") or "")[:170],
                "lang": it.get("language"),
                "pushed": (it.get("pushed_at") or "")[:10],
                "url": it["html_url"],
                "topics": it.get("topics", [])[:8],
            }
        time.sleep(7)

    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "repos.json"), "w", encoding="utf-8") as fh:
        json.dump(seen, fh, ensure_ascii=False, indent=1)

    rows = ["# 수집 결과", "", "| # | 저장소 | ★ | 언어 | 최근 푸시 | 설명 |", "|---:|---|---:|---|---|---|"]
    for i, v in enumerate(sorted(seen.values(), key=lambda x: -x["stars"]), 1):
        rows.append(f"| {i} | [{v['name']}]({v['url']}) | {v['stars']:,} | {v['lang']} | {v['pushed']} | {v['desc'].replace('|', chr(92)+'|')[:130]} |")
    with open(os.path.join(args.out, "collected.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(rows) + "\n")
    print(f"collected {len(seen)} repos -> {args.out}/")


if __name__ == "__main__":
    main()
