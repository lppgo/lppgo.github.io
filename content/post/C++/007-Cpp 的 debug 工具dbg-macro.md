---
title: "007-Cpp debug 工具dbg-macro"
author: "lucas"
date: 2023-05-03
lastmod: 2021-05-03

tags: ["C++"]
categories: ["C++"]
keywords: ["C++", "dbg", "debug"]
---

<div align='center' ><font size='50'>Cpp debug 工具dbg-macro</font></div>

# 1: 介绍

- https://github.com/sharkdp/dbg-macro
- 打日志是 C++ 开发中必不可少的一种 debug 方式，dbg-macro 受 Rust 语言中 的 dbg 启发，提供比 printf 和 std::cout 更好的宏函数。主要有如下特点：
  - 美观的彩色输出（当输出不是交互式终端时，颜色将自动禁用）
  - 兼容 C++11，并且是 header-only
  - 支持基础类型和 STL 容器类型的输出
  - 可以输出文件名、行号、函数名和原始表达式

# 2：install

```bash
git clone https://github.com/sharkdp/dbg-macro
sudo ln -s $(readlink -f dbg-macro/dbg.h) /usr/include/dbg.h
```

## 2.1 On Arch Linux

- `yay -S dbg-macro`

## 2.2 With vcpkg

- `vcpkg install dbg-macro`

## 2.3 With cmake

- `CMakeLists.txt`
-

```cmake
cmake_minimum_required(VERSION 3.11) # FetchContent added in cmake 3.11
project(app) # name of executable

set(CMAKE_CXX_STANDARD 17)

# dbg-macro
include(FetchContent)

FetchContent_Declare(dbg_macro GIT_REPOSITORY https://github.com/sharkdp/dbg-macro)
FetchContent_MakeAvailable(dbg_macro)

add_executable(${PROJECT_NAME} main.cpp) # your source files goes here
target_link_libraries(${PROJECT_NAME} PRIVATE dbg_macro) # make dbg.h available

```

- `main.cpp`

-

```cpp
#include <dbg.h>

int main() {
  dbg(42, "hello world", false);
  return 0;
}
```
