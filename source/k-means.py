from sklearn.cluster import KMeans
import numpy as np
from test import DataTreating

if __name__ == "__main__":
    GetD = DataTreating('event_t1.txt')
    warn = GetD.GetWarn().astype(float)
    #print(warn)
    clustering = KMeans(n_clusters=6).fit(warn)  # 训练模型
    labels_ = clustering.labels_
    i = 0
    point = []
    order = []
    time = [1,1,1,1,1,1,1,1,1]
    while i < len(labels_)-1:
        if labels_[i] not in point:
            point.append(labels_[i])
            order.append(i)
        else:
            time[labels_[i]] += 1
        i += 1
    # print(GetD.returnwarn(order))
    print(clustering.labels_)



