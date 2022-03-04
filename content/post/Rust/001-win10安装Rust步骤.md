---
title: "01-win10安装Rust步骤"
author: "lucas"
draft: false
date: 2021-04-25
lastmod: 2021-04-25

tags: # 文章所属标签
  ["Rust"]
categories: # 文章所属目录
  ["Rust"]
keywords: # 文章关键词
  ["Rust", "环境搭建"]
---

# 1: 首先配置环境变量

```bash
# 修改为国内镜像
#    由于rustup的官方服务器在国外，如果直接按照rust官网的方式安装，
#    非常慢且容易fail
RUSTUP_DIST_SERVER=http://mirrors.ustc.edu.cn/rust-static
RUSTUP_UPDATE_ROOT=http://mirrors.ustc.edu.cn/rust-static/rustup


# rust 安装路径
CARGO_HOME：D:\Program Files\RUST\.cargo
RUSTUP_HOME：D:\Program Files\RUST\.rustup

#
~/.cargo/bin 添加到PATH

# 下载安装racer (rust代码补全程序)
# 如果不成功，先将rustup更新成nightly版本，再进行下载：
rustup install nightly
cargo +nightly install racer

```

# 2：按照官网方式进行安装

地址:https://www.rust-lang.org/zh-CN/tools/install

> 注意：Rust 的编译工具依赖 C 语言的编译工具，这意味着你的电脑上至少已经存在一个 C 语言的编译环境。如果你使用的是 Linux 系统，往往已经具备了 GCC 或 clang。如果你使用的是 macOS，需要安装 Xcode。如果你是用的是 Windows 操作系统，你需要安装 Visual Studio 2013 或以上的环境（需要 C/C++ 支持）以使用 MSVC 或安装 MinGW + GCC 编译环境（Cygwin 还没有测试）。

使用官网的 rustup-init.exe 进行安装

安装完成，使用命令查看:

```bash
rustc -V
cargo -V
```

# 3: VScode 配置环境

1: Rust

2: Rustfmt

3: 为了能调试软件，再安装插件 CodeLLDB，当然，也可以选择使用 GDB

4: crates 是辅助开发者在使用 Cargo.toml 时管理依赖的插件，推荐下载
