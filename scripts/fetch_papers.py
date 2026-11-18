#!/usr/bin/env python3
"""
读取 literature/papers.csv，将公开可获取的论文 PDF 下载到本机 papers/ 目录。
命名规则：<年份>-<安全短名>.pdf
- 已存在且为合法 PDF 的文件自动跳过；
- 标记为“需机构访问”的付费论文跳过并在末尾单独汇总；
- 下载失败的条目记录原因并在末尾汇总，退出码仍为 0（加 --strict 时有失败则返回 1）。
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


def safe_filename(year: str, short_name: str) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*]+', "_", short_name.strip())
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return f"{year.strip()}-{cleaned}.pdf"


def is_valid_pdf(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 1024:
        return False
    with path.open("rb") as f:
        head = f.read(8)
    return head.startswith(b"%PDF")


def download_one(row: dict[str, str], out_dir: Path, timeout: int) -> tuple[str, str, str]:
    short_name = row["短名"].strip()
    year = row["年份"].strip()
    pdf_url = row["PDF"].strip()
    fname = safe_filename(year, short_name)
    dest = out_dir / fname

    if pdf_url == "需机构访问" or not pdf_url.startswith(("http://", "https://")):
        return ("paywalled", fname, f"{short_name} ({year}) — 论文页: {row['论文页']}")

    if is_valid_pdf(dest):
        return ("skipped", fname, f"{dest.stat().st_size / (1024 * 1024):.2f} MiB")

    req = urllib.request.Request(
        pdf_url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/pdf,*/*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
        if not data.startswith(b"%PDF"):
            return ("failed", fname, f"返回内容不是 PDF（前 16 字节: {data[:16]!r}）URL={pdf_url}")
        tmp = dest.with_suffix(".pdf.part")
        tmp.write_bytes(data)
        tmp.replace(dest)
        return ("downloaded", fname, f"{len(data) / (1024 * 1024):.2f} MiB")
    except Exception as exc:
        return ("failed", fname, f"{exc} | URL={pdf_url}")


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="批量下载 literature/papers.csv 中的公开论文 PDF 到 papers/ 目录。")
    parser.add_argument("--csv", type=Path, default=repo_root / "literature" / "papers.csv", help="CSV 清单路径")
    parser.add_argument("--out", type=Path, default=repo_root / "papers", help="本地 PDF 输出目录（已被 .gitignore 忽略）")
    parser.add_argument("--workers", type=int, default=6, help="并发下载线程数（默认 6）")
    parser.add_argument("--timeout", type=int, default=90, help="单篇超时秒数（默认 90）")
    parser.add_argument("--tier", choices=["A", "B", "C", "ALL"], default="ALL", help="只下载指定精读层级（默认 ALL）")
    parser.add_argument("--strict", action="store_true", help="若有下载失败则返回非零退出码")
    args = parser.parse_args()

    if not args.csv.exists():
        print(f"未找到论文清单: {args.csv}", file=sys.stderr)
        return 1

    args.out.mkdir(parents=True, exist_ok=True)
    with args.csv.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    if args.tier != "ALL":
        rows = [r for r in rows if r.get("精读层级", "").strip() == args.tier]

    print(f"共读取 {len(rows)} 条论文记录，输出目录: {args.out}")
    downloaded, skipped, paywalled, failed = [], [], [], []

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futs = {pool.submit(download_one, r, args.out, args.timeout): r for r in rows}
        for fut in as_completed(futs):
            status, fname, detail = fut.result()
            if status == "downloaded":
                downloaded.append((fname, detail))
                print(f"[下载成功] {fname} ({detail})")
            elif status == "skipped":
                skipped.append((fname, detail))
            elif status == "paywalled":
                paywalled.append((fname, detail))
            else:
                failed.append((fname, detail))
                print(f"[下载失败] {fname}: {detail}")

    print("\n================ 汇总 ================")
    print(f"新下载成功 : {len(downloaded)} 篇")
    print(f"已存在跳过 : {len(skipped)} 篇")
    print(f"需机构访问 : {len(paywalled)} 篇")
    print(f"下载失败   : {len(failed)} 篇")

    if paywalled:
        print("\n--- 需机构访问（请项目所有者通过学校/机构权限下载后放入 papers/） ---")
        for _, detail in sorted(paywalled):
            print(f"  - {detail}")

    if failed:
        print("\n--- 下载失败列表 ---")
        for fname, detail in sorted(failed):
            print(f"  - {fname}: {detail}")

    return 1 if (args.strict and failed) else 0


if __name__ == "__main__":
    raise SystemExit(main())
