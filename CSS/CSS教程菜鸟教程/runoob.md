# CSS教程
通过使用CSS我们可以大大提升网页开发的工作效率  
## 什么是CSS?
- CSS指层叠样式表(Cascading Style Sheets)
- 样式定义如何显示HTML元素
- 样式通常存储在样式表中
- 把样式添加到HTML中,是为了解决内容与表现分离的问题
- 外部样式表可以极大提高工作效率
- 外部样式表通常存储在CSS文件中
- 多个样式定义可层叠为一
  
## CSS语法
CSS规则由两个主要的部分构成:选择器,以及一条或多条声明  

![CSS选择器](http://www.runoob.com/wp-content/uploads/2013/07/632877C9-2462-41D6-BD0E-F7317E4C42AC.jpg)  
## CSS Id和Class  
HTML元素以id属性来设置id选择器,CSS中id选择器以"#"来定义.  

``` CSS
#para{
    text-align: center;
    color: red;
}
```
class选择器以一个点"."号显示:
``` CSS
.center{
    text-align: center;
}
```
## CSS创建
插入样式表的方法有三种  
- 外部样式表
- 内部样式表
- 内联样式表
  
### 外部样式表
``` HTML
<head>
    <link rel="stylesheet" type="text/css" href="my.css">
</head>
```
### 内部样式表  
``` HTML
<head>
    <style>
        hr {
            color: red;
        }
        p {
            margin-left: 20px;
        }
    </style>
</head>
```
### 内联样式
``` HTML
<p style="color: red;">这是一个段落</p>
```
## CSS背景
CSS属性定义背景效果  
- background-color
- background-image
- background-repeat
- background-attachment
- background-position

### 背景颜色
``` CSS
body {
    background-color: #33eeee;
}
```
颜色值定义:
- 十六进制 如: "#eeeeee"
- RGB 如: "rgb(244, 0, 0)"
- 颜色名称 如: "red"
### 背景图像
``` CSS
body {
    background-image: url("paper.gif");
}
```
水平或垂直平铺
``` CSS
body{
    backgrond-image: url("pag.jpg");
    backgrond-repeat: repeat-x;
}
```
设置定位与不平铺
``` CSS
body{
    background-image: url("img.jpg");
    background-repeat: no-repeat;
}
```
可以利用background-position属性改变图像在背景中的位置
``` CSS
body{
    background-image: url("img.jpg");
    background-repeat: no-repeat;
    background-position: right top;
}
```
简写属性
``` CSS
body{
    background: #ffffff url("img.jpg") no-repeat right top;
}
```
顺序为:
- background-color 背景颜色
- background-image 背景图像
- background-repeat 背景如何重复
- background-attachment 背景图像是否固定或者随着页面的其余部分滚动
- background-position 设置图像的起始位置

## CSS文本格式
|属性|描述|
|---|---|
|color|设置文本颜色|
|direction|文本方向|
|letter-spacing|字符间距|
|line-height|行高|
|text-align|对齐元素中的文本|
|text-desoration|文本添加修饰|
|text-indent|缩进文本的首行|
|text-shadow|文本阴影|
|text-transform|控制元素中的字母|
|unicode-bidi|设置或返回文本是否被重写|
|vertical-align|元素的垂直对齐|
|white-space|设置元素中空白的处理方式|
|word-spacing|设置子间距|
## CSS字体
|属性|描述|
|---|---|
|font|在一个声明中设置所有的字体属性|
|font-famail|指定文本的字体系列|
|font-size|指定文本的字体大小|
|font-style|指定文本的字体样式|
|font=variant|让小型大写字体或正常字体显示文本|
|font-weight|指定字体的粗细|
## CSS链接
- a:link 正常,未访问过的链接
- a:visited 用户已访问过的链接
- a:hover 当用户鼠标放在链接上时
- a:active 链接被点击的那一刻

## CSS盒子模型
![盒子模型](http://www.runoob.com/images/box-model.gif)

