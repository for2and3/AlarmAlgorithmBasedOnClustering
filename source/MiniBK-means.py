from sklearn.cluster import MiniBatchKMeans
import numpy as np
from test import DataTreating

if __name__ == "__main__":
    GetD = DataTreating('cpuidel.txt')
    warn = GetD.GetWarn().astype(float)
    print(warn)
    clustering = MiniBatchKMeans(n_clusters=3).fit(warn)  # 训练模型
    print(clustering.labels_)