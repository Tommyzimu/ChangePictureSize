import os


# 获取所有的目录
def file_dirs(file_path):
    file_names = []
    for file_name in os.listdir(file_path):
        new_path = os.path.join(file_path, file_name)
        if os.path.isdir(new_path):
            file_names.append(file_name)
    return file_names


def change_pic_name(name_list):
    tes_list = []
    for name in name_list:
        pic_path = base_path + name + '\\'
        pic_names = os.listdir(pic_path)
        i = 0
        for item in pic_names:
            src = os.path.join(os.path.abspath(pic_path), item)  # 原图片地址
            # print(src)
            dst = os.path.join(os.path.abspath(pic_path), name + str(i + 1) + ".jpg")
            # print(dst)
            # print(item)
            tes_list.append(item)
            try:
                os.rename(src, dst)
                i += 1
            except Exception as e:
                print(e)
                continue
    print("Rename picture finished & total converted %d:" % len(tes_list))


if __name__ == '__main__':
    base_path = r'D:\img\tiaowenganrao\\'
    # print(file_dirs(base_path))
    name_li = file_dirs(base_path)
    change_pic_name(name_li)
