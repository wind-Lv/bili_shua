import time
import requests
from fake_useragent import UserAgent
import time

url = "http://api.bilibili.com/x/click-interface/click/web/h5"
susseed_num = 0

def requests_shua(ip,data):
    global susseed_num
    bv = 'BV1hd4y1p7mE'
    reqdata = []
    headers = {
    'User-Agent':UserAgent().random,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://www.bilibili.com',
    'Connection': 'keep-alive'
    }
    proxy = {
        'http':f'http://{ip}'
    }
    try:
        a = requests.post(url,headers=headers,data=data[0],proxies=proxy,timeout=3)
        if a.status_code == 200:
            susseed_num += 1
            print(f'成功数:{susseed_num}')
            time.sleep(30)
    except requests.exceptions.ProxyError:
        pass #print('ip失效')
    except requests.exceptions.ReadTimeout:
        pass #print('timeout')
    except requests.exceptions.ChunkedEncodingError:
        pass #print('服务器拒绝')
    except requests.exceptions.TooManyRedirects:
        pass #print('服务器重新定向')



def get_data(bv):
    '''
    bv: bv号
    ip_source: IP源头 
    '''
    reqdata = []
    stime = str(int(time.time()))
    headers = {
        'User-Agent':UserAgent().random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'https://www.bilibili.com',
        'Connection': 'keep-alive'
    }
    resp = requests.get("http://api.bilibili.com/x/web-interface/view?bvid={}".format(bv),headers=headers)
    resp_json = resp.json()
    if "data" in resp_json:
        getdata = resp_json["data"]
    data= {
        'aid':getdata["aid"],
        'cid':getdata["cid"],
        "bvid": bv,
        'part':'1',
        'mid':getdata["owner"]["mid"],
        'lv':'6',
        "stime" :stime,
        'jsonp':'jsonp',
        'type':'3',
        'sub_type':'0',
        'title': getdata["title"]
    }
    reqdata.append(data)
    return reqdata

def run(bv,source):
    a = get_data(bv)
    for i in source:
        requests_shua(ip=i,data=a)

if __name__ == '__main__':
    import ips
    run('BV1ftvaeqEzn',ips.freeProxy5())