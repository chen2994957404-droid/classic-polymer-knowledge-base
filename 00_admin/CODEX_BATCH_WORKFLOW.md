# Codex 批次工作流

## 基本原则

Codex 在本项目中负责工程支持、文件组织、脚本维护、批次文档和复核记录。ChatGPT 负责学术重构、公式检查和最终内容质量。

## 每个大批次必须先有计划

批次开始前应明确：

- 任务目标。
- 允许创建或修改的文件。
- 禁止动作。
- 来源范围。
- 输出文件。
- 验收条件。
- ChatGPT 复核点。

## 文件修改边界

- 只修改用户明确允许的文件。
- 不修改 `01_raw_local/`。
- 不提交原始 PDF、页面图片、原始 OCR。
- 不创建逐页逐字稿。
- 不把 raw OCR 放入跟踪目录。

## 禁止动作

- 不浏览网页，除非用户明确要求且安全规则允许。
- 不运行未批准 OCR。
- 不抽取 PDF 正文。
- 不处理全书原始扫描。
- 不复制大段教材文本。
- 不提交。
- 不推送。

## 标准执行步骤

1. 检查当前 `git status --short --untracked-files=all`。
2. 检查允许路径是否已存在。
3. 读取相关项目规则、模板或已有任务文档。
4. 创建或修改允许文件。
5. 确认没有触碰 `01_raw_local/`。
6. 运行：

   ```text
   git status --short
   git diff --check
   ```

7. 在最终回复中报告：

   - 创建或修改的文件。
   - 是否删除错误文件。
   - 是否只改了允许文件。
   - `git diff --check` 是否通过。
   - ChatGPT 下一步应复核什么。

## 复核记录要求

每个批次都应在 `07_review_notes/` 创建复核记录，说明：

- Task Summary。
- Files Created or Modified。
- Commands Run。
- Source Information Used。
- Copyright Risk Check。
- Non-verbatim Handling Confirmation。
- Items Requiring ChatGPT Review。
- Recommended Next Step。
- Commit/Push Status。

## 何时停止并请求 ChatGPT

Codex 应在以下情况停止：

- 需要判断公式是否正确。
- 需要解释或重构复杂概念。
- 图表归属不清。
- 内容接近原文，需要版权判断。
- 页码或章节边界不清。
- 用户要求的动作会触碰禁止项。

## 默认结论

除非用户明确要求并允许，Codex 不应运行 OCR、不应处理原始文件、不应提交或推送。
