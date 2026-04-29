# Task 001: Create OCR Markdown Cleaner

## Task Goal

Create a small engineering preprocessing script that cleans OCR-derived Markdown or plain text before academic review.

The script must not rewrite academic content, summarize chapters, correct formulas, or invent missing material. Its job is limited to conservative formatting cleanup and marking lines that may need human review.

## Input Assumptions

- The input is a UTF-8 encoded `.md` or `.txt` file.
- The input may contain OCR artifacts, Markdown headings, plain paragraphs, tables, figure captions, and LaTeX-style formulas.
- Formula blocks may appear as `$$ ... $$`, `\[ ... \]`, or fenced code blocks.
- The input may contain excessive blank lines and trailing spaces.
- The input may contain uncertain OCR characters or suspicious tokens.

## Output Behavior

The script should write a UTF-8 Markdown file that:

1. Strips trailing spaces from each line.
2. Normalizes excessive blank lines to at most two consecutive blank lines.
3. Preserves Markdown headings and the original line order.
4. Preserves LaTeX-style formula blocks without changing their contents except trailing-space cleanup.
5. Marks suspicious OCR lines with a visible `<!-- OCR-UNCERTAIN: ... -->` comment immediately before the original line.
6. Never deletes uncertain lines.
7. Appends a short cleaning report at the end of the output file.

## Forbidden Actions

Codex and the script must not:

1. Delete original source files.
2. Modify files outside the explicitly requested output path.
3. Rewrite, summarize, or academically reinterpret textbook content.
4. Invent missing words, formulas, figure labels, or table values.
5. Remove uncertain OCR content.
6. Expose API keys, private tokens, or raw copyrighted source files.
7. Install dependencies.

## How To Run

From the repository root:

```bash
python scripts/clean_ocr_markdown.py input.md output.md
```

Example:

```bash
python scripts/clean_ocr_markdown.py 02_ocr_output/chapter_01_raw_ocr.md 02_ocr_output/chapter_01_cleaned.md
```

The script uses only the Python standard library.

## ChatGPT Review Workflow

After Codex generates the cleaned Markdown file:

1. ChatGPT reviews the `<!-- OCR-UNCERTAIN: ... -->` comments.
2. ChatGPT compares uncertain lines with the source image, scan, or raw OCR when needed.
3. ChatGPT checks whether formulas, headings, figures, and tables remain in the correct locations.
4. ChatGPT performs academic reconstruction only after the engineering cleanup is complete.
5. Any unresolved OCR/formula/table uncertainty should be recorded in review notes before final chapter notes are produced.

## Completion Criteria

This task is complete when:

1. `scripts/clean_ocr_markdown.py` exists and runs from the command line.
2. The script accepts exactly an input path and output path.
3. The output preserves source content while cleaning whitespace.
4. Uncertain OCR lines are marked but not deleted.
5. A cleaning report is appended to the output file.
