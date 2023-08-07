from sklearn.cluster import AgglomerativeClustering
import numpy as np
X = [[1,2],[3,2],[4,4],[1,2],[1,3]]#生成数据
clustering = AgglomerativeClustering().fit(X)#训练模型
print(clustering.labels_)