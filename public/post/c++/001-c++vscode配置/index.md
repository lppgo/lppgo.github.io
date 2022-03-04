
<div align='center' ><font size='50'>C++ VScode 配置</font></div>

- [1 C/C++基础](#1-cc基础)
- [2 Vscode 安装 C/C++插件](#2-vscode-安装-cc插件)
- [3 task.json，launch.json](#3-taskjsonlaunchjson)
  - [3.1 task.json 是编译当前文件的指令](#31-taskjson-是编译当前文件的指令)
  - [3.2 launch.json](#32-launchjson)
  - [3.3 c_cpp_properties.json](#33-c_cpp_propertiesjson)
- [4 cmake](#4-cmake)

# 1 C/C++基础

- `gcc`工具用来编译运行 C 语言编写的源文件；
- `g++`工具用来编译运行 C++语言编写的源文件；
- `gdb`工具用来调试 C/C++代码。
- gcc -v
- g++ -v

在命令行环境中，基本的编译运行命令大致如下：

```bash
# 使用 gcc 编译一个名叫 hello.c 的 C 文件，生成名为 hello 的可执行文件，或……
$ gcc hello.c -o hello
# 使用 g++ 编译一个名叫 hello.cpp 的 C++ 文件，生成名为 hello 的可执行文件
$ g++ hello.cpp -o hello

# 执行可执行文件 hello
$ ./hello
```

# 2 Vscode 安装 C/C++插件

- `C/C++ for Visual Studio Code`官方 plugin
- `C/C++ Runner`
- **Code Runner** 大多数情况下我们可以直接利用之前安装的 Code Runner 插件进行编译运行 C/C++ 程序。默认情况下 Code Runner 编译 C、C++ 文件的配置如下：

  ```bash
  "code-runner.executorMap": {
  "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
  "cpp": "cd $dir && g++ $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
  }
  ```

- **安装 C/C++ 编译调试工具**

  ```bash
  sudo apt install build-essential

  sudo apt install gcc g++ gdb
  ```

- **VS Code 智能代码提示** `c_cpp_properties.json`

# 3 task.json，launch.json

## 3.1 task.json 是编译当前文件的指令

```json
{
  // See https://go.microsoft.com/fwlink/?LinkId=733558
  // for the documentation about the tasks.json format
  "version": "2.0.0",
  "tasks": [
    {
      "type": "shell",
      "label": "g++ build active file",
      "command": "/usr/bin/g++",
      "args": [
        "-g", //启用gdb调试
        // "${workspaceFolder}/src/*.cpp", //头文件实现的cpp源文件
        "${workspaceFolder}/*.cpp", // main.cpp
        "-I",
        "${workspaceFolder}/include", // 头文件路径
        "-o",
        "${workspaceFolder}/${fileBasenameNoExtension}"
      ],
      "options": {
        "cwd": "${workspaceFolder}"
      },
      "problemMatcher": ["$gcc"],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```

## 3.2 launch.json

- 执行当前文件并让 gdb 调试工具连接到可执行文件的指令

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "(gdb) Launch", // 配置名称，将会在启动配置的下拉菜单中显示
      "type": "cppdbg", // 配置类型，这里只能为cppdbg
      "request": "launch", // 请求配置类型，可以为launch（启动）或attach（附加）
      //   "program": "${workspaceFolder}/a.out", // 将要进行调试的程序的路径
      "program": "${workspaceFolder}/${fileBasenameNoExtension}", // 将要进行调试的程序的路径
      "args": [], // 程序调试时传递给程序的命令行参数，一般设为空即可
      "stopAtEntry": false, // 设为true时程序将暂停在程序入口处
      //   "cwd": "${workspaceFolder}", // 调试程序时的工作目录
      "cwd": "/mnt/e/cppProjects001/test-1", // 调试程序时的工作目录
      "environment": [],
      "externalConsole": false, // 调试时是否显示控制台窗口，一般设置为true显示控制台
      "MIMode": "gdb",
      "setupCommands": [
        {
          "description": "Enable pretty-printing for gdb",
          "text": "-enable-pretty-printing",
          "ignoreFailures": true
        }
      ],
      "miDebuggerPath": "/usr/bin/gdb", // 调试器路径，Windows下后缀不能省略，Linux下则去掉
      "preLaunchTask": "g++ build active file"
      // 调试会话开始前执行的任务，一般为编译程序，c++为g++, c为gcc。调试会话开始前执行的任务，一般为编译程序。与tasks.json的label相对应
    },

    // Runner
    {
      "name": "C/C++ Runner: Debug Session",
      "type": "cppdbg",
      "request": "launch",
      "args": [],
      "stopAtEntry": false,
      "cwd": "/mnt/e/cppProjects001/test-1",
      "environment": [],
      "program": "/mnt/e/cppProjects001/test-1/build/Debug/outDebug",
      "internalConsoleOptions": "openOnSessionStart",
      "MIMode": "gdb",
      "miDebuggerPath": "/usr/bin/gdb",
      "externalConsole": false,
      "setupCommands": [
        {
          "description": "Enable pretty-printing for gdb",
          "text": "-enable-pretty-printing",
          "ignoreFailures": true
        }
      ]
    }
  ]
}
```

## 3.3 c_cpp_properties.json

```json
{
  "configurations": [
    {
      "name": "linux-gcc-x64",
      "includePath": [
        "${workspaceFolder}/**", //源文件
        "${workspaceFolder}/include" //头文件
      ],
      "compilerPath": "/usr/bin/gcc",
      "cStandard": "c11",
      "cppStandard": "c++17",
      "intelliSenseMode": "linux-gcc-x64",
      "compilerArgs": ["-Wall", "-Wextra", "-Wpedantic"],
      "configurationProvider": "ms-vscode.cmake-tools"
    }
  ],
  "version": 4
}
```

# 4 cmake

- CMake 是一个跨平台的安装(编译)工具,可以用简单的语句来描述所有平台的安装(编译过程)。他能够输出各种各样的 makefile 或者 project 文件,能测试编译器所支持的 C++特性,类似 UNIX 下的 automake。
- CMakeLists.txt

```cmake
#set dirs
set(PROJECT_ROOT ${CMAKE_CURRENT_LIST_DIR})
message("project dir:${PROJECT_ROOT}")

SET(CMAKE_EXPORT_COMPILE_COMMANDS ON)   #导出clangd需要的文件，用于智能提示和基于语议的补全
SET(BIN_DESTINATION ${PROJECT_SOURCE_DIR})
SET(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${BIN_DESTINATION})
SET(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${BIN_DESTINATION})
SET(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${BIN_DESTINATION})
SET(CMAKE_PROJECT_VERSION 1.0.1)
if (POLICY CMP0048)
  cmake_policy(SET CMP0048 NEW)
endif (POLICY CMP0048)

PROJECT (HelloWorld VERSION 1.0 LANGUAGES CXX)
SET(SRC_LIST main.cpp)
ADD_EXECUTABLE(test-1 ${SRC_LIST})
```
