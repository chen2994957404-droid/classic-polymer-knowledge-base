# Task 004: Check OCR Capability

## Task Goal

Check local OCR capability and plan the smallest safe processing step for the first two local sample pages.

This task is limited to environment inspection and workflow planning. It must not run OCR, process image contents, copy textbook text, or create final chapter notes.

## Raw Local Sample Location

Raw sample images are stored locally under:

```text
01_raw_local/chapter_01_sample/
```

The intended minimal test pages are:

```text
01_raw_local/chapter_01_sample/page_001.png
01_raw_local/chapter_01_sample/page_002.png
```

If those exact filenames are not present, pause and reconcile the local filenames before running any OCR.

## Why Raw OCR Should Remain Local-Only

Raw OCR text from textbook images may contain substantial copyrighted text. If raw OCR is generated, it must stay under:

```text
01_raw_local/chapter_01_sample/local_ocr_outputs/
```

That location is ignored by Git because it is inside `01_raw_local/`. Keeping raw OCR local-only prevents accidental commits of raw textbook-derived text.

## Allowed Tracked Outputs

Tracked files should contain only workflow notes, short review metadata, uncertainty lists, and non-verbatim summaries.

Allowed tracked outputs for this task are:

- `06_codex_tasks/task_004_check_ocr_capability.md`
- `07_review_notes/task_004_for_chatgpt_review.md`
- `scripts/check_ocr_tools.py`

## Forbidden Actions

- Do not commit raw images or PDFs.
- Do not create full-page verbatim OCR outputs in tracked files.
- Do not create full-book OCR outputs.
- Do not copy large amounts of textbook text into tracked files.
- Do not rewrite academic content yet.
- Do not create or modify final chapter notes yet.
- Do not run OCR during this task.
- Do not commit or push.

## How OCR Capability Will Be Checked

Run the standard-library-only capability checker:

```bash
python scripts/check_ocr_tools.py
```

The checker reports:

- Python version.
- Whether `tesseract` is available in `PATH`.
- Whether common OCR-related Python packages are importable: `PIL`, `pytesseract`, `easyocr`, and `paddleocr`.
- Whether the expected local sample files exist.
- Whether the raw sample folder and expected sample paths are ignored by Git.

The checker does not perform OCR.

## Recommended Next Step

If OCR tools are available and the expected sample paths exist, process only `page_001.png` and `page_002.png`, placing any raw OCR output under `01_raw_local/chapter_01_sample/local_ocr_outputs/`.

If OCR tools are missing or the expected sample paths do not exist, do not run OCR. First install or select a local OCR method, or prepare a very short manual transcript for only the first one or two pages. Any tracked follow-up should contain only short review metadata and uncertainty notes, not full-page verbatim textbook OCR.
