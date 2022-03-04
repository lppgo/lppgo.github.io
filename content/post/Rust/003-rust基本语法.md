---
title: "01-Rust基本语法"
author: "lucas"
draft: false
date: 2021-04-27
lastmod: 2021-04-27

tags: # 文章所属标签
  ["Rust"]
categories: # 文章所属目录
  ["Rust"]
keywords: # 文章关键词
  ["Rust"]
---

- [rust 基本语法](#rust-基本语法)
  - [1: 变量](#1-变量)
  - [2: float 类型](#2-float-类型)
  - [3: 复合类型:tuple 元组，arrary,slice](#3-复合类型tuple-元组arraryslice)
  - [4: 字符串](#4-字符串)
  - [5: 条件分支](#5-条件分支)
  - [6: 循环语句](#6-循环语句)
  - [7: 所有权 ownership](#7-所有权-ownership)
    - [7.1 所有权---变量](#71-所有权---变量)
    - [7.2 所有权---函数参数](#72-所有权---函数参数)
    - [7.3 所有权---函数返回值](#73-所有权---函数返回值)
  - [8: 引用 Reference 和租借 Borrow](#8-引用-reference-和租借-borrow)
  - [9: 悬挂引用 Dangling Reference](#9-悬挂引用-dangling-reference)
  - [10: Struct](#10-struct)
  - [11: 枚举类型 enum](#11-枚举类型-enum)
  - [12: ...](#12-)

# rust 基本语法

## 1: 变量

```rust
   fn f0(){
    println!("--------变量-----------");
    let a=12;
    let b =100;
    println!("a is {1},b is {0}",a,b);
    println!("{}","{}");
    println!("add(): {}",add(a, b));

    // 变量重新赋值
    let mut c=5;
    println!("c is  首次声明:{0}",c);
    c = 66;
    println!("c is  重新赋值:{0}",c);

    // 变量重新绑定,变量的值可以"重新绑定"，但在"重新绑定"以前不能私自被改变
    // 重影（Shadowing）
    let a :i32=11;
    println!("a is重新绑定{}",a) ;


    // 常量
    const D: i32 = 99;
    println!("常量D:{0}",D);

    //
    let a:u64 =123;
    println!("a is重新绑定{}",a);

    // 重影（Shadowing）
    // 重影与可变变量的赋值不是一个概念，重影是指用同一个名字重新代表另一个
    // 变量实体，其类型、可变属性和值都可以变化。但可变变量赋值仅能发生值的变化。
    let x =5;
    let x=x+1;
    let x=x*2;
    println!("the value of x is:{}",x);
}

// rust 不支持自动返回值类型判断
// 如果没有明确函数返回值类型，函数将被认为是"纯过程“,不允许产生返回值，return不能有返回值表达式
fn add(a:i32,b:i32)->i32{
    return a+b
}
```

## 2: float 类型

```rust
fn f1(){
    println!("--------float类型-----------");

    let x =2.0; //f64
    let y: f32 = 3.0;//f32

    println!("x is {0},y is {1}",x,y);

    let mut ok  =true;
    println!("ok is {}",ok);
    ok=false;
    println!("ok is {}",ok);
}
```

## 3: 复合类型:tuple 元组，arrary,slice

```rust
fn f2(){
    println!("--------复合类型:tuple,array,slice-----------");
    // 复合类型
    // tuple元组 ,用一对()包括的一组数据，可以包含不同种类的数据
    let tup:(i32,f64,u8,char) = (10,9.9,5,'a');
    println!("元组 tup: {} {} {} {}",tup.0,tup.1,tup.2,tup.3);
    println!("元组 tup: {:?}",tup);
    println!("元组 tup: {:?}",tup.3);

    // 数组,用[]包含相同类型的数据
    let a = [1,2,3,4,5]; //a是一个长度为5的数组
    let b = ["go","rust","java"];//b是一个长度是4的字符串数组
    let c: [i32;5] = [1,2,3,4,5];//c是一个长度是5，类型是i32的数组

    println!("数组a 的a[0]元素 : {}",a[0]);
    println!("数组b 的元素: {:?}",b);
    println!("数组c 是长度是{}类型是{}的数组:{:?}",c.len(),"i32",c);

    // slice 切片是对数据值的部分引用
    // 1:字符串切片
    let s = String::from("broadcast");
    let part1 = &s[..5];
    let part2 =&s[5..];
    // 2:对象被部分引用，禁止更改值
    // s.push_str(",aod");//TODO 错误:s被部分引用，禁止修改其值
    println!("字符串切片:{}={}+{}",s,part1,part2);

    // 3:非字符串切片
    // let a=[1,2,3,4,5];
    let patr3 =&a[1..3];
    println!("{}",patr3[0]);
    println!("非字符串切片part3:{:?}",patr3);
}
```

## 4: 字符串

```rust
    fn f3(){
    // rust中的字符串通常指 &str, String
    // rust内部的字符串默认是使用utf-8编码格式的(String和&str),
    // 而内置的char类型是4字节长度的，存储的是Unicode字符，所以Rust里面的字符串不能视为char类型的数组，而更接近u8类型的数组


    // 分的比较清.简单的可以理解为: &str 是分配在栈上, String分配在堆上.
    println!();
    println!();
    println!("--------str String  初始化 ...-----------");

    let mut a = String::from("food"); // 在堆上分配内存
    println!("as_ptr()打印堆内存的地址: {:p}", a.as_ptr()); // 打印堆内存的地址
    println!("&a 打印变量a 在栈上的地址: {:p}", &a); // 打印变量a 在栈上的地址
    println!("{} {}", a.len(),a.capacity()); // 字符串在堆内存中的字节长度, 不是字符长度!!!
    a.reserve(10); // 增加堆的内存长度
    println!("{} {}",a.len(), a.capacity()); // 总字节容量
    // 切片
    let e = &a[1..3];
    println!("切片 e: {:?},len是:{}",e,e.len());


    let str: String = String::new(); // 创建空字符串
    println!("str: {} , len: {}, cap: {}",str,str.len(),str.capacity());
    let str2: String = String::from("hello rust"); // 创建堆内存
    println!("str2: {}",str2);
    let str3: String = String::with_capacity(20); // 创建20字节的空堆内存
    println!("str3: {}, cap: {}",str3,str3.capacity());
    let str4: &'static str = "the tao of rust"; // 静态变量
    println!("str4: {}",str4);
    let str5: String = str4.chars().filter(|c| !c.is_whitespace()).collect(); // .chars() 返回 各字符
    println!("str5: {}",str5);
    let str6: String = str4.to_owned(); // 与 to_string() 基本相同
    println!("str6: {}",str6);
    let str7: String = str4.to_string();
    println!("str7: {}",str7);
    let str: &str = &str4[11..15]; // 取静态字符串的部分内容, 学名 切片 (slice)
    println!("str: {}",str);


    println!("--------字符串增加 ...-----------");
    let mut hello = String::from("hello,");
    hello.push('R');
    hello.push_str("-Rust");
    hello.insert_str(2,"-");
    println!("hello字符串增加1: {}",hello);
    let suffix =String::from("-rust");
    hello=hello+&suffix; //NOTE: +后面的对象要带&
    println!("hello字符串增加2: {}",hello);


    println!("--------字符串遍历 ...-----------");
    let s = String::from("good evening...");
    let s: String = s.chars().enumerate().map(|(i,c)|{
        if i%2 == 0{
            c.to_lowercase().to_string()
        }else{
            c.to_uppercase().to_string()
        }
    }).collect();
    println!("s遍历: {}",s);


    println!("--------字符串位置查询以及子串...-----------");
}
```

## 5: 条件分支

```rust
fn f4(){
    println!("--------条件判断语句...-----------");
    // if
    let a = 12;
    let b;
    if a>0{
        b=1;
    }else if a<0{
        b=-1;
    }else{
        b=0;
    }

    println!("b is {}",b);


    // 三元条件表达式 (A?B:C)
    let a=3;
    let number=if a > 0 {1} else {-1};
    println!("number is {}",number);

    // match  多条件分支
    // TODO match 除了能够对enum类型进行分支选择以外，还可以对整数、浮点数、字符和字符串切片引用（&str）类型的数据进行分支选择。
    // TODO 其中，浮点数类型被分支选择虽然合法，但不推荐这样使用，因为精度问题可能会导致分支错误。
    let n ="abc";
    match n{
        "abc"=>println!("Yes"),
        _=>{},
    }

    // TODO: if let语句
    /*
    if let 匹配值 = 源变量 {
        语句块
    }else{

    }
    */
    enum Book{
        Papery(u32),
        Electronic(String)
    }
    let book=Book::Electronic(String::from("url"));
    if let Book::Papery(index)=book{
            println!("Papery:{}",index);
    }else{
            println!("not papery book");
    }
}
```

## 6: 循环语句

```rust
fn f5(){
    println!("--------循环语句...-----------");
    let mut i: i32;
    i=0;
    while i<4{
        println!("i:{}",i);
        i=i+1;
    }

    let arr=[10,20,30,40,50];
    for i in arr.iter(){ //迭代器 iter(),iter_num()
        println!("for in iter() 遍历: {}",i);
    }

    for i in 0..arr.len(){
        println!("for in 下标 遍历: {}",i);
    }
}
```

## 7: 所有权 ownership

// rust 所有权
// 1: Rust 中的每一个值都有一个变量，称其为所有者；
// 2：一次只能有一个所有者；
// 3：当所有者不在程序的运行范围时，该值将被删除。

### 7.1 所有权---变量

```rust
fn f6(){
    println!("--------所有权---变量...-----------");
    {
    // 在声明以前，变量 s 无效
    let s = "runoob";
    println!("{}",s);
    // 这里是变量 s 的可用范围
    }
    // 变量范围已经结束，变量 s 无效

    // 内存的分配与释放,(heap)
    // rust没有显式的释放资源的步骤，是因为在变量作用域结束的时候，rust编译器自动添加了调用释放资源的步骤

    println!("变量与数据的交互方式：Move,Clone");
    // ----Move移动----
    let x =5;
    let y=x;
    println!("{}",y);
    // 注: 基本数据类型(整形，布尔型，浮点型，字符类型char,包含以上类型的元组),是在stack上分配内存。
    let s1=String::from("hi rust");//字符串是长度不确定类型，需要在堆中存储,栈中存储的是数据的指针s1.
    let s2=s1; // s1已经失效了
    // println!("{}",s1);// 报错:borrow of moved value: `s1`
    println!("s1 move s2 ,s2={}",s2);


    // ----Clone克隆----
    let s1 =String::from("hello");
    let s2=s1.clone();
    println!("s1 clone s2, s1={},s2={}",s1,s2);
}
```

### 7.2 所有权---函数参数

```rust
fn f7(){
    println!("--------所有权---函数参数 ownership-----------");
    let s = String::from("hello"); //s 被声明有效
    take_ownership(s);// s 的值被当作参数传入函数，相当于s已经被移动，从此开始s无效
    println!("s 是String，不是基本类型，作为函数参数被传递，相当于被移动，无效");

    let x =5;// x被声明有效
    make_copy(x);// x的值被当作参数参数函数，但x是基本类型，之后x任然有效
    println!("x:i32 是基本类型，虽然作为函数参数被传递，x依然有效")

    // 函数结束,x 也被释放，无效
}

fn take_ownership(s: String){
    // s 作为参数传入，有效
    println!("{}",s);
    // ...
}   // 函数结束,s 被释放

fn make_copy(i:i32){
    // i 作为参数传入，有效
    println!("i = {}",i);
}
```

### 7.3 所有权---函数返回值

```rust
fn f8(){
    println!("--------所有权---函数返回值-----------");
    let s1 = gives_ownership();//函数返回值移动到s1
    let s2 =String::from("hello");//s2声明有效

    let s3=takes_and_gives_back(s2);//s2作为参数被移动,s3获得返回值所有权

    println!("s1={},s3={}",s1,s3);
}   //s1,s3无效被释放
```

## 8: 引用 Reference 和租借 Borrow

```rust
fn f9(){
    println!("--------引用Reference和租借Borrow-----------");
    let s1 =String::from("reference");
    let s2=&s1; //& 运算符可以取变量的"引用",类似于指针
    // 当一个变量的值被引用时，变量本身不会被认定无效，因为 "引用" 并没有在栈中复制变量的值;
    println!("s1 = {}, s2 = {}",s1,s2);

    // 引用不会获取值的所有权,只能租借Borrow值的所有权
    // 引用本身也是一个类型并具有一个值，这个值记录的是别的值所在的位置


    // TODO 不可变租借borrow
    let s1 = String::from("这是一个不可变的borrow");
    let mut s2 = &s1;
    let s3 = s2;
    s2 = &s3; // 重新从 s3 租借Borrow所有权
    // s2.push_str("has"); 错误，禁止修改租借的值
    println!("{}", s2);

    // TODO 可变租借
    let mut s1 =String::from("这是一个可变的borrow,");
    let s2=&mut s1;
    s2.push_str("abc");
    println!("可变borrow &mut = {}",s2);
}
```

## 9: 悬挂引用 Dangling Reference

/// **悬挂引用 Dangling Reference** 指的是：那种没有实际指向一个真正能访问数据的指针（不一定是空指针，还可能是已释放的资源）  
// Dangling Reference 在 rust 里面不允许出现，编译器会进行检测。

```rust
fn f10(){
    println!("--------悬挂引用Dangling Reference-----------");
    // let reference_to_nonthing =dangling();
}

// fn dangling()->String{
//     let s =String::from("hi,this is dangling reference");
//     &s //NOTE:悬挂引用
//     // 很显然，随着dangling函数的结束，其局部变量s的值本身没有被当作返回值，被释放了，
//     // 它的引用却被返回，这个引用所指向的值已经不确定是否存在，故不允许悬挂引用
// }

```

## 10: Struct

// **struct**
// rust 中 Struct 和 Tuple 元组都可以将若干个不同类型的数据作为一个整体，
// 元组常用于非定义的多值传递，而结构体用于规范常用的数据结构，结构体每个成员叫字段
// 一定要导入调试库 #[derive(Debug)] ，
// 之后在 println 和 print 宏中就可以用 {:?} 占位符输出一整个结构体，
// 如果属性较多的话可以使用另一个占位符 {:#?}

```rust
#[derive(Debug)]
// 定义结构体
struct Site{
    domain:String,
    name:String,
    nation:String,
    found:u32,
}

// 结构体---Method方法。方法和函数与go里面含义相同
impl Site {
    // 定义一个结构体的普通方法
    // &self 是结构体普通方法固定的第一个参数
    fn get_domain(&self,found:u32)->&String{
        println!("get site found:{}",found);
        &self.domain
    }
}
// 结构体---Function函数
impl Site{
    fn toString(s:Site)->String{
        let s =s.domain+&s.name+&s.nation;
        s
    }
}
fn f11(){
    println!();println!();
    println!("--------结构体struct...-----------");
    // 元组结构体
    struct Color(u8,u8,u8);

    let black= Color(0,10,0);
    println!("black元组结构体: black=({}.{},{})",black.0,black.1,black.2);

    // 初始化结构体实例
    let mut web_site =Site{
        domain:String::from("lppgo.github.io"),
        name:String::from("lucas"),
        nation:String::from("china"),
        found: 100
    };

    println!("web_site:{:?}",web_site);
    println!("web_site.domain:{}",web_site.domain);

    // mut 修饰，修改结构体实例
    web_site.found=5000;
    println!("web_site.found:{}",web_site.found);

    // 结构体作为函数参数和返回值

    // method
    println!("struct 调用method :{}",web_site.get_domain(1000));

    // function
    println!("struct 调用function: {}",Site::toString(web_site));

    // 结构体所有权

    // 单元结构体:结构体可以只作为一种象征而无需任何成员
    // struct UnitStruct{}
}
```

## 11: 枚举类型 enum

    // 访问枚举类型的属性 match
    // rust 通过match来实现分支结构

    /*
    match 枚举类实例 {
    分类1 => 返回值表达式,
    分类2 => 返回值表达式,
    ...
    }
    */

```rust
fn f12(){
    println!("--------枚举类型enum...-----------");
    let pbook= Book::Papery{index:10001};
    let ebook =Book::Electronic{url:String::from("www.google.com")};
    println!("枚举类型enum:{:?},{:#?}",pbook,ebook);

    match pbook{
        Book::Papery{index}=>{
            println!("Papery book : {}",index);
        },
        Book::Electronic{url}=>{
            println!("Electronic book : {}",url);
        }
    }

    // Option枚举类
    // Option是Rust标准库中的枚举类，这个引用用于填补rust不支持null引用的空白
    // Rust在语言层面彻底不允许空值 null 的存在，但无奈null 可以高效地解决少量的问题，所以 Rust 引入了 Option 枚举类
    enum Option<T>{
        Some(T),
        None,
    }

    // TODO: 如果你想定一个可以为空值的类，你可以这样:
    let opt=Option::Some("hello,可以为Null");
    // TODO: 如果你想针对opt执行某些操作，你必须先判断它是否是Option::None:
    // 如果初始值为空Option必须明确类型
    match opt{
        Option::Some(sth)=>{
            println!("opt:{}",sth);
        },
        Option::None=>{
            println!("opt is nothing");
        }
    }
    // Option::可以省略

}
```

## 12: ...
