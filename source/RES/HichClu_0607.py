from sklearn.cluster import AgglomerativeClustering
import numpy as np
from test import DataTreating
import time
import json
import redis
import os

event_b = ['event:p00', 'event:p01', 'event:p02', 'event:p03', 'event:p04', 'event:p05', 'event:p06']
event = ['event:p0', 'event:p1', 'event:p2', 'event:p3', 'event:p4', 'event:p5', 'event:p6']
r = redis.Redis()

if __name__ == "__main__":
    while 1:
        #time.sleep(60)
        f = open('32451.txt', 'w')
        """for e in range(event_b.__len__()):
            l = r.llen(event_b[e])
            for i in range(l):
                p = r.blpop(event_b[e], 1)
                p = str(p[1], encoding="utf8")
                print(event_b[e],i,p)
                f.write(p)
                f.write('\n')
        f.close()"""
        GetD = DataTreating('event_t1.txt')
        warn = GetD.GetWarn().astype(float)
        if warn.all() == 0:
            print("告警数目为0")
            continue
        #print(warn)
        clustering = AgglomerativeClustering(n_clusters=6).fit(warn)
        labels_ = clustering.labels_
        i = 0
        point = []
        order = []
        sec1 = [1,1,1,1,1,1,1,1,1]
        while i < len(labels_)-1:
            if labels_[i] not in point:
                point.append(labels_[i])
                order.append(i)
            else:
                sec1[labels_[i]] += 1
            i += 1
        warn_list = GetD.returnwarn(order)
        #print(warn_list)
        with open('warn_1.txt', 'w') as file_handle:
            for line in warn_list:
                file_handle.write(line)
                data = json.loads(line)
                print(data['strategy'])
                data2 = data['strategy']
                e = data2['priority']
                print(event[e])
                r.rpush(event[e], line)
            file_handle.close()

