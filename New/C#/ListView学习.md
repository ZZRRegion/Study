# ListView类
1. 常用的基本属性
   - FullRowSelect:设置是否行选择模式.(默认为false)提示:只有在Details视图,该属性有效.
   - GridLines:设置行和列之间是否显示网格线.(默认为false)提示:只有在Details视图有效
   - AllowColumnReorder:设置是否可以拖动标头来更改列的顺序.(默认false)提示:只有在Details视图有效
   - View:获取或设置项在控件中的显示方式.包括Details,LargeIcon,List,SmallIcon,Tile(默认为LargeIcon)
   - MultiSelect:设置是否可以选择多个项.

2. 常用方法
   - BeginUpdate:避免在调用EndUpdate方法之前绘制控件.当插入大量数据时,可以有效地避免控件闪烁,并能大大提高速度.
   - EndUpdate:在BeginUpdate方式挂起描述后,继续描述列表视图控件.(结束更新)

更多详细内容可参考该[博客](https://www.cnblogs.com/shadowme/p/6250070.html)