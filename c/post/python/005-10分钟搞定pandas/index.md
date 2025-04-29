
- [1：什么是 pandas](#1什么是-pandas)
- [2：十分钟搞定 pandas（译文+注释）](#2十分钟搞定-pandas译文注释)
- [3：创建对象](#3创建对象)
- [4：查看数据](#4查看数据)
- [5：选择数据](#5选择数据)
- [6：缺失数据处理](#6缺失数据处理)
- [7：相关操作](#7相关操作)
- [8：合并](#8合并)
- [9：分组](#9分组)
- [10：重塑](#10重塑)
- [11：时间序列](#11时间序列)
- [12：分类](#12分类)
- [13：绘图](#13绘图)
- [14：获取数据写入导出](#14获取数据写入导出)
- [15：小陷阱](#15小陷阱)
- [16：pandas 实战](#16pandas-实战)

# 1：什么是 pandas

先看-> **[10 分钟搞定 pandas+实例](https://pyzh.readthedocs.io/en/latest/python-pandas.html)**

> 转自: https://pyzh.readthedocs.io/en/latest/python-pandas.html
> 本文是 pandas 官网 10 Minutes to pandas 的翻译 。

- **pandas** : Python 数据分析模块
  pandas 是为了解决数据分析任务而创建的，纳入了大量的库和标准数据模型，提供了高效地操作大型数据集所需的工具。

- **pandas 中的数据结构 :**
  - **Series:** 一维数组，类似于 python 中的基本数据结构
  - **List:** 区别是 series 只允许存储相同的数据类型，这样可以更有效的使用内存，提高运算效率。就像数据库中的列数据。
  - **DataFrame:** 二维的表格型数据结构。很多功能与 R 中的 data.frame 类似。可以将 DataFrame 理解为 Series 的容器。
  - **Panel：** 三维的数组，可以理解为 DataFrame 的容器。

# 2：十分钟搞定 pandas（译文+注释）

[原文](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)

引入需要的包:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

numpy 是一个 python 实现的科学计算包
matplotlib 是一个 python 的 2D 绘图库
更多章节请查看 [Cookbook](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html)

# 3：创建对象

> 详情请查看 [数据结构](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html)介绍

- 1. 通过传入一个列表来创建 Series ，pandas 会创建默认的整形指标:

```python
>>> s = pd.Series([1,3,5,np.nan,6,8])
>>> s
0  1
1  3
2  5
3  NaN
4  6
5  8
dtype: float64
```

# 4：查看数据

# 5：选择数据

# 6：缺失数据处理

# 7：相关操作

# 8：合并

# 9：分组

# 10：重塑

# 11：时间序列

# 12：分类

# 13：绘图

# 14：获取数据写入导出

# 15：小陷阱

# 16：pandas 实战
