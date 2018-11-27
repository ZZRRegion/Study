## 使用控制台
- error(msg) 将错误信息记录到控制台
- info(msg) 将信息性消息记录到控制台
- log(msg) 将一般消息记录到控制台
- warn(msg) 将警告消息记录到控制台

错误消息带有红色图标,警告消息带有黄色图标  
ECMA-262定义了下列7种错误类型:  
- Error:普通异常.通常与throw语句和try/catch语句一起使用.利用属性name可以声明或了解异常的类型,利用message属性可以设置和读取异常的详细信息.  
- EvalError:在不正确使用eval()方法时抛出.  
- SyntaxError:抛出语法错误.  
- RangeError: 在数字超出合法范围时抛出.
- ReferenceError:在读取不存在的变量时抛出.
- TypeError: 当一个值的类型错误时抛出该异常.
- URIError:由URL的编码和解码方法抛出.  
  
其中Error是基类,其它错误类型都继承自该类型.因此,所有错误类型共享了一组相同的属性,错误对象中的方法全是默认的对象方法. 

**使用try/catch**  
``` JavaScript
try{
    var b = a;
}catch (error){
    console.log(error);
}
```

**使用finally**
finally子句在try-catch语句中是可选的,但如果finally子句已经使用了,则其代码无论如何都会执行.  
``` JavaScript
try{
    return 2;
}catch (error){

}finally{
    return 0;
}
```
无论如何都会返回0.  
**使用throw**
与try-catch语句相配的还有一个throw操作符,用于随时抛出自定义错误.抛出错误时,必须给throw操作符指定一个值,这个值是什么类型没有要求.  
``` JavaScript
throw 1;
throw "hi";
throw {name: 'js'};
```
在遇到throw操作符时,代码会立即停止执行.仅当有try-catch语句捕获到抛出的值时,代码才会继续执行.  
**自定义错误消息**  
``` JavaScript
function CustomError(message){
    this.name = "CustomError";
    this.message = message;
}
CustomError.prototype = new Error();
throw new CustomError("My Message");
```