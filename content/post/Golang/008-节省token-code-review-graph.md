---
title: "08-code-review-graph：用知识图谱让 AI Code Review 省下 8 倍 Token"
author: "lucas"
description: "用 Tree-sitter + MCP 为 AI Coding Assistant 建立结构化代码图谱，只读取真正相关的上下文，从而显著降低 Code Review 的 token 消耗。"
date: 2026-04-30
lastmod: 2026-04-30

tags: # 文章所属标签
  ["Go", "AI", "Code Review", "MCP", "Knowledge Graph"]
categories: # 文章所属目录
  ["Go"]
keywords: # 文章关键词
  ["code-review-graph", "MCP", "Tree-sitter", "Code Review", "Token"]
---

- [08-code-review-graph：用知识图谱让 AI Code Review 省下 8 倍 Token](#08-code-review-graph用知识图谱让-ai-code-review-省下-8-倍-token)
  - [1：为什么 AI Code Review 会浪费大量 Token](#1为什么-ai-code-review-会浪费大量-token)
  - [2：code-review-graph 是怎么工作的](#2code-review-graph-是怎么工作的)
    - [2.1 用 Tree-sitter 构建结构化代码图谱](#21-用-tree-sitter-构建结构化代码图谱)
    - [2.2 用 blast radius 只圈出真正相关的文件](#22-用-blast-radius-只圈出真正相关的文件)
    - [2.3 用 MCP 把图谱能力暴露给 AI Coding 工具](#23-用-mcp-把图谱能力暴露给-ai-coding-工具)
  - [3：它到底省了多少 Token](#3它到底省了多少-token)
  - [4：适合什么场景，不适合什么场景](#4适合什么场景不适合什么场景)
  - [5：快速上手](#5快速上手)
  - [6：我对这个工具的看法](#6我对这个工具的看法)
  - [7：相关链接](#7相关链接)

# 08-code-review-graph：用知识图谱让 AI Code Review 省下 8 倍 Token

平常用 Claude Code、Codex、Cursor 这类 AI Coding Agent 时，一个很常见的问题是：**每次问一个稍微复杂一点的问题，AI 都会重新读一遍整个项目**。

项目一大，这件事就会变得很贵，也很慢。你明明只是想问「这个改动会影响哪些文件？」「谁在调用这个函数？」「这次 PR 真正需要 review 的上下文是什么？」，结果 agent 还是从 grep、glob、read 开始，一层一层把代码重新扫一遍。

`code-review-graph` 解决的正是这个问题。它的核心思路很简单：**先把代码仓库编译成一张可查询的结构化图谱，再让 AI 通过 MCP 查询图谱，而不是每次都重新读原始文件。**

> 本文整理自原始分享链接的主题内容，并结合 `code-review-graph` 官方仓库 README 中已经公开的机制、命令和 benchmark 数据做成一篇可落地的实战说明。

## 1：为什么 AI Code Review 会浪费大量 Token

传统 AI code review 的上下文获取方式，通常是这样的：

1. 用户提出一个问题
2. Agent 开始搜索相关文件
3. 读取入口文件、依赖文件、调用方、测试文件
4. 逐步扩大上下文范围
5. 最后才开始真正分析

这个流程的问题不在于它“不能用”，而在于它**成本太高**。

因为对 LLM 来说：

- 每一次 `grep`、`glob`、`read` 都会带来额外上下文开销
- 同一个仓库在不同任务里会被反复读取
- 真正相关的文件可能只有 10 个，但 agent 往往会先读几十甚至上百个
- 仓库越大，token 浪费越夸张

换句话说，很多时候 LLM 不是在“思考问题”，而是在“重新建立项目地图”。

而 `code-review-graph` 做的事情，就是把这张地图预先建好。

## 2：code-review-graph 是怎么工作的

官方说明里，它的定位非常明确：

> AI coding tools re-read your entire codebase on every task. code-review-graph fixes that.

它不是一个通用文档知识库，也不是一个替代 IDE 的索引器，而是专门面向 **AI coding / AI review 场景** 的本地知识图谱工具。

### 2.1 用 Tree-sitter 构建结构化代码图谱

`code-review-graph` 会先把仓库解析成 AST，然后抽取出图里的节点和边。

典型节点包括：

- function
- class
- import
- test
- module
- inheritance relation

典型关系包括：

- 谁调用谁
- 谁依赖谁
- 哪些测试覆盖哪些代码
- 哪些类之间有继承或组合关系

它底层依赖的是 Tree-sitter，所以不是简单的字符串匹配，而是语法层面的结构化解析。

官方 README 中提到，它支持 **23 种语言 + Jupyter/Databricks notebooks**，包括：

- Go
- Python
- TypeScript / JavaScript
- Rust
- Java
- Kotlin
- C / C++
- Ruby
- PHP
- Svelte / Vue
- 以及 `.ipynb`

这意味着它适合的并不只是单一语言项目，而是多语言仓库、前后端混合仓库，甚至 monorepo。

### 2.2 用 blast radius 只圈出真正相关的文件

这个项目最有价值的点，不是“把代码变成图”，而是基于图做 **blast radius analysis**。

也就是：

> 当一个文件发生变化时，顺着调用关系、依赖关系、测试关系，把真正可能受影响的文件圈出来。

这一步很关键。

因为对 code review 来说，我们真正关心的不是“仓库里有什么”，而是：

- 这次改动会波及哪些调用方？
- 会不会影响别的模块？
- 有哪些测试应该一起看？
- 有没有遗漏的依赖链？

如果这一步做得准，AI 就不需要重新扫描全仓，只需要读取“影响半径”里的少量文件。

官方文档对这个过程的表述大意是：

- 对改动文件做图查询
- 追踪 caller、dependent、tests
- 计算最小必要上下文
- 只把这些上下文交给 AI

这也是它节省 token 的根本原因。

### 2.3 用 MCP 把图谱能力暴露给 AI Coding 工具

`code-review-graph` 不是一个只能手动 CLI 查询的工具，它还提供 MCP server。

这一点非常重要，因为只有接进 MCP，Claude Code、Codex、Cursor、Kiro 这类 agent 才能把它当成“原生能力”去调用。

官方 README 里的安装流程大致是：

```bash
pip install code-review-graph
code-review-graph install
code-review-graph build
```

安装完成后，它会：

- 自动识别本地有哪些 AI coding 工具
- 写入对应平台的 MCP 配置
- 注入 graph-aware 的规则或说明
- 启动 `code-review-graph serve` 作为 MCP server

也就是说，从 agent 的视角看，它不再需要“自己摸索整个仓库”，而是可以直接调用：

- `get_minimal_context_tool`
- `get_impact_radius_tool`
- `get_review_context_tool`
- `query_graph_tool`
- `traverse_graph_tool`
- `semantic_search_nodes_tool`
- `list_graph_stats_tool`

这些工具本质上就是：**把昂贵的原始文件扫描，替换成廉价的结构化查询。**

## 3：它到底省了多少 Token

根据官方 README 中公开的 benchmark，`code-review-graph` 在 6 个真实开源仓库、13 个 commit 上做了自动评估。

官方给出的平均结果是：

> **Token efficiency: 8.2x average reduction (naive vs graph)**

也就是说，和“直接读取整个相关源码文件”相比，图谱方案平均能把 token 开销压到原来的大约八分之一。

README 里列出的部分数据如下：

| Repo | Avg Naive Tokens | Avg Graph Tokens | Reduction |
| --- | ---: | ---: | ---: |
| express | 693 | 983 | 0.7x |
| fastapi | 4,944 | 614 | 8.1x |
| flask | 44,751 | 4,252 | 9.1x |
| gin | 21,972 | 1,153 | 16.4x |
| httpx | 12,044 | 1,728 | 6.9x |
| nextjs | 9,882 | 1,249 | 8.0x |
| **Average** | - | - | **8.2x** |

这里有两个点值得特别注意。

### 第一，小仓库和单文件改动不一定收益最大

官方自己也明确写了：像 `express` 这种结果低于 1x 的情况，是因为：

- 改动很小
- 仓库本身不大
- 图谱上下文会附带一些结构化元数据
- 这些元数据在极小任务里，反而可能比直接读原文件更贵

这说明这个项目并不是“任何场景都绝对省 token”，而是：

> **任务越复杂、改动越跨模块、仓库越大，收益越明显。**

### 第二，它选择了 recall 优先

README 里还有一组 impact accuracy 数据：

- recall = 1.0
- average F1 = 0.54
- average precision = 0.38

这代表它的 blast radius 分析采取了比较保守的策略：

- 宁可多给一些可能相关的文件
- 也不要漏掉真正会受影响的文件

对 code review 场景来说，这其实是合理的。

因为 review 最怕的是“漏看”，而不是“多看 2 个文件”。

## 4：适合什么场景，不适合什么场景

我觉得 `code-review-graph` 特别适合下面几类场景。

### 适合的场景

#### 1）大仓库 / 多模块项目

仓库一大，AI 最贵的步骤就不是“生成答案”，而是“重建上下文”。

这种时候，预先维护一张结构化图谱，收益非常明显。

#### 2）频繁做 code review 或 PR review

如果你经常让 Claude Code / Codex 帮你做：

- review delta
- review PR
- 影响分析
- 变更风险识别

那图谱化上下文几乎天然比全文扫描更合理。

#### 3）monorepo 或跨语言仓库

README 里专门强调了 monorepo 场景，因为这种仓库最容易出现：

- 代码量巨大
- 依赖关系复杂
- 真正相关文件其实很少

而这正是图查询最擅长的场景。

#### 4）希望把 MCP 工具链接进 agent workflow

如果你已经在用：

- Claude Code
- Codex CLI
- Cursor
- Kiro

并且习惯 MCP 工作流，那 `code-review-graph` 的接入成本会很低。

### 不那么适合的场景

#### 1）超小型项目

只有几个文件的小项目，直接读原文件就够了，引入图谱反而多一层维护成本。

#### 2）一次性阅读任务

如果你只是偶尔问一个简单问题，不打算长期维护图谱，那收益不会特别高。

#### 3）需要高质量语义搜索排序的场景

官方 README 也坦承了它的一个弱点：

- search quality 的 MRR 还有提升空间
- 某些框架/命名模式下，搜索排序不够稳定

所以如果你追求的是“自然语言语义检索体验”，它现在更像是一个**强结构图谱工具**，而不是最强语义搜索工具。

## 5：快速上手

如果你想先体验它的核心价值，最短路径就是下面几步。

### 5.1 安装

```bash
pip install code-review-graph
```

或者：

```bash
pipx install code-review-graph
```

### 5.2 自动安装到你的 AI coding 平台

```bash
code-review-graph install
```

如果你只想配置某一个平台，也可以指定：

```bash
code-review-graph install --platform claude-code
code-review-graph install --platform codex
code-review-graph install --platform cursor
code-review-graph install --platform kiro
```

### 5.3 首次构建图谱

```bash
code-review-graph build
```

官方 README 提到，一个大约 500 文件的项目，初始 build 大约 10 秒。

### 5.4 增量更新

```bash
code-review-graph update
```

它支持增量更新，只重新解析改动文件，而不是全量重建。

### 5.5 常用命令

```bash
code-review-graph status
code-review-graph watch
code-review-graph detect-changes
code-review-graph visualize
code-review-graph serve
```

如果你是把它接进 agent workflow，我建议至少把下面两件事跑起来：

1. `build`
2. `serve`

这样你的 AI agent 才能真正通过 MCP 查询图谱。

## 6：我对这个工具的看法

我觉得 `code-review-graph` 真正有价值的地方，不是它又做了一个“AI coding 工具”，而是它把一个很关键的问题说清楚了：

> **大型代码库里，最贵的不是回答问题，而是找到该读什么。**

这其实已经不只是 code review 的问题，而是更广义的 agent engineering 问题。

一个 agent 如果每次都从头扫仓库，它的能力再强，都会被上下文成本拖垮。

而知识图谱 / 结构化索引 / blast radius 这种设计，本质上是在做一件事：

> 把“探索成本”从每次提问都重复支付，变成一次建图、长期复用。

这和传统 RAG 也不完全一样。

RAG 更多是“从文档里找相关文本”，而 `code-review-graph` 这种做法更偏向：

- 先理解代码结构
- 再根据结构找上下文
- 最后把最小必要上下文交给模型

对于 code review 这种强依赖依赖关系和调用链的任务，这条路明显更对。

当然，它也不是银弹。

如果你的项目非常小，或者问题非常简单，直接读文件可能反而更划算。但只要你的项目开始出现：

- 多模块调用
- 跨目录依赖
- 频繁 PR review
- monorepo
- 多语言混合

那这种图谱型工具就会越来越值。

## 7：相关链接

- 原始分享链接：
  - https://mp.weixin.qq.com/s/HJi8n8t5RXFCevn0ezmLNg?click_id=6
- 官方 GitHub 仓库：
  - https://github.com/tirth8205/code-review-graph
- 项目安装入口：
  - `pip install code-review-graph`
- 常用命令：
  - `code-review-graph install`
  - `code-review-graph build`
  - `code-review-graph update`
  - `code-review-graph serve`

如果你平常已经在用 Claude Code、Codex 或 Cursor 做代码审查，我非常建议你实际装一下跑一遍。因为这个项目最值得感受的，不是 README 上的那句 **8.2x token reduction**，而是当 agent 第一次不再重读整个仓库时，你会立刻感受到交互速度和上下文质量的变化。