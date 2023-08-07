from sklearn.cluster import AgglomerativeClustering
import numpy as np
from test import DataTreating
import time
import os

if __name__ == "__main__":
    while 1:
        #time.sleep(60)
        GetD = DataTreating('event_t1.txt')
        warn = GetD.GetWarn().astype(float)
        if warn.all() == 0:
            print("告警数目为0")
            continue
        #print(warn)
        clustering = AgglomerativeClustering(n_clusters=6).fit(warn)  # 训练模型
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
        print(warn_list)
        with open('warn_2.txt', 'w') as file_handle:
            for line in warn_list:
                file_handle.write(line)
            file_handle.close()

