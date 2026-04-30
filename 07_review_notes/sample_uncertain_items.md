# Sample OCR Review Notes

## Suspicious OCR Tokens Found

- `po1ymer` appears in prose and should be checked against the intended word.
- `rn/m` appears in prose, the table placeholder row, and the review question.
- `l0O0` appears inside the protected multi-line formula block and should be reviewed without automatic correction.
- `???` appears as a simulated unclear-symbol marker in the figure-caption line.
- `|||` appears in the figure-caption line and was marked by the cleanup script.
- `l0O` appears in the final prose line and should be reviewed with the nearby `po1ymer` marker.

## Formula Blocks Found

- Single-line display formula: `$$R^2 = nl^2$$`
- Multi-line display formula:

  ```text
  $$
  \Delta G = \Delta H - T\Delta S
  \Omega = l0O0 + q
  $$
  ```

- Bracket display formula:

  ```text
  \[
  \sigma = \frac{N k_B T}{V}
  \]
  ```

## Figure And Table Placeholders Found

- `[Figure 1-1: chain conformation schematic]`
- `[Table 1-1: simulated polymer observation table]`

## Lines That Need ChatGPT Academic Review

- The prose line containing `po1ymer` and `rn/m`.
- The multi-line formula line containing `l0O0`.
- The figure-caption line containing `???` and `|||`.
- The table row containing `rn/m`.
- The review question asking whether `rn/m` should be read as `nm`, `m/m`, or left unresolved.
- The final prose line containing `l0O` and `po1ymer`.

## Cleanup Report Check

The cleanup report in `02_ocr_output/sample_cleaned.md` indicates:

- Lines marked as OCR uncertain: 3
- Protected formula/code block lines preserved: 8

Protected formula/code lines were preserved.
