# Go学习  
## Go语言优势
- 可直接编译成机器码，不依赖其他库。  
- 静态类型语言  
- 语言层面支持并发  
- 内置runtime，支持垃圾回收  
- 简单易学，Go语言的作者都有C的基因，那么Go自然而然就有了C的基因，那么Go关键字是25个，但是表达能力很强大，几乎支持大多数其他语言见过的特性：继承、重载、对象等  
- 丰富的标准库  
- 内置强大的工具，Go语言里面内置了很多工具链，最好的应该是gofmt工具，自动化格式化代码，能够让团队review变得如此的简单，代码格式一模一样，想不一样都很困难。  
- 跨平台编译  
- 内嵌C支持，Go里面也可以直接包含C代码，利用现有的丰富的C库。  
## Go适合用来做什么  
- 服务器编程  
- 分布式系统，数据库代理器  
- 网络编程  
- 内存数据库  
## 标准命令概述
- build:用于编译给定的代码包或Go语言源码文件及其依赖包。  
- clean:用于清除执行其他Go命令后遗留的目录和文件。  
- doc:用于执行godoc命令以打印指定代码包。  
- env:用于打印go语言环境信息  
- fix:用于执行gotoo fix命令以修正给定代码包的源码文件中包含的过时语法和代码调用。  
- fmt:用于执行gofmt命令以格式化给定代码包中的源码文件。  
- get：用于下载和安装给定代码包及其依赖包  
- list:用于显示给定代码包的信息。  
- run：用于编译并运行给定的命令源码文件。  
- install:编译包文件并编译整个程序。  
- test:用于测试给定的代码包。  
- tool:用于运行Go语言的特殊工具。  
- version:用于显示当前安装的Go语言的版本信息。  

## 第一个Go程序  

```go
package main

import (
    "fmt"
)
func main(){
    fmt.Println("hello world")
}
```
## 关键字
- break
- default 
- func 
- interface
- select
- case 
- defer
- go
- map
- struct
- chan
- else
- goto
- package
- switch
- const
- fallthrough
- if
- range
- type
- continue
- for
- import
- return
- var

>内建常量：
true false iota nil

>内建类型：int int8 int16 int32 int64 uint uint8 uint16 uint32 uint64 uintptr float32 float64 complex128 complex64 bool byte rune string error

>内建函数：make len cap new append copy close delete complex real imag panic recover

## 变量
``` go
var v1 int
var v2 int
//一次定义多个变量
var v3,v4,v5 int

var (
    v10 int
    v11 int
)

var v1 int = 10
var v2 = 10
v3 := 10
var v11,v22,v23 = 1, 2, 3
```


## 基础数据类型

|类型|名称|长度|零值|说明|
|---|---|----|---|---|
|bool|布尔类型|1|false|其值不为真就是假，不可以用数字代表true或false|
|byte|字节型|1|0|uint8别名|
|rune|字符类型|4|0|专用于存储unicode编码，等价于uint32|
|int,uint|整型|4或8|0|32位或64位|
|int8,uint8|整型|1|0|-128~127，0~255|
|int16,uint16|整型|2|0|-32768~32767，0~65535|
|int32,uint32|整型|4|0|-21亿~21亿，0~42亿|
|int64,uint64|整型|8|0||
|float32|浮点型|4|0.0|小数位精确到7位|
|float64|浮点型|8|0.0|小数位精确到15位|
|complex64复数类型|8||||
|complex128复数类型|16||||
|uintptr整型|4或8|||以存储指针的uint32或uint64整数|
|string|字符串|""||utf-8字符串|
## 使用fmt包来格式化字符串  
fmt.Printf()格式字符串：  
|打印格式|含义|
|---|---|
|%%|一个%字面量|
|%b|一个二进制整数值（基数为2），或者是一个用科学计数法表示的指数为2的浮点数|
|%c|字符型。可以把输入的数字按照ASCII码相应转换位对应的字符|
|%e|以科学技术法e表示的浮点数或者复数值|
|%E|以科学计数法E表示的浮点数或者复数值|
|%f|以标准计数法表示的浮点数或者复数值|
|%g|以%e或者%f表示的浮点数或者复数，任何一个以最为紧凑的方式输出|
|%G|以%E或者%f表示的浮点数或者复数，任何一个都以最为紧凑的方式输出|
|%o|一个以八进制表示的数字（基数为8）|
|%p|以十六进制（基数为16）表示的一个值的地址，前缀为0x，字母使用小写的a-f表示|
|%T|使用Go语法输出的值的类型|

## 类型转换  
Go语言中不允许隐式转换，所有类型转换必须显示声明，而且转换只能发生在两种相互兼容的类型之间。

