# coding=utf-8
# 单行业密度聚类算法
# 散点图

import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from sklearn.cluster import DBSCAN

A = pd.read_excel(r'D:\Program Files\JetBrains\PyCharmFile\K-means\d2.xlsx', sheet_name="Sheet1", header=0)
tabtop = A.columns.values.tolist()        # 读出表头
B = np.array(A)
C = B[0:17, 6:18]

model = DBSCAN(eps=1.5)                   # 密度聚类算法
model.fit(C)                              # 开始聚类
D = DataFrame(C)
t = pd.concat([D, Series(model.labels_, index=D.index)], axis=1)
t.columns = tabtop[6:18] + [u'聚类类别']
print(t)
name1 = '谱聚类类别结果' + '.xlsx'
file2 = t.to_excel(name1)
