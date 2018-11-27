@echo off
echo 添加所有文件中...
git add *
echo 添加完毕!
echo 请输入提交描述=
set /p memo=
git commit -m %memo%  
echo 提交完毕!
echo 推送到远程
git push origin master
echo 推送完成!