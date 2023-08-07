from sklearn.cluster import AffinityPropagation
import numpy as np
from test import DataTreating

if __name__ == "__main__":
    GetD = DataTreating('cpuidel.txt')
    warn = GetD.GetWarn().astype(float)
    print(warn)
    clustering = AffinityPropagation(preference=0.0001).fit(warn)  # 训练模型
    print(clustering.labels_)