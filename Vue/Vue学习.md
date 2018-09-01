# Vue学习
Vue的目标是通过尽可能简单的API实现响应的数据绑定和组合的视图组件.   
## Vue.js安装  
[下载Vue.js](https://cdn.bootcss.com/vue/2.5.17-beta.0/vue.js)  
``` HTML
<script src="https://cdn.bootcss.com/vue/2.5.17-beta.0/vue.js"></script>
```  
## Vue.js起步  
每个Vue应用都需要通过实例化Vue来实现.  
语法格式如下:  
``` JavaScript
var app = new Vue({
    //选项
})
```  
实例:
``` HTML
 <div id="app">
            <h1>site:{{site}}</h1>
            <h1>url:{{url}}</h1>
            <h1>{{details()}}</h1>
</div>
<script>
    var app = new Vue({
        el: "#app",
        data: {
            site: '我的',
            url: 'www.baidu.com',
        },
        methods: {
            details: function(){
                return "hello world";
            }
        }
    })
</script>
```  
可以看到在Vue构造器中有一个el参数,它是DOM元素中的id.在上面实例中id为app.在div元素中.  
这意味着我们接下来的改动全部在指定的div内.div外部不受影响.  
data用于定义属性,实例中有属性:site,url.  
methods用于定义函数,可以通过return来返回函数.  
{{}}用于输出对象属性和函数返回值.   
## Vue.js模板语法  
### **插值**
### 文本  
数据绑定最常见的形式就是使用{{}}的文本插值:  
文本插值  
``` HTML
<div id="app">
    {{message}}
</div>
```
Html  
使用v-html指令用于输出html代码:  
v-html指令  
``` HTML
<div v-html="html">

</div>
var app = new Vue({
            el: "#app",
            data: {
                site: '我的',
                url: 'www.baidu.com',
                html:"<h1 style='color: red;'>这是v-html内容</h1>"
            },
            methods: {
                details: function(){
                    return "hello world";
                }
            }
        })
```
属性  
HTML属性中的值应使用v-bind指令.  
以下实例判断class1的值,如果为true使用class1类的样式.否则不使用该类:  
``` HTML
<style>
        .wo {
            color: red;
        }
        .ni {
            color: blue;
        }
    </style>
     <div id="app">
            <div v-bind:class="{'wo':wo, 'ni': !wo}">
                <p>测试v-bind</p>
            </div>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
                wo: true
            },
        })
    </script>
```  
表达式  
表达式实例:
``` HTML
<div id="app">
        <div>{{10 + 10}}</div>
        <div>{{ok ? '海' : '唐'}}</div>
        <div>{{message.split('').reverse().join('')}}</div>
        <div v-bind:id="'list-' + id">才子</div>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
                message: "hello world",
                id: 110,
                ok: true
            },
        })
    </script>
```  
指令  
指令是带有v-前缀的特殊属性.  
指令用于在表达式的值改变时,将某些行为应用到DOM上.如下例子:  
``` HTML
<div id="app">
        <div v-if="wo">这是现实</div>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
               wo: true
            },
        })
    </script>
```  
参数  
参数在指令后以冒号指明.例如,v-bind指令被用来响应地更新HTML属性.   
``` HTML
<div id="app">
        <a v-bind:href="url">教程</a>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
               url: "http://www.baidu.com"
            },
        })
    </script>
```  
另一个例子是v-on指令,它用于监听DOM事件:
``` HTML
<a v-on:click="doSome">
```  
**修饰符**  
修饰符是以半角句号,指明的特殊后缀,用于指出一个指令应该以特殊方式绑定.例如,.prevent修饰符告诉v-on指令对于触发的事件调用event.preventDefault():
``` HTML
<form v-on:submit.prevent="onSubmit"></form>
```
**用户输入**  
在input输入框中我们可以使用v-model指令来实现双向数据绑定:  
``` HTML
 <div id="app">
        <a v-bind:href="url">教程</a>
        <input v-model="wo">
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
               url: "http://www.baidu.com",
               wo: "test"
            },
        })
    </script>
```  
按钮的事件可以使用v-on监听事件,并对用户的输入进行响应.  
``` HTML
<div id="app">
        <input v-model="wo">
        <button v-on:click="click">很好</button>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
               url: "http://www.baidu.com",
               wo: "test"
            },
            methods: {
                click: function(){
                    this.wo = "我们";
                }
            }
        })
    </script>
```  
**过滤器**  
Vue.js允许你自定义过滤器,被用作一些常见的文本格式化.由"管道符"指示,格式如下:  
``` HTML
<div id="app">
        <div>{{message|cap}}</div>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
              message: 'hai'
            },
            methods: {
                
            },
            filters:{
                cap: function(value){
                    if(!value) return '';
                    value = value.toString();
                    return value.charAt(0).toUpperCase() + value.slice(1);
                }
            }
        })
    </script>
```  
**缩写**  
v-bind缩写  
``` HTML
<a v-bind:href="url"></a>

<a :href="url"></a>
```  
v-on缩写  
``` HTML
<a v-on:click="doSome"></a>

<a @click="doSome"></a>
```  
## 循环语句
循环使用v-for指令.  
v-for指令需要以site in sites形式的特殊语法,sites是元数据数组并且site是数组元素迭代的别名.  
v-for可以绑定数据到数组来渲染一个列表.  
``` HTML
<div id="app">
       <ol>
           <li v-for="site in sites">
               {{site.name}}
           </li>
       </ol>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
              sites: [
                  {"name":"第一个"},
                  {"name":"第二个"},
                  {"name":"第三个"}
              ]
            },
   
        })
    </script>
```  
可以提供第二个的参数为键名:  
``` HTML
<div id="app">
       <ul>
           <li v-for="(site, key) in sites">
               {{key}} {{site.name}}
           </li>
       </ul>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
              sites: [
                  {"name":"第一个"},
                  {"name":"第二个"},
                  {"name":"第三个"}
              ]
            },
   
        })
    </script>
```  
第三个参数为索引:  
``` HTML
 <div id="app">
       <ul>
           <li v-for="(site, key, index) in sites">
               {{key}} {{site}} {{index}}
           </li>
       </ul>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
              sites: {"one":"第一", "two": "第二", "th": "TH"}
            },
   
        })
    </script>
```  
v-for迭代整数  
``` HTML
<div id="app">
       <ul>
           <li v-for="it in 10">
               {{it}}
            </li>
       </ul>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
              sites: {"one":"第一", "two": "第二", "th": "TH"}
            },
   
        })
    </script>
```  
v-for循环数组:
``` HTML
<div id="app">
       <ul>
           <li v-for="it in [10, 20, 30]">
               {{it}}
            </li>
       </ul>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
              sites: {"one":"第一", "two": "第二", "th": "TH"}
            },
   
        })
    </script>
```  
## Vue.js计算属性  
计算属性关键字:computed.  
计算属性在处理一些复杂逻辑时是很有用的.  
可以看下以下反转字符串的列子:
``` HTML
<div id="app">
      <p>原始字符串:{{message}}</p>
      <p>计算后反转字符串:{{reversedMessage}}</p>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
                message: "Runoob"
            },
            computed: {
                reversedMessage: function(){
                    return this.message.split('').reverse().join('');
                }
            }
        })
    </script>
```  
## Vue.js组件
注册一个全局组件语法格式如下:
``` JavaScript
Vue.component(tagName, options)
```  
tagName为组件名,options为配置选项.注册后,我们可以使用以下方式来调用组件:
``` HTML
<tagName></tagName>
```  
全局组件  
``` HTML
 <div id="app">
        <wo></wo>
    </div>
    <script>
        Vue.component("wo", {
            template: '<h1>这是自定义组件</h1>'
        });
        var app = new Vue({
            el: "#app",
        })
    </script>
```  
局部组件  
``` HTML
<div id="app">
        <wo></wo>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            components: {
                'wo': {
                    template: '<h1>这是自定义</h1>'
                }
            }
        })
    </script>
```  
Prop  
prop是父组件用来传递数据的一个自定义属性.  
父组件的数据需要通过props把数据传给子组件,子组件需要显式地使用props选项声明"prop":  
``` HTML
<div id="app">
        <wo message="这是传参"></wo>
    </div>
    <script>
        Vue.component("wo", {
            template: '<h1>这是自定义组件{{message}}</h1>',
            props:['message']
        
        });
        var app = new Vue({
            el: "#app",
        })
    </script>
```  
动态Prop  
类似于用v-bind绑定HTML特性到一个表达式,也可以用v-bind动态绑定props的值到父组件的数据中.每当父组件的数据变化时,该变化也会传导给子组件:  
``` HTML
<div id="app">
        <wo v-bind:message="message"></wo>
    </div>
    <script>
        Vue.component("wo", {
            template: '<h1>这是自定义组件{{message}}</h1>',
            props:['message']
        
        });
        var app = new Vue({
            el: "#app",
            data: {
                message: "消息"
            }
        })
    </script>
```  

