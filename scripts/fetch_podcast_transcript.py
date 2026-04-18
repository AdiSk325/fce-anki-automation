#!/usr/bin/env python3
"""
Pobiera transkrypcję odcinka podcastu (Thinking in English / Learning in English)
ze strony www i zapisuje ją do markdown w repo.

Użycie:
    python scripts/fetch_podcast_transcript.py <url>
    python scripts/fetch_podcast_transcript.py <url> --date 2026-04-18
    python scripts/fetch_podcast_transcript.py <url> --output input/podcast-transcripts/custom.md
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = ROOT_DIR / "input" / "podcast-transcripts"


def fetch_html(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; fce-anki-automation/1.0)",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urlopen(request, timeout=30) as response:  # nosec B310
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def strip_html_blocks(raw_html: str) -> str:
    cleaned = re.sub(
        r"<script\b[^>]*>.*?</script\s*>", " ", raw_html, flags=re.IGNORECASE | re.DOTALL
    )
    cleaned = re.sub(
        r"<style\b[^>]*>.*?</style\s*>", " ", cleaned, flags=re.IGNORECASE | re.DOTALL
    )
    cleaned = re.sub(
        r"<noscript\b[^>]*>.*?</noscript\s*>", " ", cleaned, flags=re.IGNORECASE | re.DOTALL
    )
    return cleaned


def extract_article_html(page_html: str) -> str:
    article_match = re.search(r"<article\b[^>]*>(.*?)</article>", page_html, flags=re.IGNORECASE | re.DOTALL)
    return article_match.group(1) if article_match else page_html


def html_to_lines(article_html: str) -> list[str]:
    html_with_breaks = re.sub(r"<\s*br\s*/?>", "\n", article_html, flags=re.IGNORECASE)
    html_with_breaks = re.sub(r"</\s*(p|div|section|article|li|h1|h2|h3|h4|h5|h6|blockquote)\s*>", "\n", html_with_breaks, flags=re.IGNORECASE)

    text = re.sub(r"<[^>]+>", " ", html_with_breaks)
    text = html.unescape(text)

    text = text.replace("\r", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    lines = [line.strip() for line in text.split("\n")]
    return [line for line in lines if line]


def detect_title(page_html: str, fallback_slug: str) -> str:
    h1_match = re.search(r"<h1\b[^>]*>(.*?)</h1>", page_html, flags=re.IGNORECASE | re.DOTALL)
    if h1_match:
        title = re.sub(r"<[^>]+>", " ", h1_match.group(1))
        title = html.unescape(title)
        title = re.sub(r"\s+", " ", title).strip()
        if title:
            return title

    title_match = re.search(r"<title\b[^>]*>(.*?)</title>", page_html, flags=re.IGNORECASE | re.DOTALL)
    if title_match:
        title = html.unescape(re.sub(r"\s+", " ", title_match.group(1))).strip()
        if title:
            return title

    return fallback_slug.replace("-", " ").title()


def find_transcript_lines(lines: list[str]) -> tuple[list[str], str]:
    if not lines:
        return [], "No text lines extracted from article"

    start_idx = None
    transcript_heading_re = re.compile(r"\b(transcript|episode transcript|full transcript|podcast transcript)\b", re.IGNORECASE)

    for idx, line in enumerate(lines):
        if transcript_heading_re.search(line):
            start_idx = idx + 1
            break

    if start_idx is None:
        start_idx = 0
        reason = "Transcript heading not found; using full extracted article text"
    else:
        reason = "Transcript heading found; extracted section after heading"

    stop_patterns = [
        re.compile(r"\b(vocabulary|keywords?|sources?|support this podcast|patreon|newsletter|subscribe|join our)\b", re.IGNORECASE),
        re.compile(r"\b(leave a review|thanks for listening|see you next time)\b", re.IGNORECASE),
    ]

    end_idx = len(lines)
    for idx in range(start_idx, len(lines)):
        line = lines[idx]
        if any(pattern.search(line) for pattern in stop_patterns):
            end_idx = idx
            break

    transcript_lines = lines[start_idx:end_idx]

    if len(transcript_lines) < 3:
        transcript_lines = lines
        reason = "Detected transcript section was too short; using full extracted article text"

    return transcript_lines, reason


def slug_from_url(url: str) -> str:
    path = urlparse(url).path.strip("/")
    if not path:
        return "podcast-episode"
    slug = path.split("/")[-1]
    slug = re.sub(r"[^a-zA-Z0-9-]", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-").lower()
    return slug or "podcast-episode"


def write_transcript_markdown(output_path: Path, *, source_url: str, title: str, extraction_note: str, transcript_lines: list[str]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    numbered_lines = [f"{idx:04d}. {line}" for idx, line in enumerate(transcript_lines, start=1)]

    content = [
        f"# Transcript: {title}",
        "",
        f"- source_url: {source_url}",
        f"- fetched_at: {date.today().isoformat()}",
        f"- extraction_note: {extraction_note}",
        "",
        "## Transcript (numbered lines)",
        "",
        *numbered_lines,
        "",
    ]

    output_path.write_text("\n".join(content), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Pobiera transkrypcję podcastu i zapisuje do markdown")
    parser.add_argument("url", help="URL odcinka z transkrypcją")
    parser.add_argument("--date", dest="file_date", help="Data do nazwy pliku (YYYY-MM-DD), domyślnie dzisiejsza")
    parser.add_argument("--output", help="Docelowa ścieżka pliku markdown (nadpisuje automatyczną nazwę)")

    args = parser.parse_args()

    try:
        page_html = fetch_html(args.url)
    except (HTTPError, URLError, TimeoutError) as exc:
        print(f"❌ Nie udało się pobrać URL: {exc}")
        return 1

    slug = slug_from_url(args.url)
    title = detect_title(page_html, fallback_slug=slug)

    cleaned_html = strip_html_blocks(page_html)
    article_html = extract_article_html(cleaned_html)
    lines = html_to_lines(article_html)
    transcript_lines, extraction_note = find_transcript_lines(lines)

    if not transcript_lines:
        print("❌ Nie udało się wyodrębnić żadnych linii transkrypcji")
        return 1

    if args.output:
        output_path = Path(args.output)
        if not output_path.is_absolute():
            output_path = ROOT_DIR / output_path
    else:
        prefix_date = args.file_date or date.today().isoformat()
        output_path = DEFAULT_OUTPUT_DIR / f"{prefix_date}-{slug}.md"

    write_transcript_markdown(
        output_path,
        source_url=args.url,
        title=title,
        extraction_note=extraction_note,
        transcript_lines=transcript_lines,
    )

    print(f"✅ Zapisano transkrypcję: {output_path}")
    print(f"📄 Liczba linii: {len(transcript_lines)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
