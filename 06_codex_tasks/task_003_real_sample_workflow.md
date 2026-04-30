# Task 003: Real Sample Workflow

## Task Goal

Define a cautious workflow for testing the local OCR cleanup process on a very small real textbook sample.

This task is documentation only. It does not run OCR, process images, transcribe textbook text, or create final chapter notes.

## Why Raw Textbook Images Stay In `01_raw_local/`

Raw textbook images and PDFs are source materials for local review only. They should remain under `01_raw_local/` because that folder is ignored by Git and is intended for untracked local-only files.

Keeping raw files there prevents accidental commits of copyrighted source images and keeps the repository focused on workflow notes, short review artifacts, and cleaned outputs that are safe to track.

## Copyright And Repository Safety Rules

- Use only a very small sample for workflow testing.
- Do not commit raw textbook images or PDFs.
- Do not copy large amounts of textbook text into tracked files.
- Keep any future transcript short and limited to the minimum needed to test the workflow.
- Mark uncertain OCR items for ChatGPT review rather than rewriting academic content automatically.
- Preserve formulas and line order during engineering cleanup.
- Keep final academic reconstruction separate from this preprocessing task.

## Current Raw Sample Folder

The current local raw sample folder is:

```text
01_raw_local/chapter_01_sample/
```

Known local sample files:

```text
01_raw_localchapter_01_samplepage_001.png
01_raw_localchapter_01_samplepage_002.png
01_raw_localchapter_01_samplepage_003.png
01_raw_localchapter_01_samplepage_004.png
01_raw_localchapter_01_samplepage_005.png
01_raw_localchapter_01_samplepage_006.png
01_raw_localchapter_01_samplepage_007.png
```

These files are ignored by Git through the `01_raw_local/` rule.

## Why Process Only 1-2 Pages First

Processing only one or two pages first keeps the copyright footprint small and makes the workflow easy to inspect. It also helps verify OCR extraction, conservative cleanup, formula protection, and review-note structure before any larger local-only work is considered.

The first pass should use only `page_001.png` and `page_002.png`, or a manually prepared short transcript derived from those pages.

## Allowed Future Outputs

Future work for this task may create or update:

- `02_ocr_output/chapter_01_sample_manual_transcript.md`
- `02_ocr_output/chapter_01_sample_cleaned.md`
- `07_review_notes/task_003_real_sample_uncertain_items.md`
- `07_review_notes/task_003_for_chatgpt_review.md`

## Forbidden Actions

- Do not commit raw images or PDFs.
- Do not create full-book OCR outputs.
- Do not copy large amounts of textbook text into tracked files.
- Do not rewrite academic content without ChatGPT review.
- Do not modify final chapter notes yet.

## Recommended Next Minimal Step

Process only `page_001.png` and `page_002.png`, or create a manually prepared short transcript from those pages, then run the conservative OCR cleanup script on that small tracked transcript. After cleanup, record uncertain tokens, formulas, figure/table references, and copyright-risk notes for ChatGPT review.
