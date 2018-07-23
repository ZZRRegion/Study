# jQuery学习  
本篇主要参考[菜鸟教程](http://www.runoob.com/jquery/jquery-install.html)  
## jQuery安装  
``` JS
BootCDN  
<script src="https://cdn.bootcss.com/jquery/1.10.2/jquery.min.js">
百度  
<script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js">
```  
## jQuery语法  
通过jQuery,可以选取(查询,query) HTML元素,并对它们执行"操作"(actions)  
基础语法:$(selector).action()  
- 美元符号定义jQuery  
- 选择符(selector)"查询"和"查找"HTML元素  
- jQuery的action()执行对元素的操作  

实例  
- $(this).hide()-隐藏当前元素  
- $("p").hide()-隐藏所有<p>元素  
- $("p.test").hide()-隐藏所有class="test"的<p>元素  
- $("#test").hide()-隐藏所有id="test"的元素  
  
**文档就绪事件**
``` JS
$(document).ready(function(){
    //开始写jQuery代码
});  
```
这是为了防止文档在完全加载就绪之前运行jQuery代码.还有更加简洁的写法:
``` JS
$(function(){

    //开始写代码
});
```
JavaScript入口函数:
``` JS
window.onload = function(){
    //开始写代码
}
``` 
jQuery入口函数与javaScript入口函数的区别:  
- jQuery的入口函数式在html所有标签(DOM)都加载之后,就会去执行.
- JavaScript的window.onload事件是等到所有内容,包括外部图片之类的文件加载完后,才会执行.
    
## jQuery选择器  
**元素选择器**
jQuery元素选择器基于元素名选取元素.  
在页面中选取所有<p>元素  
``` JS
$("p")
```
实例  
用户点击按钮后,所有<p>元素都隐藏  
``` JS
$(function(){
    $("button").click(function(){
        $("p").hide();
    })
})
```
**ID选择器**  
通过id选取元素语法如下:  
``` JS
$("#test")
```  
实例  
当用户点击按钮后,有id="test"的属性的元素将被隐藏:  
``` JS
$(function(){
    $("button").click(function(){
        $("#test").hide();
    })
})
```  
**class选择器**
jQuery类选择器可以通过指定的class查找元素.  
语法如下:
``` JS
$(".test");
```  
实例  
用户点击按钮后所有带有class="test"属性的元素都隐藏:  
``` JS
$(fucntion(){
    $("button").click(function(){
        $(".test").hide();
    })
});
```  
*番外*  
> 通过$(":button")可以选取所有type="button"的<input>元素和<button>元素,如果去掉冒号,$("button")智能选取<button>元素.
> 关于:和[]这两个符号的理解  
> :可以理解为种类的意思,如:p:first,p的种类为第一个.  
> []很自然的可以理解为属性的意思,如:[href]选取所有带href属性的元素.

|语法|描述|
|---|---|
|$("*")|选取所有元素|
|$(this)|选取当前HTML元素|
|$("p.intro")|选取class为intro的<p>元素|
|$("p:first")|选取第一个<p>元素|
|$("ul li:first")|选取第一个<ul>元素的第一个<li>元素|
|$("ul li:first-child")|选取每个<ul>元素的第一个<li>元素|
|$("[href]")|选取带有href属性的元素|
|$("a[target='_blank']")|选取所有target属性值等于"_blank"的<a>元素|
|$("a[target!='_blank']")|选取所有target属性值不等于"_blank"的<a>元素|
|$("tr:event")|选取偶数位置的<tr>元素|
|$("tr:odd")|选取奇数位置的<tr>元素|
## jQuery事件  
<span id="event">常用DOM事件</span>
|鼠标事件|键盘事件|表单事件|文档窗口事件|
|---|---|---|---|
|click|keypress|submit|load|
|dblclick|keydown|change|resize|
|mouseenter|keyup|focus|scroll|
|mouseleave||blur|unload|
**jQuery事件方法语法**
页面中指定一个点击事件:  
``` JS
$("p").click()
```
下一步是定义完成什么:  
``` JS
$("p").click(function(){
    //动作触发后的执行代码
})
```
**常用的jQuery事件方法**
``` JS
$("p").click(function(){

})
$("p").dblclick(function(){

})
$("p").mouseenter(function(){

})
$("p").mouseleave(function(){

})
$("p").mousedown(function(){

})
$("p").mouseup(function(){

})
$("p").hover(function(){

})
$("input").focus(function(){

})
$("input").blur(function(){

})
$(window).keydown(function(event){
    //通过event.whitch可以拿到按键代码.
})
```

传递数据给事件处理函数  
> jQuery.keydown([[data,] handler]);
- data:通过event.data传递给事件处理函数的任意数据
- handler:指定的事件处理函数;  
  
举例:  
```
var validKeys = {start: 65, end: 90};
$("#key").keydown(validKeys, function(event){
    var keys = event.data;//拿到validkeys对象.
    return event.which >= keys.start && event.which <= keys.end;
})
```