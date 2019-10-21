# coding=utf-8
# 单行业漂移均值聚类三年mean shift 聚类


import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from sklearn.cluster import MeanShift, estimate_bandwidth

A = pd.read_excel(r'D:\Program Files\JetBrains\PyCharmFile\Cluster\Data\e2.xlsx', sheet_name="Sheet1", header=0)
tabtop = A.columns.values.tolist()        # 读出表头
B = np.array(A)
temp = ['2016年', '2017年', '2018年']

x = 1
y = 13
for j in range(3):                                       # 对某一行业的进行聚类(三次)
    C = B[0:109, x:y]
    D = DataFrame(C)
    E = D.loc[~(D == 0).all(axis=1), :]                  # 删除全为0的行
    bw = estimate_bandwidth(E, quantile=0.3)             # 设置带宽
    model = MeanShift(bandwidth=bw, bin_seeding=True)    # 聚类函数参数设置
    model.fit(E)                                         # 开始聚类
    r1 = (Series(model.labels_)).value_counts()          # 统计各个类别的数目
    r2 = DataFrame(model.cluster_centers_)               # 找出聚类中心
    r = pd.concat([r2, r1], axis=1)                      # 横向连接数据
    r.columns = tabtop[x:y] + [u'类别数目']
    name1 = temp[j] + '.xlsx'
    print(name1)
    file1 = r.to_excel(name1)
    g = pd.concat([E, Series(model.labels_, index=E.index)], axis=1)
    g.columns = tabtop[x:y] + [u'聚类类别']
    name2 = 'A' + temp[j] + '.xlsx'
    print(name2)
    file2 = g.to_excel(name2)
    x = y
    y = y + 12

