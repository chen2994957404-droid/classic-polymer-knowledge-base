# Task 007: Full Book PDF Safety Plan

## Task Goal

Register the full scanned textbook PDF as a local-only source file and define a safe processing plan before any extraction work begins.

This task does not run OCR, extract text, create page transcripts, or inspect the PDF contents. It records only local file metadata and repository-safety rules.

## Local Source Folder Checked

Source folder:

```text
01_raw_local/source_books/
```

PDF files found:

| Filename | File size |
| --- | ---: |
| `高分子物理（修订版）何曼君.pdf` | 29,387,471 bytes |

## Git Ignore Verification

The PDF is ignored by Git through the repository rule:

```text
.gitignore:184:01_raw_local/
```

This means the full scanned PDF should remain local-only and untracked as long as it stays under `01_raw_local/`.

## Copyright And Repository Safety Rules

- Do not commit raw images or PDFs.
- Do not run OCR yet.
- Do not extract full-book text.
- Do not create full-page transcripts.
- Do not copy textbook text into tracked files.
- Do not create tracked raw OCR files.
- Do not process the entire book at once.
- Do not create final chapter notes directly from raw OCR.

## Safe Processing Strategy

Processing should happen gradually, by chapter and subsection, rather than all at once.

Recommended sequence:

1. Select one small unit, such as one subsection or 1-2 pages.
2. Keep any raw page images under `01_raw_local/`.
3. If OCR is later approved, keep raw OCR output under `01_raw_local/` as local-only material.
4. Convert only manually reviewed structure into tracked workflow notes.
5. Create tracked chapter notes only as non-verbatim study notes.
6. Create tracked Notion-ready summaries only after copyright and accuracy review.

## File Categories

### Local-Only Raw PDF

- Location: `01_raw_local/source_books/`
- Example: `01_raw_local/source_books/高分子物理（修订版）何曼君.pdf`
- Git status: ignored.
- Rule: never commit.

### Local-Only Page Images

- Location: under `01_raw_local/`, such as `01_raw_local/chapter_01_sample/`
- Purpose: small local samples for manual review or future OCR tests.
- Rule: never commit raw scans or extracted page images.

### Local-Only Raw OCR

- Location: under `01_raw_local/`, for example `01_raw_local/source_books/local_ocr_outputs/` or a chapter-specific ignored folder.
- Purpose: temporary local review only.
- Rule: do not commit raw OCR text.

### Tracked Workflow Notes

- Location: `06_codex_tasks/` and `07_review_notes/`
- Purpose: plans, safety checks, uncertainty lists, and review templates.
- Rule: no large copied passages or full-page transcripts.

### Tracked Non-Verbatim Chapter Notes

- Location: `03_chapter_notes/`
- Purpose: concise Chinese study notes based on manually reviewed content.
- Rule: summarize concepts and structure without reproducing textbook text.

### Tracked Notion-Ready Summaries

- Location: `05_notion_ready/`
- Purpose: simplified import-ready study summaries and checklists.
- Rule: keep concise, non-verbatim, and reviewable.

## OCR Tool Requirement

Before any OCR is attempted, confirm a local OCR tool is available and define the exact input pages, output folder, and cleanup process. OCR should start with a very small sample and should never produce tracked full-page raw text.

## Recommended Next Step

Choose one narrow future unit, such as the next manually reviewed subsection, and create only a safe, non-verbatim Chinese study note. If OCR becomes necessary, first document the local OCR command and ensure raw OCR output is written only under `01_raw_local/`.
