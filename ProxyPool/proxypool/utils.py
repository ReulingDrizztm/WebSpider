import re

import requests
from requests.exceptions import ConnectionError

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}


def get_page(url, options={}):
    """
    抓取代理
    :param url:
    :param options:
    :return:
    """
    headers = dict(base_headers, **options)
    print('正在抓取', url)
    try:
        response = requests.get(url, headers=headers)
        print('抓取成功', url, response.status_code)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('抓取失败', url)
        return None


# for i in range(1, 3):
#     start_url = 'http://www.xicidaili.com/nn/{}'.format(i)
#     headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWRjYzc5MmM1MTBiMDMzYTUzNTZjNzA4NjBhNWRjZjliBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUp6S2tXT3g5a0FCT01ndzlmWWZqRVJNek1WanRuUDBCbTJUN21GMTBKd3M9BjsARg%3D%3D--2a69429cb2115c6a0cc9a86e0ebe2800c0d471b3',
#         'Host': 'www.xicidaili.com',
#         'Referer': 'http://www.xicidaili.com/nn/3',
#         'Upgrade-Insecure-Requests': '1',
#     }
#     html = get_page(start_url, options=headers)
#     # print(html)
#     if html:
#         find_trs = re.compile('<tr class.*?>(.*?)</tr>', re.S)
#         trs = find_trs.findall(html)
#         for tr in trs:
#             find_ip = re.compile('<td>(\d+\.\d+\.\d+\.\d+)</td>')
#             re_ip_address = find_ip.findall(tr)
#             find_port = re.compile('<td>(\d+)</td>')
#             re_port = find_port.findall(tr)
#             for address, port in zip(re_ip_address, re_port):
#                 address_port = address + ':' + port
#                 # yield address_port.replace(' ', '')
#                 print(address_port)
