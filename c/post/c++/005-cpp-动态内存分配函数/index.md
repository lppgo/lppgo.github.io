
<div align='center' ><font size='50'>Cpp 动态内存分配函数</font></div>

- [1: cpp 动态内存分配](#1-cpp-动态内存分配)
- [2: malloc](#2-malloc)
- [3: calloc](#3-calloc)
- [4: realloc](#4-realloc)
- [5: new](#5-new)
- [6: demo.cpp](#6-democpp)
- [7: 总结与比较](#7-总结与比较)

# 1: cpp 动态内存分配

- `void* malloc(unsigned int size);`
- `void* realloc(void *ptr, unsigned int newsize);`
- `void* calloc(size_t numElements, size_t sizeOfElement);`
- `加上一种new关键字，这四个都可以用来向内存申请空间`

# 2: malloc

- `malloc(unsigned int size)`，它可以在内存的堆（Heap）区域申请连续大小为 size 个字节的空间，然后成功的话返回 `void*`指针（C/C++中，`void*`可以被强制转换为其他类型的指针，像 `int*`等等），这个指针是申请这段连续空间的首地址，如果申请失败的话就返回 NULL 指针。

# 3: calloc

- `calloc(unsigned int n, unsigned int size)`，它可以在内存的堆（Heap）区域申请连续 n 个空间，每个空间包含了 size 个字节的大小，也就是总共向内存申请了 n*size 个字节的空间大小，然后成功的话返回 `void*`指针（这列的也是可以被强制转换的），这个指针是申请这段连续空间的首地址，如果申请失败的话就返回 NULL 指针。

# 4: realloc

- `realloc(void *ptr, unsigned int newsize)`，这个的作用是向内存申请一个 newsize 的空间大小。当使用 malloc 申请的内存不够用的时候，就是用 realloc 来进行申请更大的空间，前面的指针 ptr 就是一开始用 malloc 申请所返回的指针。realloc 申请的方式是从内存堆的开始地址高地址查找一块区域，这块区域大于 newsize 的大小，申请成功后将原本的数据从开始到结束一起拷贝到新分配的内存区域，然后将原本 malloc 申请的区域释放掉（注意的是：原来的指针是自动释放的，不需要使用 free 来进行释放）。最后再这块区域的首地址返回。当内存不再使用时，要记得用 free()函数进行释放。

# 5: new

- `new`是 C++提供的关键字，也是操作符，我们可以使用 new 在内存的堆上创建一个对象，在创建对象的时候，new 其实做了以下的操作：在堆上获得一块内存空间->调用构造函数（创建建档的类型变量时除外）->返回正确的指针;
- `char* p = new char(‘e’)：分配1个char类型大小的内存空间；`
- `char* p = new char[5]:   分配5个char类型大小的内存空间`

# 6: demo.cpp

```cpp
#include <iostream>
#include <memory>
#include <cstring>
using namespace std;

/*
C++ 动态内存分配函数

- malloc 是 C/C++ 标准库中的函数，用于在堆上分配指定大小的内存空间，并返回指向该内存空间的指针。
在使用 malloc 分配内存后，需要手动调用 free 函数来释放这块内存空间，以防止内存泄漏。

- calloc 与 malloc 类似，也是用于在堆上分配内存空间的函数，但它会将分配到的内存空间初始化为零。
calloc 接受两个参数，分别是要分配的内存块的数量和每个内存块的大小。
与 malloc 一样，使用 calloc 分配的内存空间也需要通过调用 free 函数来释放。

- realloc 是用于重新分配内存空间大小的函数。它接受两个参数，一个是已经分配的内存空间的指针，
另一个是需要重新分配的内存空间的大小。
realloc 可以用于扩大或缩小已经分配的内存空间，如果新分配的内存空间大小大于原来的内存空间大小，
那么新分配的内存空间中未初始化的部分将保持未定义的值。与 malloc 和 calloc 一样，使用 realloc 分配的内存空间也需要通过调用 free 函数来释放

- new是C++提供的关键字，也是操作符，我们可以使用new在内存的堆上创建一个对象，在创建对象的时候，
new其实做了以下的操作：在堆上获得一块内存空间->调用构造函数（创建建档的类型变量时除外）->返回正确的指针

 */

//
void Malloc_Test(){
  char* ptr = (char*)malloc(20);                  // 向内存堆申请10个char类型的连续空间，并且返回首地址
  cout<<"malloc 指针变量的地址   ："<<&ptr<<endl;
  cout<<"malloc 申请到的空间首地址   ："<<static_cast<void*>(ptr)<<endl;
  strcpy(ptr,"malloc...lucas");                          // 如果你复制strcpy(ptr,"Servenssssssssssssssssssss");c程序就会中断，因为你申请的区域不够放了
  cout<<"malloc 申请到的空间赋值的地址："<<static_cast<void*>(ptr)<<endl;
  free(ptr);
};

//
void Calloc_Test(){
  char* ptr=(char*)calloc(20,sizeof(char));           // 通过calloc申请10个char类型大小的内存空间
  cout<<"calloc 指针变量的地址   ："<<&ptr<<endl;
  cout<<"calloc 申请到的空间首地址时  ："<<static_cast<void*>(ptr)<<endl;
  strcpy(ptr,"calloc...lucas");
  cout<<"calloc 申请到的空间赋值的地址："<<static_cast<void*>(ptr)<<endl;
//   cout<<"malloc 申请到的空间赋值的字符串："<<strlen(ptr)<<endl;
  free(ptr);
};

void Realloc_Test(){
  char *ptr = (char*)malloc(6 * sizeof(char)); // 分配足够的内存来容纳 5 个字符和一个空终止符
  strcpy(ptr,"Serven"); // 将 6 个字符（包括空终止符）复制到分配的内存中
  cout<<"malloc 指针变量的地址   ："<<&ptr<<endl;
  cout<<"malloc 申请到的空间首地址时  ："<<static_cast<void*>(ptr)<<endl;

  char *ptru = (char*)realloc(ptr, 15 * sizeof(char)); // 分配足够的内存来容纳 14 个字符和一个空终止符
  strncpy(ptru,"Hello, Serven", 14); // 最多复制 14 个字符（包括空终止符）到分配的内存中
  ptru[14] = '\0'; // 手动添加空终止符以确保字符串正确终止
  cout<<"realloc 申请到的空间首地址时："<<static_cast<void*>(ptru)<<endl;
  cout<<"realloc 申请到的空间赋值的字符串："<<ptru<<endl;

  //free(ptr); // 无需释放 ptr，因为 realloc 会处理
  free(ptru);
}

int main(){
    cout<<"C++ 动态内存分配函数: malloc,calloc,realloc,new "<<endl;
    Malloc_Test();
    Calloc_Test();
    Realloc_Test();
    return 0;
}
```

# 7: 总结与比较

| **函数**    | **申请区域** | **申请长度** | **是否初始化** | **头文件**            |
| :---------- | :----------- | :----------- | :------------- | :-------------------- |
| **malloc**  | heap         | `size`       | `void*`        | <stdlib.h>/<malloc.h> |
| **calloc**  | heap         | `n * size`   | `void*`        | <stdlib.h>/<malloc.h> |
| **realloc** | heap         | `newsize`    | `void*`        |                       |

- 如果申请调用成功，malloc()和 calloc()函数都会返回所分配的内存空间的首地址；
- free()释放函数时紧跟着 malloc、calloc、realloc，因为它们都是返回 void\*；而 new 使用的时 delete；
- malloc 和 calloc 之间的区别就是：malloc 申请成功后没有初始化，这样会导致一些垃圾数据的存在，calloc 会初始化，将申请到的这一段连续空间初始化为 0，如果是实型数据的话，则会初始化为浮点数的 0；
- malloc、calloc、realloc 三者都是返回 void*，C/C++支持强制转换 void*成其他类型的指针；
- malloc 是在动态存储区域申请分配一块长度为 size 字节的连续区域，并返回这块区域的首地址；calloc 是在动态存储区域申请分配 n 块长度为 size 字节的区域，并返回这块区域的首地址；realloc 是将 ptr 内存大小增大到 newsize 个字节；
- realloc 是从堆上分配内存，在扩大空间的时候会直接在现存的数据后面获得附加的字节，如果空间能够满足的话就扩展，如果不满足的话，那就从堆的开始地址开始寻找，找到第一个足够大的自由块，然后将现有的数据拷贝到新的位置，而老的那一块还是放到堆上。
