# coding=utf-8
# 对全行业数据进行清洗之后的聚类

import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from sklearn.cluster import KMeans

A = pd.read_excel(r'D:\Program Files\JetBrains\PyCharmFile\Cluster\Data\d2.xlsx', sheet_name="Sheet1", header=0)
# A 也是数据框形式(读入数据中包含索引和表头)
tabtop = A.columns.values.tolist()                 # 取出表头
B = np.array(A)                                    # 变成矩阵，只含有数据，无表头和索引

L1 = B[0:1543, 0:1]                                # 在矩阵中取第一列数据
L2 = L1.reshape(-1)                                # 转为行矩阵
L3 = L2.astype(str)                                # 变换为字符串形式
lenth1 = len(L3)
count = []
temp = []


def fenlei(lenth, l):
    for k in range(lenth-1):
        # 将不同行业的行号输出到count中
        if (l[k])[0:2] == (l[k+1])[0:2]:
            # 将行业号输出到temp中(包含重复数据)
            temp.append((l[k])[0:2])
            continue
        else:
            count.append(k+1)
    count.append(lenth+1)


fenlei(lenth1, L3)
temp = sorted(set(temp), key=temp.index)      # 将行业号数据去重


def guiyi(a, h):
    b = a.T                                               # 先对原始矩阵转置
    c = DataFrame(b)                                      # 将其变成序列
    d = (c-c.min(axis=0))/(c.max(axis=0)-c.min(axis=0))   # 归一化处理
    e = np.array(d)                                       # 将其变成归一化矩阵
    f = e.T                                               # 再转置回来
    g = np.hstack((h, f))                                 # 返回归一化后的矩阵加入索引的矩阵
    return g


def kmeans(p1):
    model = KMeans(n_clusters=5)                  # 聚类函数参数设置
    model.fit(p1)                                 # 开始聚类
    r1 = (Series(model.labels_)).value_counts()   # 统计各个类别的数目
    r2 = DataFrame(model.cluster_centers_)        # 找出聚类中心
    r = pd.concat([r2, r1], axis=1)               # 横向连接数据
    r.columns = tabtop[x:y] + [u'类别数目']       # 更换表头
    name1 = temp[t] + str(j) + '.xlsx'            # 输出为excel时的文件名
    print(name1)
    file1 = r.to_excel(name1)                     # 导出为excel文件
    p2 = DataFrame(p1)
    v = pd.concat([p2, Series(model.labels_, index=p2.index)], axis=1)
    v.columns = tabtop[x:y] + [u'聚类类别']
    name2 = 'A' + temp[t] + str(j) + '.xlsx'
    print(name2)
    file2 = v.to_excel(name2)


t = 0                   # 作为聚类结果的标题计数项使用
n = 0                   # m,n 为所取数据的行数，x，y为所取数据的列数
for i in count:
    m = n
    n = i
    x = 6
    y = 18
    for j in range(3):                   # 对某一行业的进行聚类(三次)
        P1 = B[m:n, x:y]  # 取某年某行业的数据
        L3 = B[m:n, 0:1]  # 取某行业的索引数据(132)
        P2 = guiyi(P1, L3)  # 数据归一化处理
        P3 = DataFrame(P2)  # 转换为数据框
        P4 = P3.dropna()  # 删除含有NaN数据的行,包含132
        P5 = P4.drop(0, axis=1)  # 去掉132所在列
        kmeans(P5)  # 进行kmeans聚类
        x = y

        y = y + 12
    t = t + 1












