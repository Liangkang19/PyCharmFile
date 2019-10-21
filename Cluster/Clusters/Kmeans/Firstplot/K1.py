# coding=utf-8
# 对某一行业的进行原始数据进行聚类

import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from sklearn.cluster import KMeans

A = pd.read_excel(r'D:\Program Files\JetBrains\PyCharmFile\Cluster\Data\d2.xlsx', sheet_name="Sheet1", header=0)
tabtop = A.columns.values.tolist()        # 读出表头
B = np.array(A)
C = B[0:17, 6:18]

model = KMeans(n_clusters=4)                 # 聚类函数参数设置
model.fit(C)                                 # 开始聚类
# lable1 = model.predict(C)                  # lable1和lable2都返回
# lable2 = model.labels_                     # 聚类类别的标签：[0, 0 ,2 ,1 ....]
# 聚类中心均值向量的总和

r2 = DataFrame(model.cluster_centers_)       # 找出聚类中心
num = Series(model.labels_)                  # 按顺序列出类别标签

r1 = num.value_counts()                      # 按顺序统计出各个类别的数目
r = pd.concat([r2, r1], axis=1)              # 横向连接数据
r.columns = tabtop[6:18] + [u'类别数目']     # 修改表头
print(r)

D = DataFrame(C)
t = pd.concat([D, Series(model.labels_, index=D.index)], axis=1)
t.columns = tabtop[6:18] + [u'聚类类别']
print(t)





