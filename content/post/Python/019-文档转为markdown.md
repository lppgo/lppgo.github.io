---
title: "019-文档转为markdown"
author: "lucas"
description: ""
date: 2024-12-25
lastmod: 2025-01-22

categories: ["Python"]
tags: ["Python", "markdown", "tools"]
keywords: ["Python", "markdown", "tools"]
---

# 将非 Markdown 格式的文档转换为 Markdown

## 1：介绍

- 这是一个由微软开源的 Python 工具，可以将非 Markdown 格式的文档转换为 Markdown 格式，支持 PDF、PPT、Word 和 Excel 等多种文件类型，为文档的索引和文本分析提供了极大的便利。

- `github.com/microsoft/markitdown`

## 2：代码示例

```python3
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("hellogithub.xlsx")
print(result.text_content)

```
