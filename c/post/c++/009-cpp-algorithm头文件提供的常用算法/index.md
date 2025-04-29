
<div align='center' ><font size='50'>Cpp标准库中的<algorithm>头文件提供的常用算法</font></div>

# 1: <algorithm> 介绍

- 在 c++中, `<algorithm>` 头文件提供了一系列用于操作序列（如 array，vector,列表 list）的算法；
- 这些算法可以极大的帮助我们简单高效的处理数据，提高代码的可读性和可维护性；

# 2: 查找算法 search

## 2.1 std::find

- `std::find` 是一个线性查找算法，用于在序列中查找特定元素；

```c++
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    int val = 3;

    // 使用std::find查找val在vec中的位置
    auto it = std::find(vec.begin(), vec.end(), val);
    if (it != vec.end()) {
        std::cout << "找到元素 " << val << " 在位置 " << std::distance(vec.begin(), it) << std::endl;
    } else {
        std::cout << "未找到元素 " << val << std::endl;
    }
    return 0;
}
```

## 2.2 std::find_if

- `std::find_if` 允许你根据特定条件在序列中查找元素；

```c++
#include <algorithm>
#include <vector>
#include <iostream>

bool is_even(int i) {
    return (i % 2) == 0;
}

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // 使用std::find_if查找第一个偶数元素
    auto it = std::find_if(vec.begin(), vec.end(), is_even);

    if (it != vec.end()) {
        std::cout << "找到第一个偶数 " << *it << " 在位置 " << std::distance(vec.begin(), it) << std::endl;
    } else {
        std::cout << "未找到偶数" << std::endl;
    }
    return 0;
}

```

# 3: 排序算法 sort

## 3.1 std::sort

- `std::sort` 是一个高效的排序算法，通常实现为快速排序、堆排序或归并排序的混合体;

```c++
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {5, 2, 3, 1, 4};

    // 使用std::sort对vec进行排序
    std::sort(vec.begin(), vec.end());

    // 输出排序后的向量
    for (int i : vec) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## 3.2 std::stable_sort

- `std::stable_sort` 是一种稳定的排序算法，即相等元素的相对顺序在排序后保持不变;
- `std::stable_sort` 用法与 std::sort 类似，但保证排序的稳定性。

# 4: 修改序列算法

## 4.1 std::for_each

- std::for_each 用于对序列中的每个元素执行特定操作;

```c++
#include <algorithm>
#include <vector>
#include <iostream>

void print(int i) {
    std::cout << i << " ";
}

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // 使用std::for_each打印vec中的每个元素
    std::for_each(vec.begin(), vec.end(), print);
    std::cout << std::endl;
    return 0;
}
```

## 4.1 std::transform

- `std::transform` 用于对序列中的每个元素执行某种转换，并将结果存储到另一个序列中;

```c++
#include <algorithm>
#include <vector>
#include <iostream>
#include <functional> // 为了使用std::plus等函数对象

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::vector<int> result(vec.size());

    // 使用std::transform将vec中的每个元素加倍并存储到result中
    std::transform(vec.begin(), vec.end(), result.begin(), [](int x) { return x * 2; });

    // 输出转换后的结果向量
    for (int i : result) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

# 5: 其他常见算法

## 5.1 std::unique_copy

- `std::unique_copy`算法用于从一个输入序列中复制不重复的元素到一个输出序列。这个算法假定输入序列是已排序的，因为只有已排序的序列才能保证相邻的重复元素被识别并去除
- 先排序；

```c++
#include <algorithm>
#include <vector>
#include <iostream>
#include <iterator>

int main() {
    std::vector<int> source = {1, 2, 2, 3, 4, 4, 4, 5};
    std::vector<int> destination;

    // 注意：在这个例子中，std::back_inserter是一个插入迭代器，它将新元素添加到destination容器的末尾
    std::unique_copy(source.begin(), source.end(), std::back_inserter(destination));

    // 输出目标向量，应不包含重复的元素
    for (int val : destination) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

## 5.2 std::merge

- std::merge 算法用于合并两个已排序的序列，结果也是一个已排序的序列;

```c++
#include <algorithm>
#include <vector>
#include <iostream>
#include <iterator>

