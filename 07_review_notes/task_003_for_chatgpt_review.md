# Task 003 ChatGPT Review Template

## Task Summary

Task 003 documents a cautious workflow for testing the OCR cleanup pipeline on a very small real textbook sample stored locally. No OCR, image processing, or textbook transcription has been performed yet.

## Raw Local Files Checked

Raw folder exists:

```text
01_raw_local/chapter_01_sample/
```

Known files in the raw local sample folder:

```text
01_raw_localchapter_01_samplepage_001.png
01_raw_localchapter_01_samplepage_002.png
01_raw_localchapter_01_samplepage_003.png
01_raw_localchapter_01_samplepage_004.png
01_raw_localchapter_01_samplepage_005.png
01_raw_localchapter_01_samplepage_006.png
01_raw_localchapter_01_samplepage_007.png
```

## Git Ignore Safety

The raw sample images are ignored by Git through the `01_raw_local/` ignore rule. No raw images should be committed.

## Files Created Or Modified

Documentation files for this task:

- `06_codex_tasks/task_003_real_sample_workflow.md`
- `07_review_notes/task_003_for_chatgpt_review.md`

No raw image files were modified.

## Commands Run

Local inspection commands were run to confirm:

- `01_raw_local/chapter_01_sample/` exists.
- The folder contains seven `.png` sample image files.
- Git ignore rules cover the raw sample folder and its contents.
- The repository had no visible changes before creating Task 003 documentation.

No OCR command was run.

## OCR/Text Extraction Status

No OCR has been run yet. No text extraction has been performed yet. No textbook text has been copied into tracked files.

## Copyright Risk Check

Current risk is low because this step created documentation only and did not include textbook content. Future tracked outputs should remain very small, should avoid large copied passages, and should exist only to test the local workflow.

Raw images must remain local under `01_raw_local/` and must not be committed.

## Items Requiring ChatGPT Review

When a small transcript or cleaned sample is eventually created, ChatGPT should review:

- Whether the sample size is minimal enough for workflow testing.
- Whether uncertain OCR tokens are marked and not deleted.
- Whether formula blocks are preserved without correction or rewriting.
- Whether figure/table references are represented only as minimal review notes.
- Whether no large copyrighted passage has been copied into tracked files.

## Recommended Next Step

Process only `page_001.png` and `page_002.png`, or use a manually prepared short transcript from those pages. Then run the conservative cleanup workflow on that tiny sample and create a focused uncertain-items review note.

## Commit/Push Status

No commit has been made. No push has been made.
