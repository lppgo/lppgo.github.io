
<div align='center' ><font size='50'>Cpp time 示例</font></div>

# 1: time 介绍

- std::chrono::duration
- std::chrono::time_point
- std::chrono::system_clock
- std::chrono::steady_clock
- std::chrono::high_resolution_clock

- std::time_t
- std::tm

# 2: time code

```cpp
#include <chrono>
#include <iostream>
#include <thread>
#include <ctime>
#include <iomanip>

int main() {
    // std::chrono::duration<Rep ,Period> 表示一段时间
    std::chrono::duration<int> time_out_1(3); // time_out 设置为3S
    std::chrono::duration<int, std::ratio<1>> time_out_2(3); // time_out 设置为3S
    std::chrono::duration<int, std::milli> time_out_3(3000); // time_out 设置为3000 ms

    std::chrono::duration<int,std::ratio<1>> sum_duration =
            std::chrono::duration_cast<std::chrono::duration<int>>(time_out_1) +
            std::chrono::duration_cast<std::chrono::duration<int>>(time_out_2) +
            std::chrono::duration_cast<std::chrono::duration<int>>(time_out_3);

    std::cout << "sum_duration = " << sum_duration.count() << " seconds" << std::endl;

    std::chrono::duration<long long,std::ratio<1,1000>> sum_duration_mill =std::chrono::duration_cast<std::chrono::milliseconds>(sum_duration);
    std::cout << "sum_duration_mill = " << sum_duration_mill.count() << " millseconds" << std::endl;

    // std::chrono::time_point<>; 表示时间点
    std::chrono::system_clock::time_point t1=std::chrono::system_clock::now(); // 获取当前时间点
    std::this_thread::sleep_for(std::chrono::seconds(3)); // sleep 3 s
    std::chrono::system_clock::time_point t2=std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_time=t2-t1;

    std::cout << "Start time: " << std::chrono::system_clock::to_time_t(t1) << std::endl;
    std::cout << "End time: " << std::chrono::system_clock::to_time_t(t2) << std::endl;
    std::cout << "Time elapsed: " << elapsed_time.count() << " seconds" << std::endl;


    // std::chrono::system_clock 类提供给了从系统实时时钟上获取当前时间功能。
    // 可以调用std::chrono::system_clock::now()来获取当前的时间

    // std::chrono::steady_clock 能访问系统稳定时钟。
    // 可以通过调用std::chrono::steady_clock::now()获取当前的时间。设备上显示的时间，与使用std::chrono::steady_clock::now()获取的时间没有固定的关系。稳定时钟是无法回调的


    // td::chrono::high_resolution_clock类能访问系统高精度时钟。和所有其他时钟一样，通过调用std::chrono::high_resolution_clock::now()来获取当前时间
    // std::chrono::high_resolution_clock可能是std::chrono::system_clock类或std::chrono::steady_clock类的别名，也可能就是独立的一个类
    // 通过std::chrono::high_resolution_clock具有所有标准库支持时钟中最高的精度，这就意味着使用
    // std::chrono::high_resolution_clock::now()要花掉一些时间。所以，当你再调用std::chrono::high_resolution_clock::now()的时候，需要注意函数本身的时间开销。


    // datetime
    // 获取当前时间点
    auto now=std::chrono::system_clock::now();
    // 将时间点转为时间戳 time_t
    std::time_t time_t_now =std::chrono::system_clock::to_time_t(now);
    // 将时间戳转换为 std::tm 结构体
    std::tm* time_info = std::localtime(&time_t_now);
    std::cout << "Current DateTime: " << std::put_time(time_info, "%Y-%m-%d %H:%M:%S") << std::endl;


    return 0;
}



```
