# Task 005: Manual Structure Extraction

## Task Goal

Create a safe, non-verbatim structural sample from the first two real local sample images using only manually reviewed information.

This task tests whether the project can turn a very small source sample into Chinese study-note style knowledge-base entries without running OCR, copying full-page text, or creating final chapter notes.

## Revision Note

The first generated version used English for the knowledge notes. This revision converts the knowledge-note files and Notion-ready files into Chinese while keeping them non-verbatim and limited to the manually reviewed structure.

## Source Scope

Use only the manually reviewed structure from:

- `01_raw_local/chapter_01_sample/page_001.png`
- `01_raw_local/chapter_01_sample/page_002.png`

The raw images remain local under `01_raw_local/`, which is ignored by Git. They must not be committed.

## Copyright And Safety Rules

- Do not run OCR.
- Do not process all seven images.
- Do not create verbatim full-page transcripts.
- Do not copy the full preface text into tracked files.
- Do not create final chapter notes yet.
- Do not rewrite or reconstruct academic content beyond the manually reviewed structure.
- Keep tracked outputs limited to Chinese study notes, outlines, review metadata, and non-verbatim Notion-ready structure.

## Allowed Outputs For This Task

- `03_chapter_notes/chapter_00_preface_positioning.md`
- `03_chapter_notes/chapter_01_structure_outline.md`
- `05_notion_ready/chapter_00_preface_positioning_notion.md`
- `05_notion_ready/chapter_01_structure_outline_notion.md`
- `07_review_notes/task_005_for_chatgpt_review.md`

## Workflow Steps

1. Use the manually reviewed preface points from page 001.
2. Summarize the preface in Chinese without transcribing it.
3. Use the manually reviewed table-of-contents structure from page 002.
4. Build a Chinese Chapter 1 outline with section hierarchy, learning objectives, key concepts, and expected formulas or models to watch for later.
5. Create simplified Chinese Notion-ready versions of both notes.
6. Record copyright handling, source scope, and review needs in the Task 005 review note.

## Completion Criteria

This task is complete when:

1. The preface is represented only as a structured, non-verbatim Chinese positioning summary.
2. Chapter 1 is represented as a clean Chinese structural outline rather than a full content reconstruction.
3. Notion-ready Chinese versions exist for both notes.
4. Review notes clearly state that only page 001 and page 002 were used.
5. Review notes clearly state that no OCR was run and no raw images were committed.
6. `git diff --check` passes.

## Recommended Next Step

Ask ChatGPT to review whether the Chinese notes remain safely non-verbatim, whether the outline accurately reflects the manually reviewed structure, and whether the listed verification items are sufficient before any deeper chapter processing begins.
