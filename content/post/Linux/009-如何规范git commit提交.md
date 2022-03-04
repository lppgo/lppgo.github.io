<!--
 * @Author: lucas李平平
 * @Date: 2021-09-01 20:31:01
 * @LastEditTime: 2021-09-11 11:52:37
 * @LastEditors:
 * @Description: desc
 * @FilePath: /lppgo.github.io/content/post/20210414-02-如何规范git commit提交.md
-->

---

title: "02-如何规范 git commit 提交"
author: "lucas" # 文章作者
description: "如何规范 git commit 提交..."
date: 2021-04-14
lastmod: 2021-04-14

tags: # 文章所属标签
["Git"]
categories: # 文章所属目录
["Linux"]
keywords: # 文章关键词
["Git", "规范"]

# prev: ./20210414-01.md # 上一篇博客地址

# next: ./20210415-01.md # 下一篇博客地址

---

- [prev: ./20210414-01.md # 上一篇博客地址](#prev-20210414-01md--上一篇博客地址)
- [next: ./20210415-01.md # 下一篇博客地址](#next-20210415-01md--下一篇博客地址)
- [1: 规范 git 分支](#1-规范-git-分支)
- [2: 做好提交前的 Code Review](#2-做好提交前的-code-review)
- [3: Commit 信息提示](#3-commit-信息提示)

# 1: 规范 git 分支

[git 项目分支管理](https://www.cnblogs.com/jiaoshou/p/11808361.html)

# 2: 做好提交前的 Code Review

# 3: Commit 信息提示

```go
 feat：新增功能
 add: 新增文件
 fix：bug 修复
 docs：文档更新
 style：不影响程序逻辑的代码修改(修改空白字符，格式缩进，补全缺失的分号等，没有改变代码逻辑)
 refactor：重构代码(既没有新增功能，也没有修复 bug)
 perf：性能, 体验优化
 test：新增测试用例或是更新现有测试
 build：主要目的是修改项目构建系统(例如 glup，webpack，rollup 的配置等)的提交
 ci：主要目的是修改项目继续集成流程(例如 Travis，Jenkins，GitLab CI，Circle等)的提交
 chore：不属于以上类型的其他类型，比如构建流程, 依赖管理
 revert：回滚某个更早之前的提交


```
