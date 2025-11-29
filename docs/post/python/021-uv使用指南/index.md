
# uv使用指南

## 1: Introduction
- uv 是一款用 Rust 开发的高性能 Python 包管理器，旨在统一和简化 Python 的包管理、项目管理和环境管理流程,
- 核心功能对比

|功能领域|传统工具|uv对应命令|备注|
|:---|:---|:---|:---|
|包管理|pip, pip-tools|`uv pip install`||
|虚拟环境|virtualenv|`uv venv`||
|依赖锁定|pip-compile + requirements.txt|自动生成 uv.lock||
|Python版本管理|pyenv|`uv python install`||


## 2：uv的优势
- 极致的速度：得益于 Rust 的实现、并行网络请求和智能缓存，uv 在依赖解析和包安装速度上相比传统工具（如 pip 和 Poetry）有显著提升。
- 功能全面集成：它将 Python 项目开发中常用的多种工具功能集成于一身，你不再需要频繁在 pip、virtualenv、pipx 等工具间切换。
- 符合 Python 标准：uv 的项目管理基于 pyproject.toml 文件，遵循 PEP 621 标准，并支持生成跨平台的锁文件 uv.lock，保证了项目在不同环境下依赖的一致性。
- uv 提供了更强大的依赖管理功能，可以自动解析和安装依赖，避免手动安装和管理依赖的麻烦。

## 3：安装与配置uv
### 3.1 安装uv
```bash
# 在某些计算集群或受限环境中，默认安装路径可能不合适。你可以通过设置环境变量 UV_INSTALL_DIR 来自定义安装目录，并通过 INSTALLER_NO_MODIFY_PATH=1 阻止其自动修改 shell 配置文件

# macOS 和 Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
choco install uv

# pip 
pip install uv

# 验证
uv --version
```

### 3.2 配置uv镜像源

```bash
# 项目级配置(推荐): 在项目的 pyproject.toml 文件中添加

[[tool.uv.index]]
url = 'https://mirrors.aliyun.com/pypi/simple'
default=true
```

## 4: uv核心功能与常用命令
### 4.1 项目管理与依赖管理
```bash
# uv 可以帮你初始化项目、添加依赖并自动生成锁文件
# 1：初始化新项目
mkdir my_project && cd my_project
uv init #这会在当前目录生成一个基本的 pyproject.toml 文件
# 2：添加依赖
uv add requests          # 添加生产依赖
uv add pytest --dev      # 添加开发依赖
uv add -r requirements.txt # 从现有requirements.txt文件导入
# 这些命令会自动更新 pyproject.toml 并安装相应的包

# 3：同步依赖与运行项目
uv sync                  # 安装所有依赖并创建/更新锁文件
uv run python main.py    # 在项目专属环境中运行命令，无需手动激活虚拟环境
uv run python main.py --lock

```
### 4.2 虚拟环境管理

```bash         
# 1: 创建虚拟环境
uv venv                 # 在当前目录创建 .venv 虚拟环境
uv venv --python 3.12 my_env  # 创建指定Python版本和名称的环境

# 2: 列出所有虚拟环境
uv venv list

# 3: 激活虚拟环境
source .venv/bin/activate
.venv\Scripts\activate # Windows
uv venv activate my_env

# 4: 删除虚拟环境
uv venv delete my_env

```

### 4.3 工具管理(uv tool)
- 类似于 pipx，uv tool 用于在隔离环境中安装和运行 Python 命令行工具
```bash
uv tool install ruff              # 安装代码检查工具 ruff
uv tool run ruff check .          # 直接运行工具
uv tool run ruff check .          # 也可使用别名 uvx

```
### 4.4 Python版本管理
#### 4.4.1 安装和使用特定 Python 版本
- uv 可以直接安装和管理多个版本的 Python 解释器，替代 pyenv。
```bash
uv python install 3.12    # 安装 Python 3.12
uv python list            # 列出已安装的 Python 版本
uv venv --python 3.12     # 使用指定版本创建虚拟环境

```
#### 4.4.2 uv进阶使用技巧

```bash
# 依赖数分析
uv tree

# 依赖锁定与同步
uv lock --upgrade-package numpy  # 仅升级指定包
uv sync --force                  # 强制同步环境，即使本地有修改

# 单文件脚本依赖管理: uv 支持基于 PEP 723 标准的单文件 Python 脚本，可以在脚本内部通过注释块声明依赖

uv init --script myscript.py  # 初始化一个脚本文件
uv add --script myscript.py rich #为脚本添加依赖，uv 会自动在脚本顶部生成依赖元数据
uv run myscript.py 运行脚本，uv #会自动处理这些依赖
```
