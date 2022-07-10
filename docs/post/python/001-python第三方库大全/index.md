
- [1：包管理和依赖工具](#1包管理和依赖工具)
- [2：分发](#2分发)
- [3：配置相关的库](#3配置相关的库)
- [4：文件操作相关的库](#4文件操作相关的库)
- [5：日期和时间](#5日期和时间)
- [6：文本处理相关](#6文本处理相关)
  - [6.1 通用](#61-通用)
  - [6.2 slug 化](#62-slug-化)
  - [6.3 解析器](#63-解析器)
  - [6.4 PDF](#64-pdf)
  - [6.5 Markdown](#65-markdown)
- [7：CLI 命令行工具](#7cli-命令行工具)
- [8：生产力工具](#8生产力工具)
- [9：数据库](#9数据库)
  - [9.1 python 实现的数据库](#91-python-实现的数据库)
  - [9.2 数据库驱动](#92-数据库驱动)
    - [9.2.1 MySQL：awesome-mysql](#921-mysqlawesome-mysql)
    - [9.2.2 PostgreSQL](#922-postgresql)
    - [9.2.3 其他关系型数据库](#923-其他关系型数据库)
    - [9.2.4 NoSQL 数据库](#924-nosql-数据库)
- [10：网络编程的库](#10网络编程的库)
- [11：HTTP 相关的库](#11http-相关的库)
- [12：WebSocket 相关的库](#12websocket-相关的库)
- [13： WSGI 服务器](#13-wsgi-服务器)
- [14：Web 框架](#14web-框架)
- [15：RESTful API](#15restful-api)
  - [15.1 Django](#151-django)
  - [15.2 Flask](#152-flask)
  - [15.3 Pyramid](#153-pyramid)
  - [15.4 与框架无关的库](#154-与框架无关的库)
- [16：模板引擎](#16模板引擎)
- [17：队列](#17队列)
- [18：搜索](#18搜索)
- [19：解析 URLs 的库](#19解析-urls-的库)
- [20：进程](#20进程)
- [21：并发和并行](#21并发和并行)
- [22：其他库](#22其他库)
- [23：配置库](#23配置库)
- [24：配置库](#24配置库)
- [25：配置库](#25配置库)

部分转自:https://www.ctq6.cn/python%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93%E5%A4%A7%E5%85%A8/#wsgi-%E6%9C%8D%E5%8A%A1%E5%99%A8

# 1：包管理和依赖工具

- **pip**: python 包和依赖管理工具;
  - https://pypi.org/
- **pip-tools**：保证 Python 包依赖关系更新的一组工具;
- **pipenv**：Python 官方推荐的新一代包管理工具。可以利用 pipenv 来实现同时管理项目中的 python 虚拟环境和相关包依赖。**`pipenv`** 是 python 官方推荐的包管理工具，集成了 **`virtualenv`**、**`pyenv`** 和 **`pip`** 三者的功能于一身；
- **poetry**: 可完全取代 `setup.py` 的包管理工具。
- **conda**：跨平台，Python 二进制包管理工具；
- **Curdling**：管理 Python 包的命令行工具；
- **wheel**：Python 分发的新标准，意在取代 eggs；

# 2：分发

> 打包为可执行文件以便分发。

- **PyInstaller** ：将 Python 程序转换成独立的执行文件（跨平台）。
- **cx_Freeze** ：将 python 程序转换为带有一个动态链接库的可执行文件。
- **dh-virtualenv** ：构建并将 virtualenv 虚拟环境作为一个 Debian 包来发布。
- **Nuitka** ：将脚本、模块、包编译成可执行文件或扩展模块。
- **py2app** ：将 Python 脚本变为独立软件包（Mac OS X）。
- **py2exe** ：将 Python 脚本变为独立软件包（Windows）。
- **pynsist** ：一个用来创建 Windows 安装程序的工具，可以在安装程序中打包 Python 本身。

# 3：配置相关的库

> 用来解析和保存配置的库

- **config** ：logging 模块作者写的分级配置模块。
- **ConfigObj** ：INI 文件解析器，带验证功能。
- **ConfigParser** ：(Python 标准库) INI 文件解析器。
- **profig** ：通过多种格式进行配置，具有数值转换功能。
- **python-decouple** ：将设置和代码完全隔离。

# 4：文件操作相关的库

- **aiofiles** ：基于 asyncio，提供文件异步操作
- **imghdr** ：（Python 标准库）检测图片类型
- **mimetypes** ：（Python 标准库）将文件名映射为 MIME 类型
- **path.py** ：对 os.path 进行封装的模块
- **pathlib** ：（Python3.4+ 标准库）跨平台的、面向对象的路径操作库
- **python-magic** ：文件类型检测的第三方库 libmagic 的 Python 接口
- **Unipath** ：用面向对象的方式操作文件和目录
- **watchdog** ：管理文件系统事件的 API 和 shell 工具

# 5：日期和时间

> 操作日期和时间的类库。

- **arrow** ：更好的 Python 日期时间操作类库。
- **Chronyk** ：Python 3 的类库，用于解析手写格式的时间和日期。
- **dateutil** ：Python datetime 模块的扩展。
- **delorean** ：解决 Python 中有关日期处理的棘手问题的库。
- **maya** ：人性化的时间处理库。
- **moment** ：一个用来处理时间和日期的 Python 库。灵感来自于 Moment.js。
- **pendulum** ：一个比 arrow 更具有明确的，可预测的行为的时间操作库。
- **PyTime** ：一个简单易用的 Python 模块，用于通过字符串来操作日期/时间。
- **pytz** ：现代以及历史版本的世界时区定义。将时区数据库引入 Python。
- **when.py** ：提供用户友好的函数来帮助用户进行常用的日期和时间操作。

# 6：文本处理相关

> 用于解析和操作文本的库。

## 6.1 通用

- **chardet** ：字符编码检测器，兼容 Python2 和 Python3。
- **difflib** ：(Python 标准库)帮助我们进行差异化比较。
- **ftfy** ：让 Unicode 文本更完整更连贯。
- **fuzzywuzzy** ：模糊字符串匹配。
- **Levenshtein** ：快速计算编辑距离以及字符串的相似度。
- **pangu.py** ：在中日韩语字符和数字字母之间添加空格。
- **pypinyin**：汉字拼音转换工具 Python 版。
- **shortuuid** ：一个生成器库，用以生成简洁的，明白的，URL 安全的 UUID。
- **simplejson** ：Python 的 JSON 编码、解码器。
- **unidecode** ：Unicode 文本的 ASCII 转换形式 。
- **uniout** ：打印可读的字符，而不是转义的字符串。
- **xpinyin** ：一个用于把汉字转换为拼音的库。
- **yfiglet-figlet** ：pyfiglet -figlet 的 Python 实现。
- **flashtext** : 一个高效的文本查找替换库。
- **tablib**：Tablib 是一个格式无关的表格数据集库，用 Python 编写。
- **yaml**
  - **`PyYAML`**：Python 版本的 YAML 解析器
- **csv**
  - **`csvkit`**：用于转换和操作 CSV 的工具

## 6.2 slug 化

- **awesome-slugify** ：一个 Python slug 化库，可以保持 Unicode。
- **python-slugify** ：Python slug 化库，可以把 unicode 转化为 ASCII。
- **unicode-slugify** ：一个 slug 工具，可以生成 unicode slugs ,需要依赖 Django 。

## 6.3 解析器

- **phonenumbers** ：解析，格式化，储存，验证电话号码。
- **PLY** ：lex 和 yacc 解析工具的 Python 实现。
- **Pygments** ：通用语法高亮工具。
- **pyparsing** ：生成通用解析器的框架。
- **python-nameparser** ：把一个人名分解为几个独立的部分。
- **python-user-agents** ：浏览器 user agent 解析器。
- **sqlparse** ：一个无验证的 SQL 解析器。

## 6.4 PDF

- **PDFMiner** ：一个用于从 PDF 文档中抽取信息的工具。
- **PyPDF2** ：一个可以分割，合并和转换 PDF 页面的库。
- **ReportLab** ：快速创建富文本 PDF 文档。

## 6.5 Markdown

- **Mistune** ：快速并且功能齐全的纯 Python 实现的 Markdown 解析器。
- **Python-Markdown** ：John Gruber’s Markdown 的 Python 版实现。
- **Python-Markdown2** ：纯 Python 实现的 Markdown 解析器，比 Python-Markdown 更快，更准确

# 7：CLI 命令行工具

- **`asciimatics`** ：跨平台，全屏终端包（即鼠标/键盘输入和彩色，定位文本输出），完整的复杂动画和特殊效果的高级 API。
- **`cement`** ：Python 的命令行程序框架。
- **`click`** ：一个通过组合的方式来创建精美命令行界面的包。
- **`cliff`** ：一个用于创建命令行程序的框架，可以创建具有多层命令的命令行程序。
- **`clint`** ：Python 命令行程序工具。
- **`colorama`** ：跨平台彩色终端文本。
- **`docopt`** ：Python 风格的命令行参数解析器。
- **`Gooey`** ：一条命令，将命令行程序变成一个 GUI 程序。
- **`python-prompt-toolkit`** ：一个用于构建强大的交互式命令行程序的库。
- **`python-fire`** ：Google 出品的一个基于 Python 类的构建命令行界面的库。
- **`Pythonpy`** ：在命令行中直接执行任何 Python 指令。

# 8：生产力工具

- **`aws-cli`** ：Amazon Web Services 的通用命令行界面。
- **`bashplotlib`** ：在终端中进行基本绘图。
- **`caniusepython3`** ：判断是哪个项目妨碍你你移植到 Python3。
- **`cookiecutter`** ：从 cookiecutters（项目模板）创建项目的一个命令行工具。
- **`doitlive`** ：一个用来在终端中进行现场演示的工具。
- **`pyftpdlib`** ：一个速度极快和可扩展的 Python FTP 服务库。
- **`howdoi`** ：通过命令行获取即时的编程问题解答。
- **`httpie`** ：一个命令行 HTTP 客户端，cURL 的替代品，易用性更好。
- **`PathPicker`** ：从 bash 输出中选出文件。
- **`percol`** ：向 UNIX shell 传统管道概念中加入交互式选择功能。
- **`SAWS`** ：一个加强版的 AWS 命令行。
- **`thefuck`** ：修正你之前的命令行指令。
- **`mycli`** ：一个 MySQL 命令行客户端，具有自动补全和语法高亮功能。
- **`pgcli`** ：Postgres 命令行工具，具有自动补全和语法高亮功能。
- **`try`** ：一个从来没有更简单的命令行工具，用来试用 python 库。

# 9：数据库

## 9.1 python 实现的数据库

- **`pickleDB`** ：一个简单，轻量级键值储存数据库。
- **`PipelineDB`** ：流式 SQL 数据库。
- **`TinyDB`** ：一个微型的，面向文档型数据库。
- **`ZODB`** ：一个 Python 原生对象数据库。一个键值和对象图数据库。

## 9.2 数据库驱动

### 9.2.1 MySQL：awesome-mysql

- **`aiomysql`** ：基于 asyncio 的异步 MySQL 数据库操作库。
- **`mysql-python`** ：Python 的 MySQL 数据库连接器。
- **`ysqlclient`** ：mysql-python 分支，支持 Python 3。
- **`oursql`** ：一个更好的 MySQL 连接器，支持原生预编译指令和 BLOBs。
- **`PyMySQL`** ：纯 Python MySQL 驱动，兼容 mysql-python。

### 9.2.2 PostgreSQL

- **`psycopg2`** ：Python 中最流行的 PostgreSQL 适配器。
- **`queries`** ：psycopg2 库的封装，用来和 PostgreSQL 进行交互。
- **`txpostgres`** ：基于 Twisted 的异步 PostgreSQL 驱动。

### 9.2.3 其他关系型数据库

- **`apsw`** ：另一个 Python SQLite 封装。
- **`dataset`** ：在数据库中存储 Python 字典
- **`pymssql`** ：一个简单的 Microsoft SQL Server 数据库接口。

### 9.2.4 NoSQL 数据库

- **`asyncio-redis`** ：基于 asyncio 的 redis 客户端 (PEP 3156)。
- **`cassandra-python-driver`** ：Cassandra 的 Python 驱动。
- **`HappyBase`** ：一个为 Apache HBase 设计的，对开发者友好的库。
- **`Plyvel`** ：一个快速且功能丰富的 LevelDB 的 Python 接口。
- **`py2neo`** ：Neo4j restful 接口的 Python 封装客户端。
- **`pycassa`** ：Cassandra 的 Python Thrift 驱动。
- **`PyMongo`** ：MongoDB 的官方 Python 客户端。
- **`redis-py`** ：Redis 的 Python 客户端。
- **`telephus`** ：基于 Twisted 的 Cassandra 客户端。
- **`txRedis`** ：基于 Twisted 的 Redis 客户端。

# 10：网络编程的库

- **`asyncio`** ：(Python 标准库) 异步 I/O, 事件循环, 协程以及任务。
- **`Twisted`** ：一个事件驱动的网络引擎。
- **`pulsar`** ：事件驱动的并发框架。
- **`diesel`** ：基于 Greenlet 的事件 I/O 框架。
- **`pyzmq`** ：一个 ZeroMQ 消息库的 Python 封装。
- **`Toapi`** ：一个轻巧，简单，快速的 Flask 库，致力于为所有网站提供 API 服务。
- **`txZMQ`** ：基于 Twisted 的 ZeroMQ 消息库的 Python 封装。

# 11：HTTP 相关的库

- **`aiohttp`** ：基于 asyncio 的异步 HTTP 网络库。
- **`requests`** ：人性化的 HTTP 请求库。
- **`grequests`** ：requests 库 + gevent ，用于异步 HTTP 请求.
- **`httplib2`** ：全面的 HTTP 客户端库。
- **`treq`** ：类似 requests 的 Python API 构建于 Twisted HTTP 客户端之上。
- **`urllib3`** ：一个具有线程安全连接池，支持文件 post，清晰友好的 HTTP 库。

# 12：WebSocket 相关的库

- **`AutobahnPython`** ：给 Python 、使用的 WebSocket & WAMP 基于 Twisted 和 asyncio。
- **`Crossbar`** ：开源统一应用路由(Websocket & WAMP for Python on Autobahn)。
- **`django-socketio`** ：给 Django 用的 WebSockets。
- **`WebSocket-for-Python`** ：为 Python2/3 以及 PyPy 编写的 WebSocket 客户端和服务器库。

# 13： WSGI 服务器

> 兼容 WSGI 的 web 服务器

- **`gunicorn`** ：Pre-forked, 部分是由 C 语言编写的。
- **`uwsgi`** ：uwsgi 项目的目的是开发一组全栈工具，用来建立托管服务， 由 C 语言编写。
- **`bjoern`** ：异步，非常快速，由 C 语言编写。
- **`fapws3`** ：异步 (仅对于网络端)，由 C 语言编写。
- **`meinheld`** ：异步，部分是由 C 语言编写的。
- **`netius`** ：异步，非常快速。
- **`paste`** ：多线程，稳定，久经考验。
- **`rocket`** ：多线程。
- **`waitress`** ：多线程, 是它驱动着 Pyramid 框架。
- **`Werkzeug`** ：一个 WSGI 工具库，驱动着 Flask ，而且可以很方便大嵌入到你的项目中去。

# 14：Web 框架

- **`Django`** ：Python 界最流行的 web 框架。
- **`Flask`** ：一个 Python 微型框架。
- **`pyramid`** ：一个小巧，快速，接地气的开源 Python web 框架。
- **`Bottle`** ：一个快速小巧，轻量级的 WSGI 微型 web 框架。
- **`CherryPy`** ：一个极简的 Python web 框架，服从 HTTP/1.1 协议且具有 WSGI 线程池。
- **`TurboGears`** ：一个可以扩展为全栈解决方案的微型框架。
- **`Tornado`** ：一个 web 框架和异步网络库。
- **`sanic`** ：基于 Python3.5+ 的异步网络框架。
- **`starlette`** : 一款轻量级，高性能的 ASGI 框架

# 15：RESTful API

> 用来开发 RESTful APIs 的库

## 15.1 Django

- **`django-rest-framework`** ：一个强大灵活的工具，用来构建 web API。
- **django-tastypie`** ：为 Django 应用开发 API。
- **django-formapi`** ：为 Django 的表单验证，创建 JSON APIs 。

## 15.2 Flask

- **`flask-api`** ：为 flask 开发的，可浏览 Web APIs 。
- **`flask-restful`** ：为 flask 快速创建 REST APIs 。
- **`flask-restless`** ：为 SQLAlchemy 定义的数据库模型创建 RESTful APIs 。
- **`flask-api-utils`** ：为 Flask 处理 API 表示和验证。
- **`eve`** ：REST API 框架，由 Flask, MongoDB 等驱动。

## 15.3 Pyramid

- **`cornice`** ：一个 Pyramid 的 REST 框架 。

## 15.4 与框架无关的库

- **`falcon`** ：一个用来建立云 API 和 web app 后端的高性能框架。
- **`sandman`** ：为现存的数据库驱动系统自动创建 REST APIs 。
- **`restless`** ：框架无关的 REST 框架 ，基于从 Tastypie 学到的知识。
- **`ripozo`** ：快速创建 REST/HATEOAS/Hypermedia APIs。

# 16：模板引擎

> 模板生成和词法解析的库和工具。

- **`Jinja2`** ：一个现代的，对设计师友好的模板引擎。
- **`Chameleon`** ：一个 HTML/XML 模板引擎。模仿了 ZPT（Zope Page Templates）, 进行了速度上的优化。
- **`Genshi`** ：Python 模板工具，用以生成 web 感知的结果。
- **`Mako`** ：Python 平台的超高速轻量级模板。

# 17：队列

> 处理事件以及任务队列的库。

- **`celery`** ：一个异步任务队列/作业队列，基于分布式消息传递。
- **`huey`** ：小型多线程任务队列。
- **`mrq`** ：Mr. Queue -一个 Python 的分布式 worker 任务队列， 使用 Redis 和 gevent。
- **`rq`** ：简单的 Python 作业队列。
- **`simpleq`** ：一个简单的，可无限扩张的，基于亚马逊 SQS 的队列。

# 18：搜索

> 对数据进行索引和执行搜索查询的库和软件。

- **`django-haystack`** ：Django 模块化搜索。
- **`elasticsearch-py`** ：Elasticsearch 的官方底层 Python 客户端。
- **`elasticsearch-dsl-py`** ：Elasticsearch 的官方高级 Python 客户端。
- **`solrpy`** ：solr 的 Python 客户端。
- **`Whoosh`** ：一个快速的纯 Python 搜索引擎库。

# 19：解析 URLs 的库

- **`furl`** ：一个让处理 URL 更简单小型 Python 库。
- **`purl`** ：一个简单的，不可变的 URL 类，具有简洁的 API 来进行询问和处理。
- **`pyshorteners`** ：一个纯 Python URL 缩短库。
- **`shorturl`** ：生成短小 URL 和类似 bit.ly 短链的 Python 实现。
- **`webargs`** ：一个解析 HTTP 请求参数的库，内置对流行 web 框架的支持，包括 Flask, Django, Bottle, Tornado 和 Pyramid。

# 20：进程

> 操作系统进程启动及通信库。

- **`envoy`** ：比 Python subprocess 模块更人性化。
- **`sarge`** ：另一 种 subprocess 模块的封装。
- **`sh`** ：一个完备的 subprocess 替代库。

# 21：并发和并行

> 用以进行并发和并行操作的库。

- **`multiprocessing`** ：(Python 标准库) 基于进程的“线程”接口。
- **`threading`** ：(Python 标准库)更高层的线程接口。
- **`eventlet`** ：支持 WSGI 的异步框架。
- **`gevent`** ：一个基于协程的 Python 网络库，使用 greenlet。
- **`Tomorrow`** ：用于产生异步代码的神奇的装饰器语法实现。
- **`uvloop`** ：在 libuv 之上超快速实现 asyncio 事件循环

# 22：其他库

# 23：配置库

# 24：配置库

# 25：配置库
