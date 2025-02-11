
# pyenv 管理 python 多版本

## 1：virtualenv

- virtualenv 所要解决的是同一个库不同版本共存的兼容问题。例如项目 A 需要用到 requests 的 1.0 版本，项目 B 需要用到 requests 的 2.0 版本。如果不使用工具的话，一台机器只能安装其中一个版本，无法满足两个项目的需求。
- virtualenv 的解决方案是为每个项目创建一个独立的虚拟环境，在每个虚拟环境中安装的库，对其他虚拟环境完全无影响。所以就可以在一台机器的不同虚拟环境中分别安装同一个库的不同版本。

- virtualenv 在使用方法上也比较简单：

```bash
# 安装 virtualenv
pip install virtualenv
# 创建虚拟环境 myenv
virtualenv /path/to/myenv
# 切换到虚拟环境 myenv，此时命令提示符前会有 (myenv) 提示符
cd /path/to/myenv/ && source bin/activate
# 安装库，安装到 /path/to/myenv/lib 中，不会与其他虚拟环境冲突
pip install requests
# 执行 python 相关命令
python demo.py
# 退出虚拟环境
deactivate

```

## 2: pyvenv

- pyvenv 与 virtualenv 功能和用法类似。不同点在于：
  - 1: pyvenv 只支持 Python 3.3 及更高版本，而 virtualenv 同时支持 Python 2.x 和 Python 3.x；
  - 2: pyvenv 是 Python 3.x 自带的工具，不需要安装，而 virtualenv 是第三方工具，需要安装;
  - 3: pyvenv 实际上是 Python 3.x 的一个模块 venv，等价于 python -m venv
- pyvenv 的用法和 virtualenv 类似:

```bash
# 创建虚拟环境 myenv
pyvenv /path/to/myenv
# 或者
python -m venv /path/to/myenv
# 切换到虚拟环境 myenv，此时命令提示符前会有 (myenv) 提示符
cd /path/to/myenv/ && source bin/activate
# 安装库，安装到 /path/to/myenv/lib 中，不会与其他虚拟环境冲突
pip install requests
# 执行 python 相关命令
python demo.py
# 退出虚拟环境
deactivate
```

## 3：pyenv

### 3.1 pyenv 管理多个 python 版本

- 与上述两个工具不同，pyenv 不是用来管理同一个库的多个版本，而是用来管理一台机器上的多个 Python 版本。主要解决开发中有的项目需要用 Python 2.x，有的项目需要用 Python 3.x 的场景。

- 网上有很多教程，讲如何在一台机器上同时安装 2.x 和 3.x 两个版本，使用时分别用 python、python3 区分。但是这种方法有几个明显的缺点：
  安装麻烦：源码手动安装，可能需要手动指定安装路径，创建软连接等；
  2.x 和 3.x 分别只能安装一个版本：例如不能同时安装 2.6 和 2.7；
  需要人工确定项目使用的 Python 版本，指定错误会导致运行报错。
- pyenv 支持在一台机器上同时安装 cpython（平时说的 Python）、jython、anaconda、micropython、miniconda、pypy、stackless 等等的任意当前可用版本，例如可以同时安装 Python 2.6.9、2.7.15、3.6.6、3.8-dev 几个版本。
- pyenv 使用了垫片的原理，可以做到进入项目目录自动选择 Python 版本，使用极为方便，这也是我目前正在使用的工具

- pyenv 的使用方法:

```bash
# 安装 pyenv（推荐方法，此脚本会自动安装若干插件，包括下文即将提到的 pyenv virtualenv）
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
curl https://pyenv.run | bash

pyenv --version # 查看pyenv版本
pyenv update # 升级


pyenv versions # 本地可用可用python版本
pyenv install -list # 查看所有可用的Python版本
pyenv install 3.7.0 # 安装指定版本
pyenv uninstall 3.7.0  # 卸载指定版本

pyenv version # 当前活动的Python版本
pyenv shell 3.7.0 # 当前shell
pyenv local 3.7.0 # 当前目录
pyenv global 3.7.0 # 全局

pyenv shell --unset # 取消设置
pyenv local --unset # 取消设置
pyenv global --unset # 取消设置


```

### 3.2 pyenv virtualenv

- pyenv 引入了了 virtualenv 插件，可以在 pyenv 中解决同一个库的版本管理问题;
- 通过 pyenv virtualenv 命令，可以与 virtualenv 类似的创建、使用虚拟环境。但由于 pyenv 的垫片功能，使用虚拟环境跟使用 Python 版本的体验一样，不需要手动执行 activate 和 deactivate，只要进入目录即生效，离开目录即失效;
- pyenv virtualenv 的用法和 pyenv 类似（使用上述安装 pyenv 方法会自动安装 virtualenv 插件）：

```bash
# 分别安装基于 Python 2.7.17 和 Python 3.8.2 的虚拟环境
pyenv virtualenv 2.7.17 venv2
pyenv virtualenv 3.8.2 venv3
# 指定全局使用虚拟环境 venv2
pyenv global venv2
# 指定 myproject 使用虚拟环境 venv3
cd myproject
pyenv local venv3
# 在当前 shell 中临时使用虚拟环境 venv3
pyenv shell venv3

```
