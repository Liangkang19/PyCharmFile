# coding=utf-8
# 对全行业原始数据的漂移均值聚类

import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from sklearn.cluster import MeanShift, estimate_bandwidth

A = pd.read_excel(r'D:\Program Files\JetBrains\PyCharmFile\K-means\d2.xlsx', sheet_name="Sheet1", header=0)
tabtop = A.columns.values.tolist()        # 读出表头
B = np.array(A)                           # 转化为矩阵
C = B[0:1543, 0:1]                        # 取出第一列数据
C = C.reshape(-1)                         # 转为行矩阵
C = C.astype(str)                         # 变换为字符串形式
lenth1 = len(C)
count = []
temp = []
print(C)


for k in range(lenth1-1):
    if (C[k])[0:2] == (C[k+1])[0:2]:
        temp.append((C[k])[0:2])
        continue
    else:
        count.append(k+1)
count.append(lenth1+1)
print(count)              # 取出第一列数据的聚类起始位置
temp = sorted(set(temp), key=temp.index)     # 去掉列表中的重复值
print(temp)


t = 0
b = 0
for i in count:
    a = b
    b = i
    x = 6
    y = 18
    for j in range(3):                    # 对某一行业的进行聚类(三次)
        D = B[a:b, x:y]
        bw = estimate_bandwidth(D, quantile=0.3)     # 设置带宽
        model = MeanShift(bandwidth=bw, bin_seeding=True)
        model.fit(D)                                 # 开始聚类
        r1 = (Series(model.labels_)).value_counts()  # 统计各个类别的数目
        r2 = DataFrame(model.cluster_centers_)       # 找出聚类中心
        r = pd.concat([r2, r1], axis=1)              # 横向连接数据
        r.columns = tabtop[x:y] + [u'类别数目']
        name1 = temp[t] + str(j) + '.xlsx'
        print(name1)
        file1 = r.to_excel(name1)
        D2 = DataFrame(D)
        g = pd.concat([D2, Series(model.labels_, index=D2.index)], axis=1)
        g.columns = tabtop[x:y] + [u'聚类类别']
        name2 = 'A' + temp[t] + str(j) + '.xlsx'
        print(name2)
        file2 = g.to_excel(name2)
        x = y
        y = y + 12
    t = t + 1
