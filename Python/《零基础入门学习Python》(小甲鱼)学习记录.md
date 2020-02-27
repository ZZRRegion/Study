# 《零基础入门学习Python》(小甲鱼)学习记录

### 2月27日

1. p4小插曲之变量和字符串

   [视频](https://www.bilibili.com/video/av27789609?p=4)

   > 变量就是社会现实中的名字

   测试题：

   0. 以下哪个变量的命名不正确？为什么？

      (A)MM_520 (B)_MM520_ (C)520_MM (D)_520_MM

      答：C，数字不能作为变量名的开头

   1. 在不上机的情况下，以下代码你能猜到屏幕会打印什么内容吗？

      答：‘小甲鱼'

   2. 在不上机的情况下，以下代码你能猜到屏幕会打印什么内容吗？

      答：’小甲鱼'

   3. 在不上机的情况下，以下代码你能猜到屏幕会打印什么内容吗？

      答：‘520’

   4. 除了使用反斜杠(\)进行字符转义，还有什么方法可以打印:Let's go!这个字符串？

      答：print(r"Let's go!")

   5. 答：

      ```python
      DaysPerYear = 365
      HoursPerDay = 24
      MinutesPerHour = 60
      SecondsPerMinute = 60
      
      totals = DaysPerYear * HoursPerDay * MinutesPerHour * SecondsPerMinute
      print(totals)
      ```

      

2. P5改进我们的小游戏

   > random模块

3. P6闲聊之Python的数据类型

   [视频](https://www.bilibili.com/video/av27789609?p=6)

   整型、布尔型、浮点型、e记法

   int()、str()、float()

   type查看数据类型

   isinstance(a, b) #判断类型a与b的类型是否一致

   isinstance("sdf", str) # True

   isinstance(110, int) # True

   isinstance(True, bool) # True

   isinstance(2.23, float) # True

### 2月25日

1. 愉快的开始

2. 我和Python的第一次亲密接触

 下载Python并安装

```
print("I love fishc.com")
```

```
# 表示注释
```

> ALT+N下一个命令，ALT+P上一个命令

```python
print(4 + 2) # 可以在print中做运算
print("well water" + " river") # 字符串拼接
print("i love\n" * 8) # 字符串乘法
i love
i love
i love
i love
i love
i love
i love
i love
```

  **测试题**

0. Python是什么类型的语言？

​       答：是一门脚本型语言

		> 脚本语言的特性：
		>
		> * 语法和结构通常比较简单
		> * 学习和使用通常比较简单
		> * 通常以容易修改程序的“解释”作为运行方式，而不需要编译
		> * 程序的开发产能优于运行性能
		>
		> 

1. IDLE是什么？

   答：是一个Python的代码编辑器

2. print()的作用是什么？

   答：打印内容

3. Python中表示乘法的符号是什么？

   答：*（星号）

4. 为什么>>>print('I love fishc.com' * 5)可以正常执行，但>>>print('I love fishc.com' + 5)却报错？

   答：字符串支持乘法运算，字符串和数字不支持加法运算

5. 如果我需要在一个字符串中嵌入一个引号，正确的做法是？

   答：'''随意输入'""'''

6. 为什么我们要使用Python3?Python2到底有什么问题？看起来很多程序员依然在使用Python2?

   答：确实还有相当多的程序员在使用Python2，不过Python3才是Python发展的未来。

动动手：

0. 动手试试直接输入>>>5 + 8与输入>>>print(5 + 8)有何不同？

   答：

1. 在交互模式中，使用Python计算一年有多少秒？

   答：print(365 * 24 * 60 * 60) #31536000s

2. 设置你的操作系统的环境变量，以便可以轻松进入Python环境：

   答：在高级系统设置中，设置系统的环境变量Path中增加Python的安装目录

3. 用Python设计第一个游戏

   [Python视频](https://www.bilibili.com/video/av27789609?p=3)

   > 按Tab键可以看提示代码内容
   
   ```python
   print("-------我爱----------------")
   temp = input("不妨猜一下小甲鱼现在心里想的是什么数字：")
   guess = int(temp)
   if guess == 8:
       print("很好，你是小甲鱼心里的蛔虫吗？")
       print("哼，猜中了也么有奖励")
   else:
       print("猜错啦，是8！")
print("游戏结束")
   ```

   流程图

   * 圆角矩形表示流程的开始或结束

   * 矩形表示处理

   * 菱形表示判断

   
   > BIF  : Built-in functions 内置函数
   
   ```python
   dir(__builtins__) #查看内置函数
   help(input) # 查看函数帮助内容
   ```
   
   测试题：
   
     0. 什么是BIF
   
        答：Python的内置函数
   
   		1. 用课堂上的方法数一数Python3提供了多少个BIF？
   
        答：
   
   		2. 在Python看来：“FishC"和"fishc"一样吗？
   
        答：不一样，大小写是敏感
   
   		3. Python中什么是最重要的？你赞同吗？
   
        答：缩进！在小甲鱼看来，缩进是 Python 的灵魂，缩进的严格要求使得 Python 的代码显得非常精简并且有层次（小甲鱼阅读过很多大牛的代码，那个乱......C语言不是有国际乱码大赛嘛......）。
   
         所以在 Python 里对待缩进代码要十分小心，如果没有正确地缩进，代码所做的事情可能和你的期望相去甚远（就像C语言里边括号打错了位置）。
   
         如果在正确的位置输入冒号“:”，IDLE 会自动将下一行缩进！
   
   		4. 这节课的例子中出现了"="和"=="，表示不同的含义，如果避免误写错误？
   
        答：在 Python 这里，不好意思，行不通，语法错误！Python 不允许 if 条件中赋值，所以 if c = 1: 会报错！
   
   		5. 你听过“拼接”这个词吗？
   
        答：字符串拼接
   
   动动手：
   
    0. 编写程序：hello.py，要求用户输入姓名并打印“你好，姓名！”
   
       答：
   
       ```python
       name = input("请输入你的姓名：")
       print("你好，{}!".format(name))
       ```
   
       
   
   	1. 编写程序：calc.py要求用户输入1到100之间数字并判断，输入符合要求打印“你妹好漂亮”，不符合要求则打印“你大爷好丑”
   
       答：
   
       ```python
       num = int(input("请输入数字："))
       if num >= 1 and num <= 100:
           print("你妹好漂亮")
       else:
           print("你大爷好丑")
       
       ```
   
       
   
   	2. 请写下这一节课你学习到的内容
   
       答：