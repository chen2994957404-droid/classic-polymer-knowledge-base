# Task 007 ChatGPT Review

## Task Summary

Task 007 registers the full scanned textbook PDF as a local-only source file and creates a safety plan for future processing.

No OCR was run. No PDF content was extracted. No full-page transcript was created. No textbook text was copied into tracked files.

## Source PDF Files Found

Folder checked:

```text
01_raw_local/source_books/
```

PDF files found:

| Filename | File size |
| --- | ---: |
| `高分子物理（修订版）何曼君.pdf` | 29,387,471 bytes |

## Git Ignore Safety

The PDF is ignored by Git through:

```text
.gitignore:184:01_raw_local/
```

The source PDF must remain under `01_raw_local/` and must not be committed.

## Copyright Risk Check

Current risk is low because this task records only local file metadata and workflow rules. It does not extract or copy textbook text.

Future tracked files should contain only:

- workflow notes
- short review metadata
- uncertainty lists
- non-verbatim chapter notes
- Notion-ready summaries

Raw PDF files, page images, and raw OCR outputs must remain local-only under `01_raw_local/`.

## Recommended Processing Strategy

Process by chapter and subsection, not all at once.

Recommended future workflow:

1. Select a very small unit, ideally one subsection or 1-2 pages.
2. Keep raw PDF and page images under `01_raw_local/`.
3. If OCR is approved later, write raw OCR output only under `01_raw_local/`.
4. Review OCR or manual notes before creating tracked outputs.
5. Track only non-verbatim Chinese study notes and concise Notion-ready summaries.
6. Use review notes to record uncertainty, terminology questions, and copyright checks.

## OCR Tool Requirement

OCR should not be run until a local OCR tool is confirmed and the exact small input unit is selected. Raw OCR must never be stored in tracked folders.

Any OCR test should be limited to a small sample and should write output only to an ignored local folder under `01_raw_local/`.

## Recommended Next Step

Continue with manual, subsection-sized extraction before using OCR. If OCR becomes necessary, create a separate task that specifies the exact pages, command, local-only output folder, and review process.

## Commit/Push Status

No commit has been made. No push has been made.
