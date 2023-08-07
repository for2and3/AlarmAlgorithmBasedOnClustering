import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
import time

r = redis.Redis()
event = ['event:p0', 'event:p1', 'event:p2', 'event:p3', 'event:p4', 'event:p5', 'event:p6']
event_al = ['event:p00', 'event:p01', 'event:p02', 'event:p03', 'event:p04', 'event:p05', 'event:p06']

# 每n秒执行一次
def timer(n):
    i = 0
    while i < 3:
        f = open('event_t1.txt', 'w')
        for e in range(event.__len__()):
            l = r.llen(event[e])
            for i in range(l):
                p = r.blpop(event[e], 10)
                p = str(p[1], encoding = "utf8")
                # r.rpush(event_al[e], p[1])
                f.write(p)
                f.write('\n')
        f.close()
        time.sleep(n)
        i = i+1
timer(60)