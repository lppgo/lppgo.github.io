

#  1: Python读取各种编码的csv文件
## 1.1 需求背景
- 因为工作原因需要导出导入大量的CSV文件数据，这些CSV文件中存在大量的中文字符数据。但是不同数据来源的CSV格式文件的编码格式并不固定，为正确解析中文字符需要一个可以批量读取不同编码格式的CSV程序;
## 1.2 问题描述
- 通常Python CSV库读取CSV文件经常遇到莫名其妙的编码错误异常，报错信息主要是unicode解码错误，具体报错信息如下：
- `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb1 in position 0: invalid start byte`

# 2: 解决方案
- 中文编码规则主要有gbk、uft-8、utf-8-sig、GB2312、gb18030、iso-8859-1，为解析各种编码特别是涉及中文的CSV文件，防止解析出错出现中文乱码情况，需要造一个轮子（自定义函数）便于解决乱码问题；
## 2.1 解决方案1：一般方法
```python
import csv 
def read_csv(filename):
    #预设编码列表
    encodings = ['gbk','utf-8','utf-8-sig','GB2312','gb18030','iso-8859-1']
    #循环编码列表，直到正确解析返回解析后的数组data,否则返回false
    for e in encodings:
        data = []
        try:
            with open(filename, encoding=e) as f:
                reader = csv.reader(f)
                header = next(reader)
                # print(header)
                for row in reader:
                    data.append(row)
            print(filename,e)
            return data
        except: 
            print(filename,e)
    return False
```
## 2.2 解决方案2：引入chardet模块来读取文件的编码格式
```python
import csv
import chardet

def read_csv(filename):
    # 使用chardet检测文件编码
    with open(filename, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']
    # 使用检测到的编码读取CSV文件
    with open(filename, encoding=encoding) as f:
        reader = csv.reader(f)
        header = next(reader)
        data = [row for row in reader]
    print(filename, encoding)
    return data
```
## 2.3 解决方案3：使用pandas库的read_csv函数
```python
import chardet
import pandas as pd

def read_csv_pd(filename, sep=','): 
    # 1. 使用 'rb' 模式打开文件并读取前几行/字节进行编码检测
    # chardet 有时可能不可靠，但常用于猜测编码
    try:
        with open(filename, 'rb') as f:
            # 读取部分文件内容以提高检测速度
            raw_data = f.read(4096) 
            encode = chardet.detect(raw_data)['encoding']
            
            # 确保检测到的编码名称是小写字符串
            if encode:
                encode = encode.lower()
            else:
                print(f"未能检测到文件编码: {filename}")
                return False
    except Exception as e:
        print(f"文件读取或编码检测失败: {e}")
        return False

    # 2. 尝试使用检测到的编码读取文件
    try:
        # **修复点 1：变量和编码名称统一使用字符串**
        if encode in ['utf-8', 'ascii']: # chardet 有时可能返回 ascii
            # 尝试最常见的 UTF-8
            data = pd.read_csv(filename, encoding='utf-8', sep=sep)
        
        elif 'gb' in encode:
            # **修复点 2：简化中文编码处理逻辑**
            # GB2312, GBK, GB18030 兼容性：从兼容性最好的 GB18030 开始尝试
            try:
                data = pd.read_csv(filename, encoding='gb18030', sep=sep)
            except UnicodeDecodeError:
                # 如果 GB18030 失败，尝试其他检测到的编码，例如原始的 'gbk'
                data = pd.read_csv(filename, encoding='gbk', sep=sep)
        
        elif encode == 'utf-8-sig':
            data = pd.read_csv(filename, encoding='utf-8-sig', sep=sep)
        
        elif encode == 'iso-8859-1':
            # **修复点 3：修正编码名称和参数拼写**
            data = pd.read_csv(filename, encoding='iso-8859-1', sep=sep)
            
        else:
            # 对于其他未知编码，直接用检测到的编码尝试读取
            print(f"尝试使用检测到的未知编码: {encode}")
            data = pd.read_csv(filename, encoding=encode, sep=sep)
            
    except UnicodeDecodeError as e:
        # **修复点 4：通用错误处理**
        print(f"读取文件 {filename} 时发生编码错误: {e}")
        # **解决方案：忽略错误**
        try:
             data = pd.read_csv(filename, encoding=encode, sep=sep, errors='ignore') 
        except Exception as final_e:
             print(f"无法使用任何方式读取文件: {final_e}")
             return False

    except Exception as e:
        print(f"读取文件时发生未知错误: {e}")
        return False
        
    return data
```
