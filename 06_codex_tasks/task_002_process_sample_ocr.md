# Task 002: Process Simulated OCR Sample

## Task Goal

Test the OCR cleanup workflow with a short, self-made sample that imitates polymer textbook OCR output.

This task checks whether the conservative cleanup script can preserve formulas, headings, figure/table placeholders, and line order while marking suspicious OCR artifacts for human review.

## Copyright Note

The sample must be simulated rather than copied from a real textbook. It should use invented wording, invented examples, and placeholder figures/tables so the workflow can be tested without reproducing copyrighted academic content.

## Input File

- `02_ocr_output/sample_input.md`

## Output Files

- `02_ocr_output/sample_cleaned.md`
- `07_review_notes/sample_uncertain_items.md`

## Workflow Steps

1. Create a short simulated OCR input file with invented polymer-learning content.
2. Include headings, paragraphs, formulas, figure/table placeholders, OCR-like suspicious tokens, and at least one review question.
3. Run the conservative cleanup script:

   ```bash
   python scripts/clean_ocr_markdown.py 02_ocr_output/sample_input.md 02_ocr_output/sample_cleaned.md
   ```

4. Review the cleaned Markdown output.
5. Record suspicious tokens, protected formula blocks, placeholders, and review questions in `07_review_notes/sample_uncertain_items.md`.

## Completion Criteria

This task is complete when:

1. The simulated input file exists and contains no real textbook text.
2. The cleanup script runs successfully on the simulated input.
3. The cleaned output file is created with an appended OCR Cleaning Report.
4. Single-line, multi-line, and bracket display formulas are preserved.
5. Suspicious OCR-like lines are marked but not deleted.
6. The review note lists uncertain items and confirms whether protected formula/code lines were preserved.

## ChatGPT Review Criteria

ChatGPT should review:

1. Whether all suspicious OCR tokens are visible in the cleaned output.
2. Whether formula blocks remain in the correct order and are not corrected or rewritten.
3. Whether figure and table placeholders remain in place.
4. Whether the review question is still present.
5. Whether the cleanup report indicates protected formula/code block lines were preserved.
