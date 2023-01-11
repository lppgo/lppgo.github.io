
<div align='center' ><font size='50'>CMakeLists.txt说明</font></div>

- [1 C/C++基础](#1-cc基础)
- [2 Vscode 安装 C/C++插件](#2-vscode-安装-cc插件)
- [3 task.json，launch.json](#3-taskjsonlaunchjson)
  - [3.1 task.json 是编译当前文件的指令](#31-taskjson-是编译当前文件的指令)
  - [3.2 launch.json](#32-launchjson)
  - [3.3 c_cpp_properties.json](#33-c_cpp_propertiesjson)
- [4 cmake](#4-cmake)

# CMakeLists.txt

```cmake
# cmake最小版本要求3.21.0
cmake_minimum_required(VERSION 3.21.0)

# 指定project名称为client
project(client)

# set 定义变量
set(PROJ_VERSION v1.0.0)

set(CMAKE_CXX_STANDARD 17)
# 设置编译器编译模式
set(cmake_build_type "Debug")

# include 指令用来载入并运行来自于文件或模块的 CMake 代码
#include()

# 将/usr/include/myincludefolder 和./include添加到头文件搜索路径
#include_directories(/usr/include/myincludefolder ./include)
include_directories(include)

# 将/usr/lib/myincludefolder ./lib添加到库文件搜索路径
#link_directories(/usr/lib/myincludefolder ./lib)

# 设置源文件path
aux_source_directory(src DIR_SRCS)
#aux_source_directory(src/entity DIR_ENTITY)
#source_group(src src/entity)

# 生成共享库,这儿不需要.hpp
#add_library(calculate SHARED hello.cpp)

#添加编译参数 -Wall -std=c++11
add_compile_options(-Wall -std=c++17 -o2)

# 链接共享库,将calculate.so动态库链接到可执行文件main
#target_link_libraries(main calculate)


# 添加需要的所有的执行文件
add_executable(client ${DIR_SRCS})

# ---------------CMake常用变量----------------
# CMAKE_C_FLAGS #gcc编译选项
# CMAKE_CXX_FLAGS #g++编译选项
# set( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11") #这表明不会覆盖CMAKE_CXX_FLAGS，而是在它后面追加-std=c++11这个编译选项
#
##设定编译类型为debug，调试时需要选择debug
# set(CMAEK_BUILE_TYPE Debug)
##设定编译类型为release，发布时需要选择release
# set(CMAKE_BUILE_TYPE Release)
#
# CMAKE_BINARY_DIR
# CMAKE_SOURCE_DIR #指定CMakeList.txt所在的路径
# CMAKE_C_COMPILER #指定C编译器
# CMAKE_CXX_COMPILER #指定C++编译器
# EXECUTABLE_OUTPUT_PATH #可执行文件输出的存放路径
# LIBRARY_OUTPUT_PATH #库文件输出的存放路径

```
