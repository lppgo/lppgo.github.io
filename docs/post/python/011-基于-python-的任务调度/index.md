
# Table of Contents

- [Table of Contents](#table-of-contents)
- [1：快速安装与应用](#1快速安装与应用)
- [2: 快速安装与应用](#2-快速安装与应用)
- [3: 定时发送邮件](#3-定时发送邮件)
- [4: 使用装饰器进行调度](#4-使用装饰器进行调度)
- [5: 使用参数运行计划任务](#5-使用参数运行计划任务)
- [6:](#6)

# 1：快速安装与应用

- crontab 定时任务

# 2: 快速安装与应用

Python 工具包 **[schedule](https://schedule.readthedocs.io/en/stable/)** 可以轻松地在 Python 中进行任务调度，我们可以通过 PyPI 快速安装它。

- `pip install schedule`
- 借助于 schedule，我们几乎可以像用自然语言说话一样快速构建任务计划和时间表。比如，你想每小时运行一次某个功能函数（比如功能是发邮件的函数 send_email) ，写法是这样的：`schedule.every().hour.do(send_email)`

# 3: 定时发送邮件

```python
import time
import schedule


def send_email():
    # 发送邮件的操作可以加在这里
    print("Sending email...")

# 下面的代码将在每天下午14:45 调用send_email函数
schedule.every().day.at("14:45").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)
```

# 4: 使用装饰器进行调度

- 我们可以使用装饰器让代码更加干净和优雅。schedule 工具包支持开箱即用的装饰器。我们把上面发送电子邮件的示例改用装饰器完成，代码如下
-

```python
import time
from schedule import repeat, every, run_pending


@repeat(every(10).seconds)
@repeat(every(5).seconds)
def send_email():
    # 发送邮件的操作可以加在这里
    print("Sending email...")


while True:
    run_pending()
    time.sleep(1)
```

- 上述代码示例中，我们为同一个任务定制了两个计划。第一个将每 10 秒调用一次功能函数，第二个将每 5 秒调用一次.

# 5: 使用参数运行计划任务

- 我们有时候会希望任务的调用更灵活一些，比如如果可以通过传递参数来控制任务调度，那就免去了写死各种细节的问题。下面我们把发邮件的任务写成可接受参数的形式：

```python
@repeat(every(10).seconds)
@repeat(every(5).seconds, email="showmeai@yeah.net")
def send_email(email="default_email@yeah.net"):
    # 发送邮件的操作可以加在这里
    print(f"Sending email...: to {email}")
```

- 经过上面的简单处理，我们可以把电子邮箱当作参数传递给调度任务。如果我们希望通过命令行参数给脚本传参，一个示例的代码如下：

```python
import argparse

def send_email(email="default_email@yeah.net"):
    # 发送邮件的操作可以加在这里
    print(f"Sending email...: to {email}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", help="Email to send")

    args = parser.parse_args()

    if args.email:
        send_email(args.email)
    else:
        send_email()
```

- 接下来我们就可以在终端中运行上述脚本，如下所示

```python
$ python send_mail.py -e showmeai@yeah.net

# 我们也可以使用默认的邮箱参数
$ python send_email.py
```

# 6:
