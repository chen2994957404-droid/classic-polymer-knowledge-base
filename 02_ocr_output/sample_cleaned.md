# Chapter 1: Simulated Polymer Chain Notes

This short sample is invented for OCR workflow testing. It is not copied from any textbook, and the wording is deliberately simple so the cleaning step can be checked without academic reconstruction.

<!-- OCR-UNCERTAIN: digit embedded in word -->
A po1ymer chain may be pictured as many small links joined in sequence. In a rough classroom model, the links wiggle, turn, and sometimes look like rn/m when OCR confuses nearby letters.

The end-to-end distance is sometimes represented with a simple display formula:

$$R^2 = nl^2$$

The next block is a simulated multi-line formula. It is intentionally generic and should not be corrected by the cleanup script.

$$
\Delta G = \Delta H - T\Delta S
\Omega = l0O0 + q
$$

A bracket display formula can also appear in OCR output:

\[
\sigma = \frac{N k_B T}{V}
\]

[Figure 1-1: chain conformation schematic]

<!-- OCR-UNCERTAIN: repeated vertical bars -->
The scanned caption might contain unclear symbols such as ??? or repeated marks ||| near the figure label.

[Table 1-1: simulated polymer observation table]

| Sample | Simulated note |
| --- | --- |
| A | flexible coil |
| B | stiff segment with rn/m token |

Review question: Should the token rn/m be read as "nm", "m/m", or left unresolved for source-image comparison?

<!-- OCR-UNCERTAIN: digit embedded in word -->
Another OCR-like line contains l0O and a smudged po1ymer marker so the review workflow has multiple uncertain items.


---

## OCR Cleaning Report

- Script: `scripts/clean_ocr_markdown.py`
- Processing type: conservative engineering cleanup only
- Input lines: 37
- Output lines before report: 40
- Lines with trailing spaces stripped: 0
- Excess blank lines collapsed: 0
- Lines marked as OCR uncertain: 3
- Protected formula/code block lines preserved: 8

Review note: uncertain lines were marked for human review and were not deleted.
