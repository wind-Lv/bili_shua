import requests
import json
from lxml import etree
from datetime import datetime
'''
输出的ip统一为xxx.xxx.xxx:xxxx格式

'''
header = {
        "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}
def freeProxy1():
    '''
    可用率高 少
    '''
    res = requests.get(
        'https://www.docip.net/data/free.json'
        ).text
    j = json.loads(res)
    for i in j['data']:
        yield i['ip']

def freeProxy2():
    '''
    少
    '''
    res = requests.get(
        f"http://www.kxdaili.com/dailiip/1/1.html"
    ).text
    x = etree.HTML(res)
    for i in x.xpath("//table[@class='active']//tr"):
        try:
            ip = i.xpath("./td[1]/text()")[0]
            port = i.xpath("./td[2]/text()")[0]
        except IndexError:
            pass
        try:
            yield f'{ip}:{port}'
        except UnboundLocalError:
            pass


def freeProxy3(num):
    '''
    量大
    https://www.89ip.cn/api.html 此处可更新代理ip
    num: ip数
    '''
    l = []
    res = requests.get(
        f"http://api.89ip.cn/tqdl.html?api=1&num={num}&port=&address=&isp=",
        headers=header
    ).text
    x = etree.HTML(res)
    for i in range(4,num):
        try:
            ips = x.xpath(f'/html/body/text()[{i}]')[0]
            l.append(ips)
        except:
            pass
    return l

def freeProxy4():
    '''
    最高效 20分钟更新一次 但少
    '''
    res = requests.get(
        "https://api.zhyunxi.com/api.php?api=28&key=8a2119d8bfbd8a3eec89e4f477d3b4b6"
    ).text
    api_json = json.loads(res)
    ip_list = api_json['data'][0]['list']
    for i in ip_list:
        yield i

def freeProxy5():
    '''
    量大
    '''
    t = datetime.now().date()
    url = f'https://checkerproxy.net/api/archive/{t}'
    res = requests.get(url,headers=header).text
    j = json.loads(res)
    for i in j:
        yield i['addr']

if __name__ == '__main__':
    #for i in freeProxy3():
    #    print(i)
    for i in freeProxy5():
        print(i)