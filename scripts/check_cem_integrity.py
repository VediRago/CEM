#!/usr/bin/env python3
"""CEM repository integrity checks.

Current checks:
1. Fail on broken internal Markdown links.
2. Warn when an existing Markdown filename is mentioned in prose without being linked.

The unlinked-reference check is intentionally warning-only by default so the
repository can adopt CI without becoming brittle immediately. To make it fail,
run with STRICT_UNLINKED_REFS=1.
"""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
STRICT_UNLINKED_REFS = os.getenv("STRICT_UNLINKED_REFS") == "1"

# Markdown links and images: [label](target) or ![alt](target)
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")


@dataclass(frozen=True)
class Issue:
    path: Path
    line: int
    message: str

    def format(self) -> str:
        rel = self.path.relative_to(ROOT).as_posix()
        return f"{rel}:{self.line}: {self.message}"


def markdown_files() -> list[Path]:
    ignored_dirs = {".git", ".github", "node_modules", "venv", ".venv"}
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if any(part in ignored_dirs for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def strip_code_fences(text: str) -> str:
    return CODE_FENCE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)


def strip_links_and_inline_code(text: str) -> str:
    text = MD_LINK_RE.sub(lambda m: " " * len(m.group(0)), text)
    text = INLINE_CODE_RE.sub(lambda m: " " * len(m.group(0)), text)
    return text


def is_external_link(target: str) -> bool:
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target)) or target.startswith("#")


def normalize_link_target(target: str) -> str:
    target = target.strip()
    target = target.split("#", 1)[0]
    target = target.split("?", 1)[0]
    return unquote(target)


def check_broken_markdown_links(files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []

    for path in files:
        text = path.read_text(encoding="utf-8")
        text_no_fences = strip_code_fences(text)

        for match in MD_LINK_RE.finditer(text_no_fences):
            raw_target = match.group(1).strip()
            if not raw_target or is_external_link(raw_target):
                continue

            target = normalize_link_target(raw_target)
            if not target:
                continue

            # Only validate repository-relative/local links. Non-md assets are also
            # checked, since image/file links should not point nowhere.
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                issues.append(
                    Issue(path, line_number(text_no_fences, match.start()), f"link escapes repository: {raw_target}")
                )
                continue

            if not resolved.exists():
                issues.append(
                    Issue(path, line_number(text_no_fences, match.start()), f"broken link: {raw_target}")
                )

    return issues


def build_filename_index(files: list[Path]) -> dict[str, Path]:
    # Only index unique Markdown basenames. Duplicate basenames can be ambiguous.
    counts: dict[str, int] = {}
    paths: dict[str, Path] = {}
    for path in files:
        counts[path.name] = counts.get(path.name, 0) + 1
        paths[path.name] = path
    return {name: paths[name] for name, count in counts.items() if count == 1}


def check_unlinked_filename_mentions(files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    filename_index = build_filename_index(files)

    if not filename_index:
        return issues

    # Longest first prevents partial overlap oddities.
    names = sorted(filename_index.keys(), key=len, reverse=True)
    pattern = re.compile(r"(?<![\w/.-])(" + "|".join(re.escape(n) for n in names) + r")(?!(?:[\w/.-]))")

    for path in files:
        text = path.read_text(encoding="utf-8")
        searchable = strip_links_and_inline_code(strip_code_fences(text))

        for match in pattern.finditer(searchable):
            filename = match.group(1)
            # Don't warn when the file is mentioning itself in its own title or metadata.
            if filename == path.name:
                continue
            issues.append(
                Issue(
                    path,
                    line_number(searchable, match.start()),
                    f"unlinked filename mention: {filename}",
                )
            )

    return issues


def print_section(title: str, issues: list[Issue]) -> None:
    if not issues:
        print(f"✅ {title}: none")
        return

    print(f"\n{title}:")
    for issue in issues:
        print(f"- {issue.format()}")


def main() -> int:
    files = markdown_files()
    print(f"Checking {len(files)} Markdown files...\n")

    broken_links = check_broken_markdown_links(files)
    unlinked_mentions = check_unlinked_filename_mentions(files)

    print_section("Broken internal links", broken_links)
    print_section("Unlinked Markdown filename mentions", unlinked_mentions)

    failed = False
    if broken_links:
        failed = True
    if STRICT_UNLINKED_REFS and unlinked_mentions:
        failed = True

    if failed:
        print("\n❌ CEM integrity checks failed.")
        if unlinked_mentions and not STRICT_UNLINKED_REFS:
            print("Note: unlinked filename mentions are warnings unless STRICT_UNLINKED_REFS=1.")
        return 1

    print("\n✅ CEM integrity checks passed.")
    if unlinked_mentions and not STRICT_UNLINKED_REFS:
        print("Note: unlinked filename mentions are warnings. Set STRICT_UNLINKED_REFS=1 to fail on them.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
