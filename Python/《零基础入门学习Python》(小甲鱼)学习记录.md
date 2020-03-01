# 《零基础入门学习Python》(小甲鱼)学习记录

### 3月1日

1. P46魔法方法：属性访问

   getattr

   setattr

   delattr

   property

   ```python
   >>> class C:
   	def __init__(self, size=10):
   		self.size = size
   	def getSize(self):
   		return self.size
   	def setSize(self, value):
   		self.size = value
   	def delSize(self):
   		del self.size
   	x = property(getSize, setSize, delSize)
   ```

   ```python
   __getattr__(self,name)定义当用户视图获取一个不存在的属性时的行为
   __getattribute__(self,name)
   定义当该类的属性被访问时的行为
   __setattr__(self,name,value)
   定义当一个属性被设置时的行为
   __delattr__(self,name)
   定义当一个属性被删除时的行为
   
   >>> class C:
   	def __getattribute__(self,name):
   		print("getattribute")
   		return super().__getattribute__(name)
   	def __getattr__(self, name):
   		print("getattr")
   	def __setattr__(self,name,value):
   		print("seattr")
   		super().__setattr__(name,value)
   	def __delattr__(self, name):
   		print("delattr")
   		super().__delattr__(name)
   ```

   防止递归调用

   ```python
   class Rectangle:
       def __init__(self, width = 0, height = 0):
           self.width = width
           self.height = height
   
       def __setattr__(self, name, value):
           print(name)
           if name == "square":
               self.width = value
               self.height = value
           else:
               super().__setattr__(name, value)
               #self.__dict__[name] = value
   
       def getArea(self):
           return self.width * self.height
   ```

   2. P47魔法方法：描述符(property的原理)

      描述符

      描述符就是某种特殊类型的类的实例指派给另一个类的属性

      ```python
      __get_(self, instance,owner)
      用于访问属性，它返回属性的值
      __set__(self, instance, value)
      将在属性分配操作中调用，不返回任何内容
      __delete__(self, instance)
      控制删除操作，不返回任何内容
      ```

   3. P48魔法方法：定制序列

      | 函数名                        | 说明                                                  |
      | ----------------------------- | ----------------------------------------------------- |
      | __len__(self)                 | 定义当被len()调用时的行为（返回容器中元素的个数       |
      | __getitem__(self, key)        | 定义获取容器中指定元素的行为，相当于self[key]         |
      | __setitem__(self, key, value) | 定义设置容器中指定元素的行为，相当于self[key] = value |
      | __delitem__(self, key)        | 定义删除容器中指定元素的行为，相当于del self[key]     |
      | __iter__(self)                | 定义当迭代器中的元素的行为                            |
      | __reversed__(self)            | 定义当被reversed()调用时的行为                        |
      | __contains__(self, item)      | 定义当使用成员测试运算符(in 或not in)                 |

      ```python
      class CountList:
          def __init__(self, *args):
              self.values = [x for x in args]
              self.count = {}.fromkeys(range(len(self.values)), 0)
      
          def __len__(self):
              return len(self.values)
          def __getitem__(self, key):
              self.count[key] += 1
              return self.values[key]
      ```

      4. P49 魔法方法：迭代器

         ```python
         iter()
         __iter__()魔法方法
         next()
         __next__()魔法方法
         >>> string = "我爱中国"
         >>> it = iter(string)
         >>> next(it)
         '我'
         >>> 
         实现迭代器对象
         class Fibs:
             def __init__(self, n = 10):
                 self.n = n
                 self.a = 0
                 self.b = 1
             def __iter__(self):
                 return self
             def __next__(self):
                 self.a, self.b = self.b, self.a + self.b
                 if self.a > self.n:
                     raise StopIteration
                 return self.a
         
         fibs = Fibs()
         for each in fibs:
             print(each)
         ```

      5. P50乱入：生成器

         yield

         ```python
         >>> def myGen():
         	print("生成器被执行!")
         	yield 1
         	yield 2
         my = myGen()
         next(my)
         next(my)
         也可以使用for
         for each in my:
             print(each)
         ```

         ```python
         列表推导式
         a = [i for i in range(100) if not(i % 2) and i % 3]
         字典推导式
         b = {i:i % 2 == 0 for i in range(10)}
         >>> b
         {0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}
         >>> 
         集合推导式
         >>> c = {i for i in {1, 2, 3, 4, 56, 4,4}}
         >>> c
         {1, 2, 3, 4, 56}
         >>> 
         生成器推导式
         >>> e = (i for i in range(100))
         >>> e
         <generator object <genexpr> at 0x000001F32F7C9AC0>
         >>> 
         ```

      6. P51模块：模块就是程序

         容器->数据的封装

         函数->语句的封装

         类=>方法和属性的封装

         模块->模块就是程序

         > 导入模块
         >
         > import hello
         >
         > from hello import * #不需要前缀模块名调用
         >
         > import hello as newName

      7. P52模块：__name__='__main__'搜索路径和包

         ```python
         if __name__ == '__main__'
         import sys
         sys.path
         ```

      8. P53模块：像个极客一样去思考

         用一种方法，最好是只有一种方法来做一件事

         Python标准库中包含一般任务所需要的模块

         timeit
         
      9. P54论一只爬虫的自我修养1
      
         urllib
      
         http,https,ftp,file,ed2k...
      
         import urllib.request
      
         response = urllib.request.urlopen("http://www.baidu.com")
      
      10. P55论一只爬虫的自我修养2：实战
      
          import urllib.parse
      
          urllib.parse.urlencode(data).encode("utf-8")
      
      11. P56论一只爬虫的自我修养3：隐藏
      
          代理
      
          步骤：
      
          1参数是一个字典{'类型':'代理IP:端口号'}
      
          proxy_support = urllib.request.ProxyHandler({})
      
          2定制、创建一个opener
      
          opener = urllib.request.build_opener(proxy_support)
      
          3安装opener
      
          urllib.request.install_opener(opener)
      
          4调用
      
          opener.open(url)
      
      12. P57论一只爬虫的自我修养4：ooxx
      
      13. P65GUI的终极选择：tkinter1
      
          import tkinter
      
          ```python
          import tkinter as tk
          
          class App:
              def __init__(self, master):
                  frame = tk.Frame(master)
                  frame.pack(side = tk.LEFT, padx = 10, pady = 100)
          
                  self.hi_there = tk.Button(frame, text = "打招呼", fg="blue", bg = "white", command=self.say_hi)
                  self.hi_there.pack()
          
              def say_hi(self):
                  print("互联网的广大朋友你们好")
          
          root = tk.Tk()
          app = App(root)
          
          root.mainloop()
          ```
      
      14. P66GUI的终极选择：tkinter2
      
      15. P79 Pygame：初次见面，请大家多多关照
      
          ```python
          import pygame
          import sys
          #初始化pygame
          pygame.init()
          size = width, height = 600, 400
          speed = [-2, 1]
          bg = (255, 255, 255)
          # 创建指定大小的窗口
          screen = pygame.display.set_mode(size)
          # 设置窗口标题
          pygame.display.set_caption("初次见面")
          # 加载图片
          turtle = pygame.image.load("22.jpg")
          # 获取图像的位置矩形
          position = turtle.get_rect()
          
          while True:
              for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                      sys.exit()
              #移动图形
              position = position.move(speed)
          
              if position.left < 0 or position.right > width:
                  #翻转图像
                  turtle = pygame.transform.flip(turtle, True, False)
                  #反向移动
                  speed[0] = -speed[0]
          
              if position.top < 0 or position.bottom > height:
                  speed[1] = -speed[1]
              #填充背景
              screen.fill(bg)
              screen.blit(turtle, position)
              pygame.display.flip()
              pygame.time.delay(1000)
          ```
      
      16. P80Pygame:解惑
      
      17. P81Pygame:事件

