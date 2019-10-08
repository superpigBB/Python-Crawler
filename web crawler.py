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

"""
百度搜索
"""
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
# import requests
# import os
# url = "https://c-ssl.duitang.com/uploads/item/201404/21/20140421074258_nERhe.jpeg"
# root = '/Users/VickyBao/Documents/Python_Web_Crawler/pics_from_web/'
# path = root + url.split('/')[-1]
#
# try:
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#         r = requests.get(url)
#         with open(path, 'wb') as f:
#             f.write(r.content)   # r.content是文件的二进制形式，所以用b打开
#             f.close()
#             print("文件保存成功")
#     else:
#         print("文件已存在")
# except:
#     print("爬取失败")


"""
ip地址归属地查询: utilize website: ip138
"""
# # import requests
# # url = 'http://m.ip138.com/ip.asp?ip='
# # r = requests.get(url + '202.204.80.112')
# # print(r.status_code)
# # print(r.text[-500:])
#
# """
# Beautiful Soup： 解析html/xml/...等标签类型数据
# example: http://python123.io/ws/demo.html
# """
# import requests
# r = requests.get('http://python123.io/ws/demo.html')
# demo = r.text
# # print(f'{demo}\n------------')
#
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(demo, 'html.parser')
# print(soup.prettify())
#
# # print(f"tag a name: {soup.a.name}; tag a's parents' name:{soup.a.parent.name}"
# #       f" tag a's grandparents'name: {soup.a.parent.parent.name}")
#
# # tag's attributes
# tag = soup.a
# print(f"tag a's attributes: {tag.attrs}")
# print(tag.attrs['class'])
# type(tag.attrs)  #dict
# type(tag)   #tag
#
# # tag's navigable string
# tag.string  # Basic Python
# type(soup.p.string)   # NavigableString
#
# # tag's Comment
# """
# <! 代表comment的开头
# """
# newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")
# print(type(newsoup.b.string))  # Comment type
# print(type(newsoup.p.string))  # Navigable String

"""
Example: 提取HTML中所有URL链接
1)搜索所有<a>标签
2）解析<a>标签格式，提取href后的链接内容
html: view-source:https://python123.io/ws/demo.html
"""
from bs4 import BeautifulSoup
import requests
r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))