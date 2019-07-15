# -*- coding: utf-8 -*-
from PIL import Image
import os
from gevent import monkey

monkey.patch_all()
import os
from gevent.pool import Pool


# 改变图片的大小
def changeImgSize(name):
    Img_path = File_dir + name
    img = Image.open(Img_path)
    print(Img_path)
    img_name = Img_path.split('\\')[-1]
    print("开始处理图片！！！！！！")
    (x, y) = img.size
    if y > 600:
        # 如果图片的尺寸大于600则将其改为600
        y_n = 600
        x_n = 600
        # x_n = int(x * y_n / y)
    else:
        x_n = x
        y_n = y

    New_Img = img.resize((x_n, y_n), Image.ANTIALIAS)
    Out_path = Save_Dir + img_name
    New_Img.save(Out_path)
    print("处理图片结束！！！！！！")


if __name__ == '__main__':
    global File_dir
    # File_dir 为给定的绝对路径
    File_dir = "C:\\Users\\samsung\\Desktop\\Collection\\KouTing\entity\\"
    # File_dir = os.getcwd() + "/pictures/"
    # 新建的目录路径
    global Save_dir
    Save_Dir = os.getcwd() + "\\Picoutput\\"
    if not os.path.exists(Save_Dir):
        os.mkdir(Save_Dir)  # 新建目录

    filenames = os.listdir(File_dir)

    pool = Pool(5)
    # for i in range(len(filenames)):
    pool.map(changeImgSize, filenames)
