import bili_req
import ips
import time
bv = input('bv>')

def wen():
    '''
    稳定刷
    '''
    while True:
        bili_req.run(bv,ips.freeProxy4())
        time.sleep(1200)

#bili_req.run(bv,ips.freeProxy1())
#bili_req.run(bv,ips.freeProxy2())
#bili_req.run(bv,ips.freeProxy3(6000))
#bili_req.run(bv,ips.freeProxy5())