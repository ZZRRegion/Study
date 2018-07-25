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
```
通过$(":button")可以选取所有type="button"的<input>元素和<button>元素,如果去掉冒号,$("button")智能选取<button>元素.
关于:和[]这两个符号的理解  
:可以理解为种类的意思,如:p:first,p的种类为第一个.  
[]很自然的可以理解为属性的意思,如:[href]选取所有带href属性的元素.
```  
|语法|描述|
|---|---|
|$("*")|选取所有元素|
|$(this)|选取当前HTML元素|
|$("p.intro")|选取class为intro的p元素|
|$("p:first")|选取第一个p元素|
|$("ul li:first")|选取第一个ul元素的第一个li元素|
|$("ul li:first-child")|选取每个ul元素的第一个li元素|
|$("[href]")|选取带有href属性的元素|
|$("a[target='_blank']")|选取所有target属性值等于"_blank"的a元素|
|$("a[target!='_blank']")|选取所有target属性值不等于"_blank"的a元素|
|$("tr:event")|选取偶数位置的tr元素|
|$("tr:odd")|选取奇数位置的tr元素|
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
## jQuery效果-隐藏和显示  
隐藏,显示,切换,滑动,淡入淡出,以及动画.  
**jQuery.hide()和show()**  
``` JS
$("#hide").click(function(){
    $("p").hide();
})
#("#show").click(function(){
    $("p").show();
})
```
语法:  
``` JS
$(selector).hide(speed, callback);
$(selector).show(speed, callback);
```
可选的speed参数规定隐藏/显示的速度,可以取以下值:"slow","fast"或毫秒.  
可选的callback参数是隐藏或显示完成后执行的函数名称.
例子:  
``` JS
$(function(){
    $("click").click(function(){
        $("p").hide(2000, function(){
            console.log("隐藏完毕!");
        })
    })
})
```
**jQuery.toggle()**
通过jQuery,可以使用toggle()方法来切换hide()和show()方法.  
语法:  
> $(selector).toggle(speed, callback);  

与show,hide相同的参数意义
``` JS
$("button").click(function(){
    $("p").toggle(1000, function(){
        console.log("ok");
    });
})
```
*番外*
对于可选的callback参数,有以下两点说明:  
1. $(selector)选中的元素的个数为n哥,则callback函数会执行n次.  
2. callback函数名后加括号,会立即执行函数,而不是等到显示或隐藏完成后执行,但是只会执行一次. 
3. callback既可以是函数名,也可以是匿名函数;  
## jQuery效果-淡入淡出
通过jQuery可以实现元素的淡入淡出效果,拥有四种fade方法:  
- fadeIn()
- fadeOut()
- fadeToggle()
- fadeTo()

**jQuery fadeIn()方法**
用于淡入已隐藏的元素.  
语法:
> $(selector).fadeIn(speed, callback)

例子:
``` JS
$("#wo").click(function(){
    $("p").fadeIn(1000, function(){
        console.log("可以整");
    })
})
```
**jQuery fadeOut()方法**
用于淡出可见元素.  
语法:
> $(selector).fadeout(speed, callback);

例子:
``` JS
$(selector).click(function(){
    $("#p").fadeOut();
    #("#a").fadeOut(3000);
})
```  
**jQuery fadeToggle()方法**
该方法可以在fadeIn()方法和fadeOut()方法之间进行切换.  
语法:  
> $(selector).fadeToggle(speed, callback)  

例子:  
``` JS
$("button").click(function(){
    $("#div1").fadeToggle();
    $("#div2").fadeToggle(3200);
})
```
**jQuery fadeTo()方法**
该方法允许渐变为给定的不透明度(值介于0与1之间).  
语法:  
> $(selector).fadeTo(speed, opacity, callback)  

必须的speed参数规定效果的时长  
opacity参数为淡入淡出效果设置的不透明度.  
可选的callback参数是该函数完成后所执行的函数名称.  
例子:
``` HTML
<p style="color: red;">设施显示的画面</p>
<p style="color: blue;">这是例外</p>
<button id="abc">点击我</button>
<button id="wo">点对对对</button>
<script>
    $(function(){
        $("#abc").click(function(){
            $("p").fadeTo(2000, 0.3);
        })
    })
</script>
```
## jQuery效果-滑动
滑动方法:
- slideDown()
- slideUp()
- slideToggle()
  
**jQuery slideDown()方法**
> $(selector).slideDown(speed, callback)  

例子:
``` HTML
<div style="color: red;">设施显示的画面</div>
    <div style="color: blue;">这是例外</div>
    <button id="abc">点击我</button>
    <button id="wo">点对对对</button>
    <script>
       $(function(){
           $("#abc").click(function(){
              console.log("ds");
               $("div").slideDown(2000);
           })
       })
    </script>
```
**jQuery slideUp()方法**
该方法用于向上滑动元素
> $(selector).slideUp(speed, callback)  

**jQuery slideToggle()方法**
该方法可以在slideDown()与slideUp()方法之间切换.
> $(selector).slideToggle(speed, callback)