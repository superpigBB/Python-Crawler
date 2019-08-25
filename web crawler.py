"""
Amazon China Crawler
"""
import requests
url = 'https://www.amazon.com/gp/product/B07T1GWF38/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1'

try:
    key_value = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=key_value)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:10000])
except:
    print('failed to crawl anything there')


