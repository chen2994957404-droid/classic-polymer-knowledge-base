\# Codex Task Template



\## Task Name



Write the task name here.



\## Background



This task belongs to the classic polymer knowledge-base project.



ChatGPT is responsible for academic editing and content quality control.



Codex is responsible for engineering execution only.



\## Input



Describe the input files here.



Example:



\- `01\_raw\_local/chapter\_01.pdf`

\- `01\_raw\_local/page\_images/`



\## Output



Describe the required output files here.



Example:



\- `02\_ocr\_output/chapter\_01\_raw\_ocr.md`

\- `02\_ocr\_output/chapter\_01\_cleaned.md`

\- `07\_review\_notes/chapter\_01\_uncertain\_items.md`



\## Requirements



Codex should:



1\. Keep the original structure as much as possible.

2\. Do not delete uncertain content.

3\. Mark uncertain OCR items clearly.

4\. Preserve formula locations.

5\. Preserve figure and table locations.

6\. Avoid academic rewriting unless instructed.

7\. Generate a review note file.



\## Forbidden Actions



Codex should not:



1\. Push raw copyrighted PDFs to GitHub.

2\. Delete original files.

3\. Invent missing textbook content.

4\. Rewrite final academic explanations without review.

5\. Expose API keys or tokens.



\## Completion Criteria



The task is complete when:



1\. All expected output files are generated.

2\. Uncertain OCR/formula/table items are listed.

3\. The generated files can be reviewed by ChatGPT.

