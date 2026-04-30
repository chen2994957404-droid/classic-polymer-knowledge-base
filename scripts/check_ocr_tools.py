#!/usr/bin/env python3
"""Report local OCR capability without performing OCR."""

from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "01_raw_local" / "chapter_01_sample"
SAMPLE_FILES = [
    RAW_DIR / "page_001.png",
    RAW_DIR / "page_002.png",
]
PACKAGE_NAMES = ("PIL", "pytesseract", "easyocr", "paddleocr")


def relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def package_status(name: str) -> str:
    return "available" if importlib.util.find_spec(name) is not None else "missing"


def git_check_ignore(path: Path) -> tuple[str, str]:
    git = shutil.which("git")
    if git is None:
        return "unknown", "git not found in PATH"

    rel_path = relative(path)
    try:
        result = subprocess.run(
            [git, "check-ignore", "-v", "--", rel_path],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as exc:
        return "unknown", f"git check-ignore failed: {exc}"

    detail = (result.stdout or result.stderr).strip()
    if result.returncode == 0:
        return "ignored", detail
    if result.returncode == 1:
        return "not ignored", "no matching ignore rule"
    return "unknown", detail or f"git check-ignore returned {result.returncode}"


def main() -> int:
    print("OCR Capability Report")
    print("=====================")
    print(f"Repository root: {ROOT}")
    print(f"Python version: {sys.version.split()[0]}")
    print()

    tesseract_path = shutil.which("tesseract")
    print("Command-line OCR tools:")
    if tesseract_path:
        print(f"- tesseract: available at {tesseract_path}")
    else:
        print("- tesseract: missing from PATH")
    print()

    print("Python OCR-related packages:")
    for package_name in PACKAGE_NAMES:
        print(f"- {package_name}: {package_status(package_name)}")
    print()

    print("Expected sample image files:")
    for sample_file in SAMPLE_FILES:
        status = "found" if sample_file.is_file() else "missing"
        print(f"- {relative(sample_file)}: {status}")
    print()

    print("Raw sample folder:")
    folder_status = "found" if RAW_DIR.is_dir() else "missing"
    print(f"- {relative(RAW_DIR)}: {folder_status}")
    if RAW_DIR.is_dir():
        png_files = sorted(path.name for path in RAW_DIR.glob("*.png"))
        if png_files:
            print("- PNG files currently present:")
            for name in png_files:
                print(f"  - {name}")
        else:
            print("- PNG files currently present: none")
    print()

    print("Git ignore checks:")
    paths_to_check = [ROOT / "01_raw_local", RAW_DIR, *SAMPLE_FILES]
    for path in paths_to_check:
        status, detail = git_check_ignore(path)
        print(f"- {relative(path)}: {status}")
        if detail:
            print(f"  {detail}")
    print()

    print("OCR performed: no")
    print("This script only checks local capability and repository safety.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
