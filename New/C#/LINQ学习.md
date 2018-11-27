# LINQ巩固
1. LINQ过滤运算符
   Where 基于谓词函数过滤值  
   测试例子如下:
``` C#
public class TestModel
{
    public string Name { get; set; }
    public string Age { get; set; }
}

 List<TestModel> lst = new List<TestModel>()
            {
                new TestModel(){Name = "张三" },
                new TestModel(){Name = "李四" },
            };
var querys1 = from item in lst where item.Name == "李四" select item;
var querys2 = lst.Where(item => item.Name == "李四");
```
2. LINQ Join操作  
   
!运算符|描述|查询语法|
|---|---|---|
|Join|运算符连接两个序列配键的基础|join...in...on...equals...|
|GroupJoin|连接连个序列和组匹配元素|join...in...on...equals...into|
测试例子：   

···  C#
List<TestModel> lst = new List<TestModel>()

            {
                new TestModel(){Name = "张三", Age = "23" },
                new TestModel(){Name = "李四", Age = "43" },
            };
            List<CameraModel> lstCamera = new List<CameraModel>()
            {
                new CameraModel(){Name = "张三", Price = "sfsf" },
                new CameraModel(){Name = "张三", Price = "测试工程时" },
                new CameraModel(){Name = "李四", Price = "买菜的" }
            };
var query = from it in lst
            join item in lstCamera on it.Name equals item.Name
            select new
            {
                it.Name,
                it.Age,
                item.Price
            };  

···

3. LINQ投影操作  

|运算符|描述|
|---|---|
|Select|操作转换函数的基础项目值|
|SelectMany|操作项目的值是根据上的转换函数，以及拼合成一个单一的序列的序列|

``` C#
var querys = from ite in lst from item in lstCamera select ite;
```
4. LINQ排序运算符  

|操作符|描述|
|---|---|
|OrderBy|按升序操作排序值|
|OrderByDescending|按降序排序操作值|
|ThenBy|执行二次元排序按升序|
|ThenByDescending|执行二次排序以降序|
|Reverse|进行反转的元素顺序|
5. LINQ分组操作

|操作|描述|
|---|---|
|GroupBy|组织项目的顺序组，并将其返回IEnumerable类型的集合|
|ToLookup|执行在其中的密钥对的序列被返回分组运算|
5. LINQ转换操作

|操作符|描述|
|---|---|
|AsEnumerable|返回输入类型为IEnumerable T|
|AsQueryable|IEnumerable被转换为IQueryable|
|Case|执行一个集合的元素的转换到一个指定类型|
|OfType|在它们的基础上过滤值，这取决于它们的能力，以被转换为特定类型|
|ToArray|转换为数组|
|ToDictionary|转为字典|
|ToList|转为列表|
|ToLookup|强制执行查询，并把元素融入一个Lookup TKey,TElement键选择器函数|

6. LINE级联

|操作符|描述|
|---|---|
|Concat|两个序列被连接为一个单一的一个序列|
 
7. LINQ聚合

|操作|描述|
|---|---|
|Aggergate|对集合的值进行操作执行自定义聚合操作|
|Average|计算集合的平均值|
|Count|计算数量|
|LongCount()|计算一个巨大集合中的数量|
|Max|找出一个集合中的最大值|
|Min|找出一个最小值|
|Sum|计算总和|

8. LINQ量词操作

|操作|描述|
|---|---|
|All|返回一个值'true'，如果序列中的所有元素满足谓词条件|
|Any|确定通过搜索一个序列是否相同的任何元素满足规定条件|
|Contains|如果找到某个特定元素有一个序列返回一个'true'的值，如果序列不包含特定的元素，'false‘值返回|

9. LINQ分区操作符

|操作|描述|
|---|---|
|Skip|跳过一些指定的序列中一些元素，并返回其余的|
|SkipWhile|相同，唯一的例外调到多个元素，跳过的是由一个布尔条件指定|
|Take|采取元素指定数量的序列，并跳过其余的|
|TakeWhile|相同，布尔条件指定|

10. LINQ元素操作符

|操作|描述|
|---|---|
|ElementAt|返回一个特定的索引中的一个元素存在于一个集合|
|ElementAtOrDefault|相同与ElementAt，未找到返回默认值|
|First|检索集合的满足的第一个元素|
|FirstOrDefault|相同，未检索到返回默认值|
|Last|用法同上|
|LastOrDefault|同上|
|Single|返回集合唯一元素或唯一元素满足的一定条件|
|SingleOrDefault|不解释|