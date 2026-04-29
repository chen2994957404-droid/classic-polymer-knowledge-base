\# Project Rules



\## Project Positioning



This project is a personal academic knowledge-base project for classic polymer science textbooks and related materials.



The goal is not to simply copy textbook content, but to reconstruct the knowledge into a classic-and-modern integrated learning system.



\## Tool Roles



\### ChatGPT



ChatGPT acts as:



\- Editor-in-chief

\- Knowledge architect

\- Content reviewer

\- Formula checker

\- Concept explainer

\- Notion content designer



ChatGPT is responsible for the academic quality of the final notes.



\### Codex



Codex acts as:



\- Engineering assistant

\- Script writer

\- OCR pipeline builder

\- Markdown cleaner

\- File organizer

\- Notion export helper



Codex should not independently rewrite the final textbook-style content unless specifically instructed.



\### GitHub



GitHub acts as:



\- Version-controlled middle layer

\- Task record system

\- Script storage

\- Markdown storage

\- Review and correction history



\### Notion



Notion acts as:



\- Final knowledge base interface

\- Literature and textbook note database

\- Long-term review and learning platform



\## Copyright and Raw Files



Raw textbook PDFs, scanned images, and full unprocessed OCR outputs should remain local by default.



Do not push the following to GitHub:



\- full textbook PDFs

\- complete scanned page images

\- full raw OCR of copyrighted textbooks

\- API keys

\- private tokens

\- large temporary files



The repository should mainly contain:



\- project rules

\- task prompts

\- scripts

\- structured personal notes

\- review comments

\- self-made figures

\- Notion-ready summaries



\## Content Standard



Every final chapter note should include:



1\. Original chapter structure

2\. Core concepts

3\. Key formulas in LaTeX

4\. Formula explanations

5\. Tables and diagrams where useful

6\. Important derivations

7\. Typical misunderstandings

8\. Review questions and answers

9\. Modern research extensions where appropriate

10\. Notion-ready formatting



\## Workflow



The standard workflow is:



1\. Put raw files in `01\_raw\_local/`

2\. Let Codex perform OCR or file preprocessing

3\. Store OCR drafts in `02\_ocr\_output/`

4\. Let ChatGPT review and reconstruct the content

5\. Store final notes in `03\_chapter\_notes/`

6\. Store figures in `04\_figures/`

7\. Store Notion-ready exports in `05\_notion\_ready/`

8\. Store Codex task prompts in `06\_codex\_tasks/`

9\. Store review notes in `07\_review\_notes/`