``` go
var ch byte = 97
var a int = int(ch)
```
# 类型别名  
``` go
type bigint int64 // int64类型改名为bigint
var x bigint = 100
type (
    myint int
    mystr string
)
```
## 流程控制
Go语言支持最基本的三种程序运行结构：顺序结构、选择结构、循环结构。
## if语句
**if**
```go
var a int = 3
if a == 3{
    fmt.Println("a==3")
}
//支持一个初始化表达式，初始化子句和条件表达式直接需要用分号分隔
if b := 3; b == 3{
    fmt.Println("b == 3")
}
```
**if...else**
```go
if a := 3; a == 4{

}else{
    fmt.Println("a != 4")
}
```
**switch语句**
Go里面switch默认相当于每个case最后带有break,匹配成功后不会自动向下执行其他case,而是跳出整个switch，但是可以使用fallthrough强制执行后面的case代码：

```go
var score int = 90
switch score{
    case 10:
        fmt.Println("游戏")
    case 80:
        fmt.Println("靓号")
    default:
        fmt.Println("差")
}
```
可以使用任何类型或表达式作为条件语句：

```go
switch s1 := 90; s1{
    case 90:
        fmt.Println("优秀")
    default:
        fmt.Println("一般")
}
var s2 int = 90
switch {
    case s2 >= 90:
        fmt.Println("优秀")
    case s2 >=80
        fmt.Println("发的")
}
```
**循环语句**
for
```go
var i, sum int
for i = 1; i <= 100; i++{
    sum += i
}
fmt.Println("sum =", sum)
```
range
```go
s := "abc"
for i := range s{
    fmt.Printf("%c\n", s[i])
}
for _, c := range s{
    fmt.Println("%c\n", c)
}
```
**跳转语句**
break和continue  
```go
for i := 0; i < 100; i++{
    if 2 == i{
        continue
    }
}
```
goto  
```go
func main(){
    LABEL:
    for i := 0; i < 100; i++{
        for {
            fmt.Println(i)
            goto LABEL
        }
    }
}
```
## 自定义格式
Go语言函数定义格式：
```go
func FuncName(/*参数列表*/) (o1 type1, o2 type2/*返回类型*/){
    //函数体
    return v1, v2
}
```
## 延迟调用defer
defer作用  
关键字defer用于延迟一个函数或者方法的执行  
```go
func main(){
    fmt.Println("this is a test")
    defer fmt.Println("this is a defer")
}
```
**多个defer执行顺序**
如果一个函数中多个defer语句，他们会以LIFO（后进先出）的顺序执行。哪怕函数或某个延迟调用发生错误，这些调用依旧会被执行。

## 获取命令行参数
```go
package main

import (
	"fmt"
	"os"
)
func main(){
	args := os.Args
	if args == nil || len(args) < 2{
		fmt.Println("err:xxx ip port")
		return
	}
	ip := args[1]
	port := args[2]
}
```
## 复合类型

|类型|名称|长度|默认值|说明|
|---|---|---|---|---|
|pointer|指针||nil||
|array|数组|0|||
|slice|切片||nil|引用类型|
|map|字典|n|nil|引用类型|
|struct|结构体||||

## 复合类型-指针  
- 默认值nil,没有NULL常量
- 操作符“&”取变量地址，"*"通过指针访问目标对象
- 不支持指针运算，不支持"->"运算符，直接用"."访问目标成员

```go
package main

import (
	"fmt"
)
func main(){
	var a int = 10
	fmt.Printf("&a = %p", &a)

	var p *int = nil
	p = &a
	fmt.Printf("p = %p\n", p)
	fmt.Printf("a = %d,*p = %d\n", a, *p)
	*p = 111
	fmt.Printf("a = %d, *p = %d\n", a, *p)
}
``` 
new函数  
表达式new(T)将创建一个T类型的匿名变量，所做的是为T类型的新值分配并清零一块内存空间，然后将这块内存空间的地址作为结果返回，而这个结果就是指向这个新的T类型值的指针值，返回的指针类型为*T.
```go
package main

import (
	"fmt"
)
func main(){
	var p1 *int
	p1 = new(int)
	fmt.Println("*p1 = ", *p1)
	p2 := new(int)
	*p2 = 111
	fmt.Println("*p2 = ", *p2)
}
```
## 符合类型-数组
数组是指一系列同一类型数据的集合。数组中包含的每个数据被称为数组元素，一个数组包含的元素个数被称为数组的长度。  
数组长度必须是常量，且是类型的组成部分。[2]int 和 [4]int是不同类型。  
**操作数组**
数组的每个元素可以通过索引下标来访问，索引下标的范围是从0开始到数组长度减1的位置。  
```go
package main

import (
	"fmt"
)

func main(){
	var a [10] int
	for i := 0; i < 10; i++{
		a[i] = i + 1
		fmt.Println(i, a[i])
	}

	for i, v := range a{
		fmt.Println(i, v)
	}
}
```
内置函数len和cap都返回数组长度
```go
fmt.Println(len(a), cap(a))
```