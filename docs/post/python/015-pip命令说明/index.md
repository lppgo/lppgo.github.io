
[toc]

# Table of Contents

# 1：pip 命令说明

## 1.1: 安装 pip

- `python -m pip --version`:

## 1.2: 安装 Python 库

- `pip install requests`: 它会自动处理库及其依赖关系

## 1.3: 升级库

- `pip list --outdated # 查看待升级库`
- `pip upgrade <package_name> # 升级指定库`

## 1.4: 卸载库

- `pip uninstall <package_name>`

## 1.5: 搜索库

- `pip search <keyword>`: 比如查找与机器学习相关的库，你可以输入 pip search machine learning

## 1.6: 查看已安装库详细信息

- `pip show <package_name>`

## 1.7: 只下载库而不安装

- 有时你可能需要离线环境安装包或者备份当前环境的依赖，那么可以使用 download 命令只下载不安装：
- `pip download <package_name>`

## 1.8: 创建 requirements 文件

- 在项目开发中，为了方便团队成员统一环境，我们可以创建一个包含所有依赖的 requirements 文件：
- `pip freeze > requirements.txt`
- 这会列出当前环境中所有已安装库及其版本，并保存到 requirements.txt 文件中。而要根据这个文件安装所有依赖，只需：
- `pip install -r requirements.txt`

## 1.9: 指定库版本安装

- 在某些情况下，你可能需要安装特定版本的库，比如安装 requests 库的 2.25.1 版本
- `pip install requests==2.25.1`

## 1.10: 检查是否存在安全漏洞

- pip 配合 Safety 工具可以检查已安装库的安全性：

  ```python
  pip install safety
  safety check --full-report
  ```

- 这会扫描所有已安装的库，并报告是否有已知的安全漏洞

## 1.11: 创建虚拟环境并激活

- 为了避免不同项目间依赖冲突，我们通常会在每个项目下创建独立的虚拟环境，然后使用 pip 进行管理：
  ```python
  python -m venv my_project_env # 创建虚拟环境
  source my_project_env/bin/activate # Linux/Mac激活环境
  my_project_env\Scripts\activate.bat # Windows激活环境
  ```
- 在虚拟环境中，你可以放心使用 pip 安装和管理项目的专属依赖。

## 1.12: 清理未使用的库或缓存

- `pip-autoremove <package_name>`:
- `pip cache purge`: 清理 pip 下载缓存以释放磁盘空间

## 1.13: 查看 pip 自身的版本信息及更新 pip

- `pip --version`:
- `python -m pip install --upgrade pip`: 升级 pip

## 1.14: 指定源安装库

- 在某些网络环境下，可能需要从国内镜像或者其他自定义源下载和安装库。例如使用阿里云的 Python 镜像源：
- `pip install -i https://mirrors.aliyun.com/pypi/simple/ <package_name>`
- 或永久更改 pip 默认源（推荐在配置文件中修改）：
- `pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/`

## 1.15: 分发本地构建的库

- 如果你自己开发了一个 Python 包，并希望在本地测试安装，可以先打包成 whl 或 tar.gz 格式，然后通过 pip 进行安装：

```python
# 假设你已经将项目打包为my_package-0.1.0.whl
pip install ./my_package-0.1.0.whl
```

## 1.16: 查看库安装路径

- 如果想知道某个库具体安装在系统哪个位置，可以使用 show --files 选项：
- `pip show --files <package_name>`

## 1.17: 在安装时跳过测试

- 有些库在安装过程中会执行单元测试，若想快速安装可选择跳过这些测试：

```python
pip install --no-deps --ignore-installed --no-cache-dir --disable-pip-version-check --no-build-isolation


# 在这个命令中：
--no-deps 表示不安装任何依赖项。
--ignore-installed 表示忽略已安装的包。
--no-cache-dir 表示不使用缓存目录来存储下载的包。
--disable-pip-version-check 表示禁用对 pip 版本的检查。
--no-build-isolation 表示不使用虚拟环境进行构建隔离（不建议在普通的安装过程中使用此选项，但在某些特殊情况下可能有用）。
通过这些参数，您可以快速安装 Python 包，并跳过单元测试。
```

## 1.18: 列出所有全局安装的库

- `pip list`

## 1.19: 在安装时指定额外选项

- 某些库可能在安装时需要额外参数，比如 numpy、scipy 等科学计算库，你可以直接在 pip 命令中传递这些选项：
- `pip install numpy --install-option="--openblas"`

## 1.20: 查看依赖树

- 要了解一个包及其所有依赖关系，可以使用 deptree 第三方工具：

```python
pip install deptree
deptree -l <package_name>
```

- 这将展示指定包及其所有依赖项之间的层级关系。

## 1.21: 修复损坏的库

- 如果某个库在安装或升级过程中出现问题导致无法正常使用，可以尝试修复它：
- `pip install --force-reinstall <package_name>`

## 1.22: 获取库的源码,压缩解压

- 如果你对某个库的实现细节感兴趣，可以通过 pip 下载其源码
- `pip download <package_name> --no-binary :all:`
- 然后在下载目录中找到对应的 tar.gz 或 whl 文件解压查看.
- `tar -xzvf your_package.tar.gz`: 解压 tar.gz
- `tar -czvf your_package.tar.gz /path/to/your_package_directory1  /path/to/your_package_directory2`: 压缩
- `unzip your_package.whl`: 解压.whl 文件

## 1.23: 执行 pip 的自定义脚本

- 有些开发者可能会编写自定义的 pip 脚本来自动化一些任务，你可以通过 run 命令执行：
- `pip run  my_script.py`

## 1.24: 在安装时指定 Python 版本

- 如果你有多个 Python 版本并希望为特定版本安装库：
- `python3.7 -m pip install <package_name>`
- 这里 python3.7 替换成你想要使用的 Python 解释器路径。

## 1.25: 检查依赖冲突

- 在项目中可能存在不兼容的依赖版本，可以使用 pipdeptree 第三方工具来检测

```python
pip install pipdeptree
pipdeptree --packages <package_name>
```

- 这将展示指定包及其依赖项之间是否存在版本冲突。

## 1.26: 创建独立可执行文件

- 借助 pyinstaller 等工具，你可以通过 pip 将 Python 程序打包成一个独立可执行文件:

```python
pip install pyinstaller
pyinstaller your_script.py
```

## 1.27: 管理用户级别的包

- 默认情况下，pip 会安装全局系统级别的包。若想为当前用户安装不影响系统的包，可以加上--user 选项：
- `pip install --user <package_name>`

## 2.28: 只升级指定的包而不升级所有包

- 当只需要更新某个特定的库时，可以使用--upgrade 选项：
- `pip install --upgrade <package_name>`

## 2.29: 批量卸载多个包

- `pip uninstall <package1> <package2> ...`

## 2.30: freeze 冻结当前环境下的所有包及其版本

- 为了能够复制或记录当前环境中所有已安装包的状态，可以生成一个 requirements 文件：
- `pip freeze > requirements.txt`
- 这将把所有已安装包及其版本号写入 requirements.txt 文件中，便于在其他环境下复现相同的软件环境。

## 2.31: 根据 requirements 文件创建虚拟环境并安装包

- 结合虚拟环境（如 venv 或 conda），可以从 requirements 文件重新构建环境：

```python
python -m venv my_venv
source my_venv/bin/activate # Windows: my_venv\Scripts\activate.bat
pip install -r requirements.txt
```
