# 导入模块
import os
from PIL import Image
import time


def image_processing(name):
    if name.endswith('jpg') or name.endswith('jpeg') or name.endswith('png'):
        im = Image.open(name)
        w, h = im.size
        if max(w, h) < 1200 and min(w, h) < 900:
            return 
        print('Original image size: %sx%s' % (w, h))
        if w > h:
            if h * 1200 / w > 900:
                n = h / 900
            else:
                n = w / 1200
            im.thumbnail((w / n, h / n))
        else:
            if h * 900 / w > 1200:
                n = h / 1200
            else:
                n = w / 900
            im.thumbnail((w / n, h / n))
        print('Resize image to: %sx%s' % (w / n, h / n))
        im.save(name)
        
if __name__ == "__main__":
    print("请先确认已将修改图片大小.exe文件与待处理图片在同一个文件夹下")
    flag = input("运行此程序，将会直接修改原有图片尺寸，继续请输入1，退出请输入2->")
    if flag == "1":
        for name in os.listdir():
            image_processing(name)

    print("Successful!")
    time.sleep(5)
    
