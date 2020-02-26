from MyQR import myqr #二维码
import time #时间模块

import matplotlib.pyplot as plt #图片显示
import matplotlib.image as mping

#判断是否包含中文字符串
def is_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
while True:
    
    code = input("请输入需要转为二维码的网址链接或字符串，不支持中文：")
    if is_contain_chinese(code):
        print("不支持中文，请重新输入！")
        continue
    fileName = time.strftime("%Y%m%d%H%M%S", time.localtime()) #格式化当前时间，作为文件名
    fileName += ".png"
    myqr.run(
        words = code,
        version = 5,
        level = 'H',
        contrast = 1.0,
        brightness = 1.0,
        save_name= fileName,
        )
    print("已将字符串:{}成功生成并保存二维码图片:{}".format(code, fileName))
    png = mping.imread(fileName) #读取图片文件
    plt.imshow(png)
    plt.axis("off")
    plt.title(code) #更改标题
    plt.show() #显示图片
