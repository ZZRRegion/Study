# Vue生命周期
参考[vue生命周期](http://www.cnblogs.com/gagag/p/6246493.html)  
![Vue生命周期](https://images2015.cnblogs.com/blog/1064935/201701/1064935-20170103204551597-1413099760.png)  
这是Vue文档里关于实例生命周期的解释图  
进行测试一下
测试代码如下:
``` HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="https://unpkg.com/vue/dist/vue.js"></script>
</head>
<body>
    <div id="app">
        {{data}}
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
                data: "这是测试",
                info: "none"
            },
            beforeCreate() {
                console.log("创建前=======");
                console.log(this.data);
                console.log(this.$el);
                console.log("这是一条分割线==========");
            },
            created() {
                console.log("已创建=========");
                console.log(this.data);
                console.log(this.$el);
                console.log("这是一条分割线==========");
            },
            beforeMount() {
                console.log("mount之前==========");
                console.log(this.info);
                console.log(this.$el);
                console.log("这是一条分割线==========");
            },
            mounted() {
                console.log("mounted======");
                console.log(this.info);
                console.log(this.$el);
                console.log("这是一条分割线==========");
            },
            beforeUpdate() {
                console.log("更新前=========");
                console.log("这是一条分割线==========");
            },
            updated() {
                console.log("更新完成=======");
                console.log("这是一条分割线==========");
            },
            beforeDestroy() {
                console.log("销毁前========");
                console.log(this.info);
                console.log(this.$el);
                console.log("这是一条分割线==========");
            },
            destroyed() {
                console.log("已销毁=========");
                console.log(this.info);
                console.log(this.$el);
                console.log("这是一条分割线==========");
            },
        })
    </script>
</body>
</html>
```
结果图:
![结果图](https://alicliimg.clewm.net/264/935/3935264/15339977675168915a23e51387901b913689566e0e7421533997750.png)
由图可知:
1. beforeCreate此时$el,data的值都为undefined
2. 创建之后,此时可以拿到data的值,但是$el依旧为undefined
3. mount之前,$el的值为"虚拟"的元素节点
4. mount之后,mounted之前,"虚拟"的dom节点被真是的dom节点替换,并将其插入到dom树中,于是在出发mounted时,可以获取到$el为真实的dom元素 app.$el === document.getElementById("app")//true

继续,现在修改data的值,更新视图:
![更新后](https://alicliimg.clewm.net/264/935/3935264/153399830070071da6115269e16567b07650bbf22d7b01533998297.png)  
触发了beforeUpdate和updated  
接着,继续执行销毁app.$destroy()
![销毁后](https://alicliimg.clewm.net/264/935/3935264/153399844437571da6115269e16567b07650bbf22d7b01533998297.png)  
总结一下,简化后的图为:
![简化生命周期图](https://images2015.cnblogs.com/blog/1064935/201701/1064935-20170103211421987-2119701214.png)