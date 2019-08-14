import re
import os
import urllib
import time
import requests


def getPage(keyword, page, n):  # 获取路径
    page = page * n
    keyword = urllib.parse.quote(keyword, safe='/')
    url_begin = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
    url = url_begin + keyword + "&pn=" + str(page) + "&gsm=" + str(hex(page)) + "&ct=&ic=0&lm=-1&width=0&height=0"
    return url


def get_onepage_urls(onepageurl):  # 加载每页数据
    try:
        html = requests.get(onepageurl).text
    except Exception as e:
        print(e)
        pic_urls = []
        return pic_urls
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    return pic_urls


def down_pic(pic_urls, save_dir):
    """给出图片链接列表, 下载所有图片"""

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=15)
            string = str(i + 1) + '.jpg'
            with open(save_dir + "\\" + string, 'wb') as f:
                f.write(pic.content)
                print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
            print(e)
            continue
        time.sleep(0.1)


if __name__ == '__main__':
    keyword = '监控花屏图'  # 关键词, 改为你想输入的词即可, 相当于在百度图片里搜索一样
    save_dir = "D:\\img\\tiaowenganrao\\" + "\\" + keyword
    page_begin = 0  # 初始化拉取次数
    page_number = 50  # 每次拉取的图片数
    image_number = 10  # 最大拉取次数
    all_pic_urls = []
    while 1:
        if page_begin > image_number:
            break
        print("第%d次请求数据" % (page_begin + 1))
        try:
            url = getPage(keyword, page_begin, page_number)
        except:
            page_begin -= 1
            continue
        # 获取一页中的URL
        onepage_urls = get_onepage_urls(url)
        page_begin += 1
        # extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
        all_pic_urls.extend(onepage_urls)
    # 下载所有的图片
    down_pic(list(set(all_pic_urls)), save_dir)
    # print(all_pic_urls)
