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

**jQuery 效果-动画**
jQuery animate()方法用于创建自定义动画.  
语法:  
> $(selector).animate({params}, speed, callback);

必须的params参数定义形成动画的css属性.  
可选的speed参数规定效果的时长.  
可选的callback参数是动画完成后所执行的函数名称.  
实例:把div元素往右边移动250像素  
``` HTML
<body>
<button>开始动画</button>
<p>默认情况下，所有的 HTML 元素有一个静态的位置，且是不可移动的。 
如果需要改变为，我们需要将元素的 position 属性设置为 relative, fixed, 或 absolute!</p>
<div style="background:#98bf21;height:100px;width:100px;position:absolute;">
</div>

</body>
<script>
    $(function(){
        $("button").click(function(){
            $("div").animate({left: '250px'});
        })
    })
</script>
```
jQuery animate()操作多个属性  
``` JS
$("button").click(function(){
    $("div").animate({
        left: '250px',
        opacity: '0.5',
        height: '150px',
        width: '200px'
    });
});
```
> 可以用animate()方法来操作所有css属性,但是必须使用Camel标记法书写所有的属性名,比如,必须使用paddingLeft而不是padding-left.等
> 也可以使用相对值  
``` JS
$("button").click(function(){
    $("div").animate({
        left: '250px',
        height: '+=150px'
    };
});
```
**jQuery停止动画**
jQuery stop()方法用户停止动画或效果,在它们完成之前.  
stop()方法使用于所有jQuery效果函数,包括滑动,淡入淡出和自定义动画.  
语法:  
> $(selector).stop(stopAll, goToEnd);
可选的stopAll参数规定是否应该清除动画队列.默认是false,即仅停止活动的动画,允许任何排入队列的动画向后指定.  
可选的goToEnd参数规定是否立即完成当前动画,默认是false.  
``` JS
$("#stop").click(function(){
    $("#panel").stop();
});
```
## jQuery-获取内容和属性  
获取内容-text(),html()以及val(),attr()和prop()获取属性值
- text()-设置或返回所选元素的文本内容
- html()-设置或返回所选元素的内容(包括html标记)  
- val()-设置或返回表单字段的值  
``` JS
$(function(){
    $("button").click(function(){
        var text = $("p").text();
        var html = $("p").html();
        var val = $("input").val();
        var value = $("a").attr("href");
        var my = $("p").prop("flat");
    })
})
```
*番外*
> attr和prop的区别
> 对于HTML元素本身就带有的固有属性,在处理时,使用prop方法.  
> 对于HTML元素我们自己定义的DOM属性,在处理时,使用attr方法.  

**jQuery-设置内容和属性**
使用之前的三个相同的方法来设置内容:
- text()-设置或返回所选元素的文本内容
- html()-设置或返回所选元素的内容(包括HTML标记)
- val()-设置或返回表单字段的值

实例:
``` JS
$("#btn").click(function(){
    $("#test1").text("hello world");
})
$("#btn").click(function(){
    $("$test2").html("<b>hello world</b>");
});
$("#btn").click(function(){
    $("#test3").val("Runoob");
})
```
text(),html()以及val()的回调函数  
回调函数有两个参数:被选元素列表中当前元素的下标,以及原始值,然后以函数新值返回希望使用的字符串.  
实例:
``` JS
$("#btn1").click(function(){
    $("#test").text(function(i, origText){
        return "旧文本:" + origText + "就是";
    })
})
```
设置属性-attr()
``` JS 
$("button").click(function(){
    $("#run").attr("href", "www.baidu.com");

    $("#run2").attr({
        "href": "www",
        "title": "标题"
    });//同时设置多个属性值
});
```
attr()的回调函数
回调函数有两个参数:被选元素列表中当前元素的下标,以及原始值.然后以函数返回值作为新值.
``` JS
$("button").click(function(){
    $("#run").attr("href", function(i, old){
        return old + "new";
    })
})
```
**jQuery-添加元素**
- append()-在被选元素的结尾插入内容
- prepend()-在被选元素的开头插入内容
- after()-在被选元素之后插入内容
- before()-在被选元素之前插入内容

实例:
``` JS
function appendText(){
	var txt1="<p>文本。</p>";              // 使用 HTML 标签创建文本
	var txt2=$("<p></p>").text("文本。");  // 使用 jQuery 创建文本
	var txt3=document.createElement("p");
	txt3.innerHTML="文本。";               // 使用 DOM 创建文本 text with DOM
	$("body").append(txt1,txt2,txt3);        // 追加新元素
}
```
**jQuery-删除元素**
- remove()-删除被选元素(及其子元素)
- empty()-从被选元素中删除子元素

实例:
``` JS
$("#div1").remove();
$("#div2").empty();
```
过滤被删除的元素  
``` JS
$("p").remove(".italic");
```
**jQuery-获取并设置CSS类**
- addClass()-向被选元素添加一个或多个类
- removeClass()-从被选元素删除一个或多个类
- toggleClass()-对被选元素进行添加/删除类的切换操作
- css()-设置或返回样式属性

``` JS
$("button").click(function(){
    $("h1,h2,p").addClass("blue");
    $("div").addClass("important");
    $("div").addClass("blue test");//添加多个类  
    $("div").removeClass("blue");
    $("div").toggleClass("blue");
});
```
**jQuery css()方法**
``` JS
var color = $("p").css("background-color");
//获取样式值  
$("p").css("background-color", "yellow");
//设置值  
$("p").css({
    "background-color":"yellow",
    "font-size": "200%"
});
//设置多个样式值
```
**jQuery尺寸**
- width()
- height()
- innerWidth()
- innderHeight()
- outerWidth()
- outerHeight()


![jQuery尺寸](http://www.runoob.com/images/img_jquerydim.gif)

## jQuery-AJAX
AJAX=异步JavaScript和XML.  
简短的说,在不重载整个网页的情况下,AJAX通过后台加载数据,并在网页上进行显示.  
**jQuery load()方法**
> $(selector).load(URL, data, callback);

必须的URL参数规定希望加载的URL.  
可选的data参数规定与请求一同发送的查询字符串键值对集合.  
可选的callback参数是load()方法完成后执行的函数名称.
``` JS 
$("input").click(function(){
    $("p").load("/Home/Test");
})
```
可选的callback参数规定当load()方法完成后索要允许的回调函数.回调函数可以设置不同的参数:  
- responseTxt -包含调用成功时的结果内容
- statusTxt -包含调用的状态 
- xhr -包含XMLHttpRequest对象

``` JS
$("button").click(function(){
    $("div").load("/Home/Test", function(res, status, xhr){
        console.log(res);
        console.log(status);
        console.log(xhr);
    })
})
```
## jQuery -AJAX get()和post()方法
> $.get(URL, callback);

必须的URL参数规定请求的URL.  
可选的callback参数是请求成功后所执行的函数名.  
``` JS
$("button").click(function(){
    $.get("/Home/Test", function(data, status){
        console.log(data);
        console.log(status);
    })
})
```
> $.post(URL, data, callback)

必须的URL参数规定请求的URL.  
可选的data参数固定请求发送的数据.  
可选的callback参数是请求成功后所执行的函数名.  
``` JS 
$("button").click(function(){
    $.post("/Home/Test",
    {
        name:'这种人',
        pwd: 123444
    }, function(data, status){
        console.log(data);
        console.log(status);
    });
})
```
``` JS
$.getJson("/Home/TT", function(data){
console.log(data);
});
```