### 2月29日

1. P14元组：戴上枷锁的列表

   [视频](https://www.bilibili.com/video/av27789609?p=14)

   创建元组

   member = (1, 2, 3) 

   member= 1, 2, 3 

   逗号才是关键

   元组是不能修改的

   元组更新

   temp = (1, 2, 3)

   temp = temp[:2] + (3,) + temp[2:]

2. P15字符串：各种奇葩的内置方法

   capitalize()将字符串的第一个字符改为大写

   casefold()将字符串所有改为小写字母

   center(width)将字符串居中，并使用空格填充至长度width的新字符串

   count(sub[,start[,end]])返回sub在字符串中出现的次数.start和end表示范围

   endswitch(sub[,start[,end]])检查字符串是否以sub子字符串结束

   expandtabs([tabsize=8])把字符串中的tab符号(\t)转换为空格

   find(sub[,start[,end]])检测sub是否包含在字符串中，如果有则返回索引值，否则返回-1

   index(sub[,start[,end]])跟find方法一样，不过如果sub不在string中会产生一个异常

   join(sub)以字符串作为分隔符，插入到sub中所有的字符之间

   lstrip()去掉字符串左边的所有空格

3. P16字符串：格式化

   [视频](https://www.bilibili.com/video/av27789609?p=16)

   "{0} love {1}.{2}".format(2, 3, 4)

   "{0} love {b},{c}".format("1", b = "fishc", c="com")

   "{{0}}".format(2)，打印花括号

   “{0:.1f}{1}".format(23.223, "GB")

   '%c' % 97 格式化

   ‘%s' % "是否" 格式化字符串

   "%d + %d = %d" % (3, 4, 3 + 4) 多参数使用元组

   "%3.22f" % 2.234

   m.n m是显示最小总宽度,n是小数点后的位数

   >"%10.2f" % 2.33
   >'      2.33'
   >
   >不够的填充空格

   >"%#x" % 23
   >'0x17'

   "%010d" % 2
   '0000000002'

4. P17 序列！序列！

   列表、元组和字符串的共同点

   都可以通过索引得到每一个元素

   默认索引值总是从0开始

   可以通过分片的方法得到一个范围

   有很多共同的操作符

   max

   min

   sorted(member)

   reversed(member)

   >list(enumerate(numbers))
   >[(0, 1), (1, 18), (2, 18), (3, 0), (4, -98), (5, 34), (6, 54), (7, 76), (8, 32)]

   >a = [1, 2, 3, 4, 5, 6, 7, 8]
   >b = [4, 5, 6, 7, 8]
   >zip(a, b)
   ><zip object at 0x0000021DF8F1A540>
   >list(zip(a, b))
   >[(1, 4), (2, 5), (3, 6), (4, 7), (5, 8)]

5. P18 函数：Python的乐高积木

   def myfirstfunction():

   ​		print("hello world")

   ​		return "OK"

   myfirstfunction()

6. P19 函数：灵活即强大

   def test(*params):

   ​		print("参数长度是：", len(params))

   ​		print("第二个参数是：", params[1])

7. P20 函数：我的地盘听我的

   返回值空：None

8. P21函数：内嵌函数和闭包

   def test():

   ​		global count

   ​		count = 10

   count = 1

   test()

   在函数中使用global声明一下全局变量，则在函数内就可以修改全局变量的值了。

   内嵌函数

   def fun1():

   ​		print("fun1调用")

   ​		def fun2():

   ​				print("fun2调用")

   ​		fun2()

   <font color=blue>nonlocal</font>使用

   def fun1():
       x = 5
       def fun2():
           nonlocal x
           x *= x
           return x
       return fun2()
   print(fun1())

9. P22函数：lambada表达式

   匿名函数

   c = lambda x,y: x + y

   c(2, 3)

   <font color=blue>filter</font>

   >member = [1, 0, 2, 3]
   >list(filter(None,member))
   >[1, 2, 3]

   >>list(filter(lambda x: x > 2,member))
   >>[3]

   <font color=blue>map</font>

   >>list(map(lambda x: x * 2, member))
   >>[2, 0, 4, 6]

10. P23函数：递归是神马

    def ss(x):

    ​		if x == 1:

    ​					return 1

    ​		return x * ss(x - 1)

11. P24函数：这帮小兔崽子

12. P25递归：汉诺塔

13. P26字典：当索引不好用时1

    创建和使用字典

    dict1 = {"sdf":"sdf", "sfw": "sdfs"}

14. P27字典：当索引不好用时2

    <font color=blue>fromkeys</font>

    >dict1 = dict.fromkeys("12345")
    >dict1
    >{'1': None, '2': None, '3': None, '4': None, '5': None}

    >>dict1 = dict.fromkeys("1234", "中国")
    >>dict1
    >>{'1': '中国', '2': '中国', '3': '中国', '4': '中国'}

15. P28集合：在我的世界里，你就是唯一

    集合中的元素都是唯一的

    <font color=blue>frozenset</font>

    冻结的集合

    num3 = frozenset([1, 2, 3, 4])

    不可修改

16. P29因为懂你，所以永恒

    open打开文件

    ’r'以只读方式打开文件

    'w'以写入的方式打开文件，会覆盖已存在的文件

    'x'如果文件已经存在，使用此模式打开将引发异常

    'a'以写入模式打开，如果文件存在，则在末尾追加写入

    'b'以二进制模式打开

    f.close()关闭文件

    f.read(size=-1)从文件读取size个字符，当未给定size或给定负值的时候，读取剩余的所有字符，然后作为字符串返回

    f.readline()

    f.write(str)将字符串str写入文件

    f.writelines(seq)向文件写入字符串序列seq，seq应该是一个返回字符串的课迭代对象

    f.seek(offset,from) 在文件中移动文件指针，从from（0代表文件起始文件，1代表当前位置，2代表文件末尾）偏移offset个字符

    f.tell()返回当前文件中的位置

17. P30文件：一个任务

18. P31文件系统：介绍一个高大上的东西

    OS模块

    getcwd()返回当前工作目录

    chdir(path)改变工作目录

    listdir(path=".") 列举指定目录中的文件名

    mkdir(path)创建目录，该目录已存在抛出异常

    makedirs(path)递归创建多层目录，如该目录已存在抛出异常

    remove(path)删除文件

    rmdir(path)删除目录

    removedirs(path)递归删除目录，从子目录到父目录逐层删除，遇到目录非空则抛出异常

    rename(old, new)将文件old重命名为new

    system(command)运行系统的shell命令


    os.curdir 指代当前目录('.')
    
    os.pardir 指代上一级目录('..')
    
    os.sep 输出操作系统特定的路径分隔符（win下为"\\\\",linux下为“/")
    
    os.linesep 当前平台使用的行终止符(win下为"\\r\\n", linux下为"\\n")
    
    os.name 指代当前使用的操作系统(包括：'posix','nt','mac','os2','ce','java')


​    

    ##### os.path模块中关于路径常用的函数使用方法
    
    basename(path)去掉目录路径，返回文件名
    
    dirname(path)去掉文件名，返回目录路径
    
    join(path1[,path2[,...])将path1，path2拼接路径
    
    split(path)分隔文件名与路径
    
    splitext(path)分离文件名与扩展名
    
    getsize(file)返回指定文件的尺寸
    
    getatime(file)返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或
    
    localtime()函数换算)
    
    getctime(file)返回指定文件的创建时间
    
    getmtime(file)返回指定文件最新的修改时间
    
    exists(path)判断指定路径是否存在
    
    isabs(path)判断指定路径是否绝对路径
    
    isdir(path)判断指定路径是否存在且是一个目录
    
    isfile(path)判断指定路径是否存在且是一个文件
    
    islink(path)判断指定路径是否存在且是一个符号链接
    
    ismount(path)判断指定路径是否存在且是一个挂载点
    
    samefile(path1,path2)判断path1和path2两个路径是否指向同一个文件

19. P32永久存储：腌制一缸美味的泡菜

    pickle模块

    dump写入

    load加载

20. P33异常处理：你不可能总是对的1

    标准异常总结

    AssertionError 断言语句失败

    AttributeError尝试访问未知的对象属性

    IndexError 索引超出序列的范围

21. P34异常处理：你不可能总是对的2

    try:

    ​	检测范围

    except Exception [as reason]:

    ​	出现异常的处理情况



​		try:

​			检查范围

​		except Exception[as reason]:

​			出现异常

​		finally:

​			无论如何也执行

​	raise ZeroDivisionError 主动抛异常

22. P35丰富的else语句及简洁的with语句

    with open("wo.txt") as f:

23. P36推行用户界面入门：EasyGui

24. P37类和对象：给大家介绍对象

    属性+方法=对象

    ```python
    class Turtle:
        def run(self, name):
            print(name)
            pass
        @staticmethod
        def funcname(parameter_list):
            pass
    t = Turtle()
    print(t)
    t.run("name")
    ```

    封装 继承 多态

    ```python
    class Turtle:
        def run(self, name):
            print(name)
            pass
    
        @staticmethod
        def funcname(parameter_list):
            pass
    
    class MyTurtle(Turtle):
        def sleep(self, name):
            print(name)
    
    m = MyTurtle()
    m.run("hello world")
    
    ```

25. P38类和对象：面向对象编程

    ```python
    __init__(self) #构造函数
    
    class Ball:
        def __init__(self):
            self.name = "账啊"
    
        def run(self):
            print(self.name)
    
    b = Ball()
    b.run()
    ```

    公有和私有

    __双下滑线的函数或者变量就变成私有变量或函数了

26. P39类和对象：继承

    ```python
    class ClassName(BaseClassName):
        ....
    ```

    ```python
    import random as r
    
    class Fish:
        def __init__(self):
            self.x = r.randint(0, 10)
            self.y = r.randint(0, 10)
    
        def move(self):
            self.x -=1
            print("我的位置是:", self.x, self.y)
    
    class Goldfish(Fish):
        pass
    class Carp(Fish):
        pass
    class Salmon(Fish):
        pass
    
    class Shark(Fish):
        def __init__(self):
            Fish.__init__(self)
            self.hungry = True
    
        def eat(self):
            if self.hungry:
                print("吃货的梦想就是天天有的吃")
                self.hungry = False
            else:
                print("太撑了，吃不下了")
    
    ```

    <font color=red>super().__init__()</font>

    支持多重继承

    ```python
    class ClassName(baseClass1,baseClass2):
        ....
    ```

27. P40 类和对象：拾遗

28. P41类和对象：一些相关的BIF

    issubclass(class, classinfo) 

    >>issubclass(B, object)
    >>True

    isinstance(object, classinfo)

    hasattr(object, name) 判断是否有该指定属性

    getattr(object, name[,default])返回对象指定属性的值

    setattr(object,name,value) 设定指定属性的值

    delattr(object,name)删除指定的属性

    property(fget=None, fset=None, fdel =None, doc=None)属性设置属性

    ```python
    >>> class C:
    	def __init__(self, size=10):
    		self.size = size
    	def getSize(self):
    		return self.size
    	def setSize(self, value):
    		self.size = value
    	def delSize(self):
    		del self.size
    	x = property(getSize, setSize, delSize)
    
    	
    >>> cl = C()
    >>> cl.x
    ```

29. P42魔法方法：构造和析构

    魔法方法总是被双下划线包围，例如__init__

    ```python
    def __init__(self[,...])
    __new__(cls[,...])
    ```

    ```python
    >>> class CapStr(str): # 继承的是一个不可改变的类
    	def __new__(cls,string): #可以在new的时候进行替换，然后将替换后的返回
    		string = string.upper()
    		return str.__new__(cls, string)
    
    	
    >>> a = CapStr("hello I")
    >>> a
    'HELLO I'
    ```

    ```python
    __del__(self) #析构函数，当垃圾回收的时候会执行
    >>> class C:
    	def __init__(self):
    		print("我是init")
    	def __del__(self):
    		print("我是del")
    
    		
    >>> c = C()
    我是init
    >>> del c
    我是del
    >>> 
    ```

30. P43魔法方法：算术运算1

    | 魔法方法                     | 说明                                |
    | ---------------------------- | ----------------------------------- |
    | __add__(self, other)         | 定义加法的行为：+                   |
    | __sub__(self, other)         | 定义减法的行为:-                    |
    | __mul__(self, other)         | 定义乘法的行为：*                   |
    | __truediv__(self,other)      | 定义真除法的行为:/                  |
    | __floordiv__(self,other)     | 定义整数除法的行为://               |
    | __mod__(self,other)          | 定义取模算法的行为：%               |
    | __divmod__(self,other)       | 定义当被divmod()调用时的行为        |
    | __pow__(self,other[,moduio]) | 定义当被power()调用或**运算时的行为 |
    | __ishift__(self,other)       | 定义按位左移位的行为：<<            |
    | __rshift__(self,other)       | 定义右移位的行为：>>                |
    | __and__(self,other)          | 定义按位与操作的行为：&             |
    | __xor__(selft,other)         | 定位按位异或的行为：^               |
    | __or__(self,other)           | 定义按位或的行为：\|                |

    ```python
    >>> class New_int(int):
    	def __add__(self, other): #重写加法运算
    		return int.__sub__(self, other)
    	def __sub__(self, other): #重写减法运算
    		return int.__add__(self, other)
    
    	
    >>> a = New_int(3)
    >>> b = New_int(5)
    >>> a + b
    -2
    >>> 
    ```

31. P44 魔法方法：算术预算2

32. P45魔法方法：简单定制

    ```python
    >>> class A():
    	def __str__(self):
    		return "小甲鱼是帅哥"
    
    	
    >>> a = A()
    >>> print(a)
    小甲鱼是帅哥
    >>> class B():
    	def __repr__(self):
    		return "小甲鱼"
    
    	
    >>> b = B()
    >>> b
    小甲鱼
    ```

    ```python
    import time as t
    
    class MyTime():
        def __init__(self):
            self.unit = ['年','月','天','小时时','分钟','秒']
            self.prompt = "未开始计时"
            self.lasted = []
            self.begin = 0
            self.end = 0
        def __str__(self):
            return self.prompt
        __repr__ = __str__
        def __add__(self, other):
            prompt = "总共运行了"
            result = []
            for index in range(6):
                result.append(self.lasted[index] + other.lasted[index])
                if result[index]:
                    prompt += (str(result[index]) + self.unit[index])
                return prompt
        # 开始计时
        def start(self):
            self.begin = t.localtime()
            self.prompt = "提示，请先条用stop亭子计时"
            print("计时开始")
    
        # 停止计时
        def stop(self):
            if not self.begin:
                print("提示", "请先代用start()")
            else:
                self.end = t.localtime()
                self._calc()
                print("计时停止")
                self.begin = 0
                self.end = 0
    
        # 内部方法计算运行时间
        def _calc(self):
            self.lasted = []
            self.prompt = "总共运行了"
            for index in range(6):
                self.lasted.append(self.end[index] - self.begin[index])
                if self.lasted[index]:
                    self.prompt += str(self.lasted[index]) + self.unit[index]
        
            
    
    ```

    

### 2月28日

1. P7Python之常用操作符

   算术操作符：+、-、*、、、%、**、//

   其中**是幂操作，//是取整除数

2. P8了不起的分支和循环1

3. P9了不起的分支和循环2

   x if 条件 else y 

   small = x if x < y else y

   assert断言

   assert(par) par的表达式值为False就自爆

4. P10了不起的分支和循环3

   while 条件:

   ​	循环体

   for 目标 in 表达式:

   ​	循环体

   range([starat,]stop[,step=1])

5. P11列表：一个打了激素的数组1

   一个普通列表

   member = ["小甲鱼", "小布丁", "黑夜", "迷途", "怡景"]

   列表添加元素

   <font color=blue>append()</font>

   append()

   member.append("这种人")

   len(member) #取列表长度

   <font color=blue>extend</font>

   member.extend(["sf", "sdfs"])#添加列表

   <font color=blue>insert(index, p)</font>

   member.insert(0, "sdf")

6. P12列表：一个打了激素的数组2

   从列表删除元素

   <font color=blue>remove</font>

   <font color=blue>del member[0]</font>

   <font color=blue>del member</font>

   <font color=blue>pop()</font>

   弹出最后一个值

   <font color=blue>pop(2)</font>

   弹出指定索引的值

   切片操作

   member[0:2]取左不取右原则

   member[1:]取从下标1开始的全部

   7. P13列表：一个打了激素的数组3

    member = [1, 2, 3]

   <font color=blue>1 in member</font>

   <font color=blue>10 not in member</font>

   <font color=blue>member.count(1)</font>

   .count()表示参数在列表中出现的次数

   <font color=blue>member.index(1)</font>

   .index()找到元素第一次出现的索引

   reverse()翻转列表

   sort()排序

   list = [x * 3 for x in range(10)]

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
   
   s为字符串
   
   s.isalnum() #所有字符都是数字或者字母
   
   s.isalpha() #所有字符都是字母
   
   s.isdigit()#所有字符都是数字
   
   s.islower()#所有字符都是小写
   
   s.isupper()#所有字符都是大写
   
   s.istitle()#所有单词都是首字母大写
   
   s.isspace()#所有字符都是空白字符

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