
<div align='center' ><font size='50'>Cpp thread用法整理</font></div>

- [1: Cpp thread 多线程](#1-cpp-thread-多线程)
- [2: std::thread 类成员函数](#2-stdthread-类成员函数)
- [3: 创建一个 thread 线程](#3-创建一个-thread-线程)
- [4: mutex 和 std::lock\_guard 的使用](#4-mutex-和-stdlock_guard-的使用)
  - [4.1 mutex](#41-mutex)

# 1: Cpp thread 多线程

- **C++11** 中加入了<**thread**>头文件，此头文件主要声明了`std::thread`线程类。C++11 的标准类`std::thread`对线程进行了封装，定义了 C++11 标准中的一些表示线程的类、用于互斥访问的类与方法等。

# 2: std::thread 类成员函数

- **[get_id]()**: 获取线程 ID，返回一个类型为 std::thread::id 的对象;
- **[joinable]()**: 检查线程是否可被 join。检查当前的线程对象是否表示了一个活动的执行线程。缺省构造的 thread 对象、已经完成 join 的 thread 对象、已经 detach 的 thread 对象都不是 joinable;
- **[join]()**: 调用该函数会阻塞当前线程（主调线程）。阻塞调用者(caller)所在的线程（主调线程）直至被 join 的`std::thread`对象标识的线程（被调线程）执行结束;
- **[detach]()**: 将当前线程对象所代表的执行实例与该线程对象分离，使得线程的执行可以单独进行。一旦线程执行完毕，它所分配的资源将会被释放;
- **[native_handle]()**: 该函数返回与`std::thread`具体实现相关的线程句柄。native_handle_type 是连接 thread 类和操作系统 SDK API 之间的桥梁，如在 Linux g++(libstdc++)里，native_handle_type 其实就是 pthread 里面的 pthread_t 类型，当 thread 类的功能不能满足我们的要求的时候(比如改变某个线程的优先级)，可以通过 thread 类实例的 native_handle()返回值作为参数来调用相关的 pthread 函数达到目录。This member function is only present in class thread if the library implementation supports it. If present, it returns a value used to access implementation-specific information associated to the thread.
- **[swap]()**: 交换两个线程对象所代表的底层句柄;
- **[operator=]()**:moves the thread object;
- **[hardware_concurrency]()**:静态成员函数，返回当前计算机最大的硬件并发线程数目。基本上可以视为处理器的核心数目;
- 另外，`std::thread::id` 表示线程 ID，定义了在运行时操作系统内唯一能够标识该线程的标识符，同时其值还能指示所标识的线程的状态。Values of this type are returned by thread::get_id and this_thread::get_id to identify threads.

- 有时候我们需要在线程执行代码里面对当前调用者线程进行操作，针对这种情况，C++11 里面专门定义了一个命名空间
  - **`this_thread`**，此命名空间也声明在<thread>头文件中，其中包括 get_id()函数用来获取当前调用者线程的 ID；
  - `yield()` 函数（yield，放弃的意思）可以用来将调用者线程跳出运行状态，重新交给操作系统进行调度，即当前线程放弃执行，操作系统调度另一线程继续执行；
  - `sleep_until()`函数是将线程休眠至某个指定的时刻(time point),该线程才被重新唤醒；
  - `sleep_for()`函数是将线程休眠某个指定的时间片(time span)，该线程才被重新唤醒，不过由于线程调度等原因，实际休眠实际可能比 sleep_duration 所表示的时间片更长。

# 3: 创建一个 thread 线程

- 创建线程比较简单，使用 std 的 thread 实例化一个线程对象就创建完成了，示例：

```cpp
#include <iostream>
#include <thread>
#include <stdlib.h> //sleep

using namespace std;

void t1()  //普通的函数，用来执行线程
{
    for (int i = 0; i < 10; ++i)
    {
        cout << "t1111\n";
        sleep(1);
    }
}
void t2()
{
    for (int i = 0; i < 20; ++i)
    {
        cout << "t22222\n";
        sleep(1);
    }
}
int main()
{
    thread th1(t1);  //实例化一个线程对象th1，使用函数t1构造，然后该线程就开始执行了（t1()）
    thread th2(t2);

    th1.join(); // 必须将线程join或者detach 等待子线程结束主进程才可以退出
    th2.join();

    //or use detach
    //th1.detach();
    //th2.detach();

    cout << "here is main\n\n";

    return 0;
}
```

# 4: mutex 和 std::lock_guard 的使用

## 4.1 mutex

https://www.cnblogs.com/haippy/p/3237213.html

- `#include <mutex>`: **mutex**互斥锁是用来保证线程同步的，防止不同的线程同时操作同一个共享数据;
- **四种 mutex 类**:

  - `std::mutex`: 最基本的 mutex 类;
  - `std::recursive_mutex`: 递归 mutex 类;
  - `std::timed_mutex`: 定时的 mutex 类;
  - `std::recursive_timed_mutex`: 定时递归 mutex 类;

- **两种 Lock 类**:

  - `std::lock_guard<>`:但使用 lock_guard 则相对安全，它是基于作用域的，能够自解锁，当该对象创建时，它会像 m.lock()一样获得互斥锁，当生命周期结束时，它会自动析构(unlock)，不会因为某个线程异常退出而影响其他线程 ;
  - `std::unique_lock<>`: ;

- 函数
  - `std::try_lock`，尝试同时对多个互斥量上锁。
  - `std::lock`，可以同时对多个互斥量上锁。
  - `std::call_once`，如果多个线程需要同时调用某个函数，call_once 可以保证多个线程对该函数只调用一次。
