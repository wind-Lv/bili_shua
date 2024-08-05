import requests
from fake_useragent import UserAgent
import ips
import time

def get_data(bvid) -> dict:
    '''
    bvid: 视频bv号
    '''
    url = f'http://api.bilibili.com/x/web-interface/view?bvid={bvid}'
    headers = {
        "User-Agent": UserAgent().random
    }
    req = requests.get(url,headers=headers).json()
    aid = req["data"]["aid"]
    cid = req["data"]["cid"]
    post_data = {"aid":aid,"cid":cid,"realtime":600,"played_time":600,"sub_type":0}
    return post_data

def report_heartbeat(post_data: dict, ip):
    '''
    progres:播放的时长 单位为秒
    '''
    ip_ = {'http':f'http://{ip}'}
    url = "https://api.bilibili.com/x/click-interface/web/heartbeat"
    headers = {"User-Agent":UserAgent().random}

    ret = requests.post(url=url, data=post_data, headers=headers,proxies=ip_).json()
    return ret

def run(bv:list, ips):
    '''
    bv: bv号
    ips: 代理ip
    '''
    ips = {"http":f"http://{ips}"}
    headers = {"User-Agent":UserAgent().random}
    try:
        requests.get("http://www.baidu.com",headers=headers,proxies=ips,timeout=3)
        for i in bv:
            date = get_data(i)
            ret = report_heartbeat(date,ips)
            print(ret)
            time.sleep(15)
    except requests.exceptions.ProxyError:
        pass #print('ip失效')
    except requests.exceptions.ReadTimeout:
        pass #print('timeout')
    except requests.exceptions.ChunkedEncodingError:
        pass #print('服务器拒绝')
    except requests.exceptions.TooManyRedirects:
        pass #print('服务器重新定向')

bv = [
    "BV1revfe7EL3",
    "BV1f3iTeNE6s",
    "BV1iVijeREYY",
    "BV1ftvaeqEzn",
    "BV1PCvWesEaq",
    "BV16avseDEzi",
]

if __name__ == '__main__':
    for i in ips.freeProxy1():
        run(bv,i)