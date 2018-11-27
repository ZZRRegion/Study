# 通过API获取BootCDN所加速的所有前端开源库的基本信息和文件列表  
## **API**
> 将一下API链接中的.min字样去掉后,获取到的JSON格式的返回信息是经过良好的格式化的,便于查看.  

**所有开源库简要信息列表**
> https://api.bootcdn.cn/libraries.min.json   

该列表是一个json数组,数组中的每一个条目是由开源库的名称(name),描述,星标数组成的数组.  
``` C#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;

namespace BootCDNAPIDemo
{
    /// <summary>
    /// 开源库简要信息列表
    /// </summary>
    public class LibrariesModels
    {
        public List<LibrariesModel> ListLibraries { get; set; } = new List<LibrariesModel>();
        public LibrariesModels(string content)
        {
            JArray json = JArray.Parse(content);
            foreach(JArray jitem in json)
            {
                LibrariesModel model = new LibrariesModel(jitem);
                this.ListLibraries.Add(model);
            }
        }
    }
    public class LibrariesModel
    {
        public string name { get; set; }
        public string desc { get; set; }
        public string stars { get; set; }
        public LibrariesModel(JArray jitem)
        {
            this.name = jitem[0].ToString();
            this.desc = jitem[1].ToString();
            this.stars = jitem[2].ToString();
        }
        public override string ToString()
        {
            return this.name;
        }
    }
}

```
**获取某个开源库的详细信息**  

> https://api.bootcdn.cn/libraries/[name].min.json  

通过此接口获取到的是开源库的json对象格式的详细信息,包括所有版本以及文件列表.其中,assets属性是所有版本及对应文件的列表.
``` C#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BootCDNAPIDemo
{
    public class DetailedModel
    {
        public string name { get; set; }
        public string npmName { get; set; }
        public string version { get; set; }
        public string description { get; set; }
        public string homepage { get; set; }
        public List<string> keywords { get; set; }
        public string license { get; set; }
        public Repository repository { get; set; }
        public List<Asset> assets { get; set; }
        public string stars { get; set; }
    }
    public class Repository
    {
        public string type { get; set; }
        public string url { get; set; }
    }
    public class Asset
    {
        public string version { get; set; }
        public List<string> files { get; set; }
    }
}

```
Github:[ZZRRegion/BootCDNAPIDemo](https://github.com/ZZRRegion/BootCDNAPIDemo.git)