#!/usr/bin/env python3
"""Conservative OCR Markdown cleanup.

This script performs engineering preprocessing only. It does not rewrite,
summarize, correct, or complete academic content.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


UNCERTAINTY_PATTERNS = (
    (re.compile(r"[\ufffd\u25a1\u25a0\u25cf\u25cb]"), "replacement or placeholder character"),
    (re.compile(r"\b(?:l|I|O|0){4,}\b"), "repeated ambiguous OCR characters"),
    (re.compile(r"[A-Za-z]{2,}\d[A-Za-z]{2,}"), "digit embedded in word"),
    (re.compile(r"\b\w*[{}]\w*\b"), "unexpected brace inside token"),
    (re.compile(r"\s+[.,;:]\s*"), "space before punctuation"),
    (re.compile(r"[|]{2,}"), "repeated vertical bars"),
    (re.compile(r"[_~^]{3,}"), "repeated OCR-like symbols"),
)


@dataclass
class CleaningStats:
    input_lines: int = 0
    output_lines_before_report: int = 0
    trailing_space_lines: int = 0
    collapsed_blank_lines: int = 0
    uncertain_lines: int = 0
    formula_or_code_block_lines: int = 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Clean OCR Markdown conservatively without rewriting content."
    )
    parser.add_argument("input_path", help="Input UTF-8 Markdown or text file")
    parser.add_argument("output_path", help="Output UTF-8 Markdown file")
    return parser.parse_args()


def is_fence_toggle(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("```") or stripped.startswith("~~~")


def is_single_line_dollar_formula(line: str) -> bool:
    stripped = line.strip()
    return (
        stripped.startswith("$$")
        and stripped.endswith("$$")
        and stripped != "$$"
        and stripped.count("$$") >= 2
    )


def is_dollar_formula_toggle(line: str) -> bool:
    # Treat a line with an unpaired $$ marker as a block boundary.
    return not is_single_line_dollar_formula(line) and line.count("$$") % 2 == 1


def is_bracket_formula_start(line: str) -> bool:
    return line.strip() == r"\["


def is_bracket_formula_end(line: str) -> bool:
    return line.strip() == r"\]"


def is_protected_line(
    line: str,
    in_fenced_block: bool,
    in_dollar_formula: bool,
    in_bracket_formula: bool,
) -> bool:
    return (
        in_fenced_block
        or in_dollar_formula
        or in_bracket_formula
        or is_fence_toggle(line)
        or is_single_line_dollar_formula(line)
        or is_dollar_formula_toggle(line)
        or is_bracket_formula_start(line)
        or is_bracket_formula_end(line)
    )


def update_protected_state(
    line: str,
    in_fenced_block: bool,
    in_dollar_formula: bool,
    in_bracket_formula: bool,
) -> tuple[bool, bool, bool]:
    if is_fence_toggle(line):
        return not in_fenced_block, in_dollar_formula, in_bracket_formula

    if in_fenced_block:
        return in_fenced_block, in_dollar_formula, in_bracket_formula

    if in_dollar_formula:
        if is_dollar_formula_toggle(line):
            in_dollar_formula = False
        return in_fenced_block, in_dollar_formula, in_bracket_formula

    if is_single_line_dollar_formula(line):
        return in_fenced_block, in_dollar_formula, in_bracket_formula

    if is_dollar_formula_toggle(line):
        return in_fenced_block, True, in_bracket_formula

    if in_bracket_formula:
        if is_bracket_formula_end(line):
            in_bracket_formula = False
        return in_fenced_block, in_dollar_formula, in_bracket_formula

    if is_bracket_formula_start(line):
        in_bracket_formula = True

    return in_fenced_block, in_dollar_formula, in_bracket_formula


def uncertainty_reason(line: str) -> str | None:
    stripped = line.strip()
    if not stripped:
        return None

    # Headings are preserved and not marked just for containing numbering.
    if stripped.startswith("#"):
        return None

    for pattern, reason in UNCERTAINTY_PATTERNS:
        if pattern.search(line):
            return reason

    # Very high punctuation density is often an OCR artifact in prose lines.
    non_space_chars = [char for char in line if not char.isspace()]
    punctuation_chars = [char for char in non_space_chars if not char.isalnum()]
    if len(non_space_chars) >= 20 and len(punctuation_chars) / len(non_space_chars) > 0.45:
        return "high punctuation density"

    return None


def clean_lines(lines: list[str]) -> tuple[list[str], CleaningStats]:
    stats = CleaningStats(input_lines=len(lines))
    output: list[str] = []
    blank_run = 0
    in_fenced_block = False
    in_dollar_formula = False
    in_bracket_formula = False

    for raw_line in lines:
        line = raw_line.rstrip("\n\r")
        stripped_trailing = line.rstrip()
        if stripped_trailing != line:
            stats.trailing_space_lines += 1
        line = stripped_trailing

        in_protected_block = is_protected_line(
            line,
            in_fenced_block,
            in_dollar_formula,
            in_bracket_formula,
        )

        if in_protected_block:
            blank_run = 0
            stats.formula_or_code_block_lines += 1
            output.append(line)
            in_fenced_block, in_dollar_formula, in_bracket_formula = update_protected_state(
                line,
                in_fenced_block,
                in_dollar_formula,
                in_bracket_formula,
            )
            continue

        if line.strip() == "":
            blank_run += 1
            if blank_run <= 2:
                output.append("")
            else:
                stats.collapsed_blank_lines += 1
            continue

        blank_run = 0

        reason = uncertainty_reason(line)
        if reason:
            output.append(f"<!-- OCR-UNCERTAIN: {reason} -->")
            stats.uncertain_lines += 1
        output.append(line)

    stats.output_lines_before_report = len(output)
    return output, stats


def build_report(stats: CleaningStats) -> list[str]:
    return [
        "",
        "",
        "---",
        "",
        "## OCR Cleaning Report",
        "",
        "- Script: `scripts/clean_ocr_markdown.py`",
        "- Processing type: conservative engineering cleanup only",
        f"- Input lines: {stats.input_lines}",
        f"- Output lines before report: {stats.output_lines_before_report}",
        f"- Lines with trailing spaces stripped: {stats.trailing_space_lines}",
        f"- Excess blank lines collapsed: {stats.collapsed_blank_lines}",
        f"- Lines marked as OCR uncertain: {stats.uncertain_lines}",
        f"- Protected formula/code block lines preserved: {stats.formula_or_code_block_lines}",
        "",
        "Review note: uncertain lines were marked for human review and were not deleted.",
    ]


def main() -> int:
    args = parse_args()
    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    text = input_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    cleaned_lines, stats = clean_lines(lines)
    final_lines = cleaned_lines + build_report(stats)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(final_lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
