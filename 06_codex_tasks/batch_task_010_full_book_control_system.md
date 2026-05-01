# Batch Task 010: Full Book Control System

## Batch Task Goal

Create the tracked control-system files for staged full-book processing of the scanned polymer physics textbook project.

This task fixes the previous incomplete execution by moving the reusable batch review template from `07_review_notes/_BATCH_REVIEW_TEMPLATE.md` to `00_admin/BATCH_REVIEW_TEMPLATE.md`, deleting the misplaced file, and completing all required workflow, queue, template, index, task, and review documents.

## Allowed Files

This task may create or modify:

- `00_admin/FULL_BOOK_WORKFLOW.md`
- `00_admin/FULL_BOOK_PROCESSING_QUEUE.md`
- `00_admin/BATCH_REVIEW_TEMPLATE.md`
- `00_admin/CHAPTER_NOTE_TEMPLATE.md`
- `00_admin/CODEX_BATCH_WORKFLOW.md`
- `03_chapter_notes/chapter_01_processing_index.md`
- `05_notion_ready/chapter_01_processing_index_notion.md`
- `06_codex_tasks/batch_task_010_full_book_control_system.md`
- `07_review_notes/batch_task_010_for_chatgpt_review.md`

This task may delete:

- `07_review_notes/_BATCH_REVIEW_TEMPLATE.md`

## Forbidden Actions

- Do not browse the web.
- Do not touch `01_raw_local/`.
- Do not run OCR.
- Do not extract PDF text.
- Do not process raw images.
- Do not create full-book transcripts.
- Do not copy large textbook passages into tracked files.
- Do not commit.
- Do not push.

## Source Context

The project is a Chinese, non-verbatim polymer physics knowledge-base workflow built from a scanned textbook PDF kept locally. Existing tasks established OCR cleanup, simulated workflow testing, real sample safety checks, OCR capability status, manual Chapter 1 structure extraction, subsection 1.1.1 notes, and full-PDF safety registration.

OCR capability is currently limited: no Tesseract, pytesseract, easyocr, or paddleocr are available; PIL is available.

## Outputs Created

- Full-book workflow document.
- Full-book processing queue.
- Batch review template under `00_admin/`.
- Chapter note template.
- Codex batch workflow guide.
- Chapter 1 processing index.
- Chapter 1 Notion-ready processing index.
- Batch task documentation.
- ChatGPT review note.

## Completion Criteria

This task is complete when:

1. All required files exist at the correct paths.
2. The misplaced `07_review_notes/_BATCH_REVIEW_TEMPLATE.md` file is removed if it exists.
3. No raw files under `01_raw_local/` are modified.
4. No OCR, PDF extraction, or raw image processing is performed.
5. `git status --short` and `git diff --check` have been run.
6. The final response reports exact file changes and ChatGPT review needs.
