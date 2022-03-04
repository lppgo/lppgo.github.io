---
title: "02-修改ubuntu/centos默认编辑器为vim"
author: "lucas" # 文章作者
description: "..."
date: 2021-04-15
lastmod: 2021-04-15

tags: # 文章所属标签
  ["Linux"]
categories: # 文章所属目录
  ["Linux"]
keywords: # 文章关键词
  ["Linux", "Ubuntu", "vim"]
# prev: ./20210415-01.md # 上一篇博客地址
# next: ./20210415-03.md # 下一篇博客地址
---

- [1: 直接在配置文件中修改](#1-直接在配置文件中修改)
- [2: 使用系统管理工具 update\-alternatives](#2-使用系统管理工具-update-alternatives)
- [3: 完全删除 nano](#3-完全删除-nano)

# 1: 直接在配置文件中修改

```shell
echo export EDITOR=/usr/bin/vim >> ~/.bashrc
```

# 2: 使用系统管理工具 update-alternatives

update-alternatives --config editor

```shell
xxx:~$ update-alternatives --config editor
有 4 个候选项可用于替换 editor (提供 /usr/bin/editor)。

 选择       路径              优先级  状态
------------------------------------------------------------
* 0            /bin/nano            40        自动模式
 1            /bin/ed             -100       手动模式
 2            /bin/nano            40        手动模式
 3            /usr/bin/vim.basic   30        手动模式
 4            /usr/bin/vim.tiny    10        手动模式

要维持当前值[*]请按<回车键>，或者键入选择的编号：3
```

# 3: 完全删除 nano

如果系统中只剩下 nano 和 vim 两个编辑器，完全删除 nano，那么系统会默认选择 vim 为默认编辑器 在终端输入删除 nano 编辑器的命令：

```shell
apt-get remove nano
```
