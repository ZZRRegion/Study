![git](https://cdn.liaoxuefeng.com/cdn/files/attachments/0013848605496402772ffdb6ab448deb7eef7baa124171b000/0)  
写这篇主要是为了我做一个学习的记录，对于学习一个新的知识，我觉的还是记录一些东西对于知识点会更加清晰，故逐渐的我就保持学习一个新的知识时，我就开始做记录，也培养培养自己用文字描述一个事情的能力，话说这个过程是真的很难受，咱真真不善于表达。  
Git是目前世界上最先进的分布式版本控制系统  
Git真的是高端大气上档次，分支秒切，真真惊艳到咱了。  
更惊讶的是，Linus大神只花了两周时间用C写的，一个月之内容，LInux系统的源码就由Git管理了！
本文主要参考[廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
# 集中式Vs分布式
## 集中式图  
![集中式](https://cdn.liaoxuefeng.com/cdn/files/attachments/001384860735706fd4c70aa2ce24b45a8ade85109b0222b000/0)  
## 分布式图  
![分布式](https://cdn.liaoxuefeng.com/cdn/files/attachments/0013848607465969378d7e6d5e6452d8161cf472f835523000/0)
### 创建版本库
版本库又名仓库，英文名为repository,可以简单理解成一个目录，这个目录里面的所有文件都可以被git管理，每个文件的修改、删除、Git都能跟踪，以便于任何时刻都可以追踪历史，或者还原。  
创建一个版本库非常简单，首先，旋转一个合适的地方，创建一个空的目录：  
mdkir test
cd test  
第二部，通过git init命令把这个目录变成Git可以管理的仓库：
git init
瞬间就把仓库建好了，是一个空的仓库  
然后就可以在该目录下新建文件可以管理了  
使用git add命令来添加文件到仓库  
git add readme.md  
执行上面的命令，没有任何显示就对了，Unix的哲学是”没有消息就是好消息“，说明添加成功  
第二步，用命令git commit告诉git，把文件提交到仓库。  
> git commit -m '描述一下'  

git commit命令，-m后面输入的是本次提交的说明，可以输入任意内容，这个你就能从历史记录f方便的找到改动记录。
可以继续修改文件内容，然后使用git status命令查看结果  
git status命令可以让我们时刻了解仓库当前的状态。
可以使用命令git diff查看
git diff是查看difference，显示的格式是unix通用的diff格式  
git log查看历史记录
git log --pretty=oneline可以看得舒服一些  
这里看到的一串类似1094adc...的是commit id（版本号)  
每提交一个新版本，实际上git就会把它们串成一条时间线。  
git reset --hard HEAD^回退到上一个版本  
git reset --hard 1094a (commit id版本号)即可回退到指定版本  
git reflog 会显示每一次的命令  
**版本库**
![版本库图](https://cdn.liaoxuefeng.com/cdn/files/attachments/001384907702917346729e9afbf4127b6dfbae9207af016000/0)