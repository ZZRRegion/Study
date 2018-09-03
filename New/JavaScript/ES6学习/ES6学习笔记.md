# ES6学习笔记
学习ES6主要参考了阮一峰大牛的书,[<ECMAScript 6入门>](http://es6.ruanyifeng.com/)  
可以使用[Babel](https://babeljs.io/repl)转码器来讲ES6的代码转为ES5的代码,从而在现有环境执行.这意味着,你可以使用ES6的方式编写程序,又不用担心现有环境是否支持.  
## let和const命令  
> 1. let命令
> 2. 块级作用域
> 3. const命令
> 4. 顶层对象的属性
> 5. global对象


1. let命令  
基本用法  
ES6新增了let命令,用来声明变量.它的用法类似于var,但是所声明的变量,只有let命令所在的代码块内有效.  
``` JavaScript
{
    let a = 10;
    var b = 1;
}
a // is not defined.
b // 1
```  
上面代码在代码块之中,分别用let和var声明了两个变量.然后在代码块之外调用者两个变量,结果let声明的变量报错,var声明的变量返回了正确的值.这表明,let声明的变量只在它所在的代码块有效.

for循坏的计数器,就很适合使用let命令.
``` JavaScript
for (let i = 0; i < 10; i++){

}
console.log(i);
// is not defined
```  
不存在变量提升  
var命令会发生"变量提升"现象,即变量可以在声明之前使用,值为undefined.这种现象多多少少是有些奇怪的,按照一般的逻辑,变量应该在声明语句之后才可以使用.  

为了纠正这种现象,let命令改变了语法行为,它所声明的变量一定要在声明后使用,否则报错.  
``` JavaScript
//var的情况
console.log(foo);//输出undefined  
var foo = 2;

//let的情况  
consoel.log(bar);//报错ReferenceError  let bar = 1;
```
上面代码中,变量foo用var命令声明,会发生变量提升,即脚本开始运行时,变量foo已经存在了,但是没有值,所以会输出undefined.变量bar用let命令声明,不会发生变量提升.这表示在声明它之前,变量bar是不存在的,这时如果用到它,就会抛出一个错误.  
## const命令
基本用法  
const声明一个只读的常量.一旦声明,常量的值就不能改变.
``` JavaScript
const PI = 3.1415;
PI //3.1415
PI = 3;
// TypeError:Assignment to constant variable.
```
上面代码表明改变常量的值会报错.  
const声明的变量不得改变值,这意味着,const一旦声明变量,就必须立即初始化,不能留到以后赋值.  
const的作用域与let相同:只在声明所在的块级作用域内有效.
``` JavaScript
if (true){
    const MAX = 5;
}
MAX // uncaught ReferenceError: MAX is not defined  
```
**本质**  
const实际上保证的,并不是变量的值不得改动,而是变量指向的那个内存地址所保存的数据不得改动.对于简单类型的数据,值就保存在变量指向的那个内存地址,因此等同于常量.但对于复合类型的数据,变量指向的内存地址,保存的只是一个指向实际数据的指针,const只能保证这个指针是固定的,至于它指向的数据结构是不是可变得,就完全不能控制了.因此,将一个对象声明为常量必须非常小心.  
``` JavaScript
const foo = {};
foo.prop = 123;
foo.prop // 123
//将foo指向另一个对象,就会报错
foo = {};//TypeError: "foo" is read-only
```
## 顶层对象的属性  
顶层对象,在浏览器环境指的是window对象,在Node指的是global对象.ES5之中,顶层对象的属性与全局变量是等价的.
``` JavaScript
window.a = 1;
a //1
a = 2;
window.a // 2
```  
# 变量的解构赋值  
> 1. 数组的解构赋值
> 2. 对象的解构赋值
> 3. 字符串的解构赋值
> 4. 数值和布尔值的解构赋值
> 5. 函数参数的解构赋值
> 6. 圆括号问题
> 7. 用途

1. 数组的解构赋值  
   **基本用法**
   ES6允许按照一定模式,从数组和对象中提取值,对变量进行赋值,这被称为解构  
   以前,为变量赋值,只能直接指定值  
   ``` JavaScript
   let a = 1;
   let b = 2;
   let c = 3;
   ```
   ES6允许写成这样.  
``` JavaScript
let [a, b, c] = [1, 2, 3];
```
对于Set结构,也可以使用数组的解构赋值.  
``` JavaScript
let [x, y, z] = new Set(['a', 'b', 'c']);
```  

**默认值**  
解构赋值允许指定默认值.  

``` JavaScript
let [foo = true] = [];  
foo // true
let [x, y = 'b'] = ['a'];//x='a', y='b'  
let [x, y = 'b'] = ['a', undefined]; //x='a',y='b'
let [x = 1] = [null];//x=null
```
**对象的解构赋值**  

解构不仅可以用于数组,还可以用于对象.  
``` JavaScript
let {foo, bar} = {foo: "aaa", bar: "bbb"};
foo // aaa
bar // bbb
```  

如果变量名与属性名不一致,必须写成下面这样:  
``` JavaScript
let {foo:baz} = {foo: 'aaa', bar: 'bbb'};
baz // aaa
```  
**字符串的解构赋值**  
``` JavaScript
const [a,b,c,d,e] = "hello";
a //h
b //e
c //l
d //l
e //o
```  

类似数组的对象有一个length属性,因此还可以对这个属性解构赋值.  
``` JavaScript
let {length: len} = "hello";
len // 5
```  
