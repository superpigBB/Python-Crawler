"""
Amazon China Crawler
"""
# import requests
# url = 'https://www.amazon.com/gp/product/B07T1GWF38/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1'
#
# try:
#     key_value = {'user-agent': 'Mozilla/5.0'}
#     r = requests.get(url, headers=key_value)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text[:10000])
# except:
#     print('failed to crawl anything there')

# """
# 百度搜索
# """
# import requests
# keyword = "Python"
#
# try:
#     kv = {'wd': keyword}
#     r = requests.get("http://www.baidu.com/s", params=kv)
#     print(r.request.url)
#     r.raise_for_status()
#     print(len(r.text))
#     print(r.text)
# except:
#     print("failed to crawl anything there")


"""
网络图片获取及保存
"""
import requests
import os
url = "https://c-ssl.duitang.com/uploads/item/201404/21/20140421074258_nERhe.jpeg"
root = '/Users/VickyBao/Documents/Python_Web_Crawler/pics_from_web/'
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)   # r.content是文件的二进制形式，所以用b打开
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
