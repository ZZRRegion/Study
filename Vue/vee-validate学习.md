# Vee-validate使用方法
首先引入
``` HTML
<script src="https://cdn.bootcss.com/vee-validate/2.0.9/vee-validate.js"></script>
<script src="https://cdn.bootcss.com/vee-validate/2.0.9/locale/zh_CN.js"></script>
```
然后在VUE中使用
``` JS
 Vue.use(VeeValidate);
 ```
 简单例子:
 ``` HTML
 <div>
    <label for="email">邮箱：</label>
    <input v-validate ="'required|email'" type="text" name="myEmail">
</div>
<span v-show="errors.has('myEmail')">{{ errors.first('myEmail')}}</span>
```
v-validate后面的required和email是官方提供的几种默认错误类型中的两个.  
span中用到了errors的几个方法,这里的参数都是定义了验证规则的表单的name.列举几个errors的方法:
1. first('field')  
   field中的第一个错误  
2. collect('field')  
   field中所有的错误  
3. has('field')  
   field中是否有错误  
4. all()  
   当前表单中的所有错误  
5. any()  
   当前表单中是否有错误  
6. count()  
   当前表单中的错误数量  
7. clear()  
   清除当前表单中的所有错误  
## 使用中文提示
``` JS
 var Validator = VeeValidate.Validator;
Vue.use(VeeValidate, {
    locale: 'zh_CN'
});
Validator.locale = "zh_CN";
Validator.localize(Validator.locale, {
    messages: window.__vee_validate_locale__zh_CN.js.messages
})
```
## 修改默认的错误提示信息
``` JS
 Validator.dictionary.container.zh_CN.messages.email = function(name){
            return name + "这个邮箱格式不正确哦!";
        }
```
## 内置的校验规则
- after{target} 比target要大的一个合法日期,格式(DD/MM/YYYY)  
- alpha 只包含英文字符
- alpha_dash 可以包含英文,数字,下划线,破折号 
- alpha_num 可以包含英文和数字
- before:{target} 和after相反
- between:{min},{max}  在min和max之间的数字
- confirmed:{target} 必须和target一样
- date_between:{min,max} 日期在min和max之间
- date_format:{format} 合法的format格式化日期
- decimal:{decimals} 数字,而且是decimals进制
- digits: {length} 长度为length的数字
- dimentsions: {width},{height}符合宽度规定的图片
- email 邮箱验证
- ext:[extensions] 后缀名
- image 图片
- in:[list] 包含在数组list内的值
- ip Ipv4地址
- max:{length} 最大长度为length的字符
- mimes:[list] 文件类型
- min: max相反
- mot_in: in相反
- numeric 只允许数字
- regex:{pattern} 值必须符合正则
- required: 必须
- size:{kb} 文件大小不超过
- url:{domain} 指定域名的url

## 自定义规则
``` JS
Validator.extend("hello", {
            messages:{
                zh_CN:field => field + "必须是11位",
            },
            validate: value => {
                console.log("ssdfds");
                return value == "123";
            }
        });
        Validator.dictionary.container.zh_CN.messages.hello = function(name){
            return name + "这个不对!";
        }
```