int main() {
    std::vector<int> vec1 = {1, 3, 5, 7};
    std::vector<int> vec2 = {2, 4, 6, 8};
    std::vector<int> result(vec1.size() + vec2.size());

    std::merge(vec1.begin(), vec1.end(), vec2.begin(), vec2.end(), result.begin());

    // 输出合并后的结果向量
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

## 5.3 集合算法：std::set_difference, std::set_intersection, std::set_union, std::set_symmetric_difference

- 这些算法用于在两个已排序的序列之间执行集合操作。
- `std::set_difference`：计算两个已排序范围的差集。
- `std::set_intersection`：计算两个已排序范围的交集。
- `std::set_union`：计算两个已排序范围的并集。
- `std::set_symmetric_difference`：计算两个已排序范围的对称差集（即属于第一个范围但不属于第二个范围，以及属于第二个范围但不属于第一个范围的所有元素）。
- 对于其他集合算法，使用方法是类似的，只是调用的函数名不同，以及它们处理集合运算的方式不同。这些算法在处理大量数据时可以显著提高效率，因为它们都利用了输入数据已排序的特性来优化性能

# 6 其他值得注意的算法

- 除了之前提到的算法外，C++标准库还提供了许多其他有用的算法，这些算法在处理各种编程任务时都非常实用。

## 6.1. std::partition 和 std::stable_partition

std::partition 和 std::stable_partition 算法用于根据给定谓词对序列进行划分，使得满足谓词的元素出现在不满足谓词的元素之前。std::stable_partition 还保持了等价元素的相对顺序。

## 6.2. std::nth_element

std::nth_element 算法用于对序列进行部分排序，使得第 n 个位置的元素在排序后处于它在完全排序序列中的位置，且该位置左边的所有元素都小于或等于它，右边的所有元素都大于或等于它。

## 6.3. std::rotate 和 std::rotate_copy

std::rotate 算法用于将序列中的元素循环左移或右移，而 std::rotate_copy 则在旋转的同时将结果复制到一个新的序列中。

## 6.4. std::remove 和 std::remove_if

std::remove 算法用于从序列中移除所有等于给定值的元素，而 std::remove_if 则根据给定的谓词来移除元素。这两个算法并不实际删除元素，而是将不需要删除的元素移动到序列的前面，并返回一个迭代器指向新的序列末尾。

## 6.5. std::lower_bound 和 std::upper_bound

std::lower_bound 和 std::upper_bound 算法用于在已排序的序列中查找给定值的下界和上界。下界是指不小于给定值的第一个元素，而上界是指大于给定值的第一个元素。

## 6.6. std::inplace_merge

std::inplace_merge 算法用于将两个相邻的已排序序列合并为一个已排序序列。这个算法在需要合并多个已排序子序列时非常有用。

## 6.7. std::includes, std::set_difference, std::set_intersection, 和 std::set_union

这些算法用于执行集合操作，如判断一个集合是否包含另一个集合、计算两个集合的差集、交集和并集等。这些操作在处理集合数据时非常有用。

## 6.8. std::for_each, std::transform, 和 std::accumulate

这些算法用于对序列中的每个元素执行某种操作。std::for_each 对每个元素执行给定的操作，std::transform 将一个序列中的元素转换为另一个序列中的元素，而 std::accumulate 则计算序列中元素的累积和或其他二元操作的累积结果。

总的来说，C++标准库提供了丰富的算法工具，可以帮助开发者更加高效地处理各种数据结构和序列操作任务。这些算法不仅功能强大，而且经过高度优化，能够在各种场景下提供出色的性能表现。
