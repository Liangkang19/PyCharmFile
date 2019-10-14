# coding=utf-8
# 单行业漂移均值聚类三年/清除全零行
# 散点图

import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth

A = pd.read_excel(r'D:\Program Files\JetBrains\PyCharmFile\K-means\e2.xlsx', sheet_name="Sheet1", header=0)
tabtop = A.columns.values.tolist()        # 读出表头
B = np.array(A)
temp = ['2016年', '2017年', '2018年']
linelabel = list(range(1, 13))

C = B[0:109, 1:13]
D = DataFrame(C)
E = D.loc[~(D == 0).all(axis=1), :]                  # 删除全为0的行
E2 = np.array(E)
bw = estimate_bandwidth(E, quantile=0.2)             # 设置带宽
model = MeanShift(bandwidth=bw, bin_seeding=True)    # 聚类函数参数设置
model.fit(E)                                         # 开始聚类
r1 = (Series(model.labels_)).value_counts()          # 统计各个类别的数目
r2 = DataFrame(model.cluster_centers_)               # 找出聚类中心
r = pd.concat([r2, r1], axis=1)                      # 横向连接数据
r.columns = tabtop[1:13] + [u'类别数目']
nameA = temp[0] + '.xlsx'
print(nameA)
fileA = r.to_excel(nameA)
g = pd.concat([E, Series(model.labels_, index=E.index)], axis=1)
g.columns = tabtop[1:13] + [u'聚类类别']
nameB = 'A' + temp[0] + '.xlsx'
print(nameB)
file2 = g.to_excel(nameB)

label1 = model.labels_
R = DataFrame(model.cluster_centers_)        # 找出聚类中心
len4 = E.shape[0]

m1 = np.median(R, axis=0)                 # 求出每列的中位数
Rm1 = np.vstack((R, m1))                  # 将中位数的列合并
len1 = Rm1.shape[0]                       # 求出行的数目

m2 = np.median(E, axis=0)                  # 求出每列的中位数
Dm2 = np.vstack((E, m2))                   # 将中位数的列合并
len2 = Dm2.shape[0]                        # 求出行的数目
print(len2)

Dm21 = np.vstack((Dm2, m1))                # 将原始数据和两组中位数合并
len3 = Dm21.shape[0]                       # 求出行的数目
print(len3)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示正常中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
plt.figure()

for i in range(len1):
    if i == (len1 - 1):
        plt.plot(linelabel, Rm1[i], linestyle='--', marker='*', linewidth=1.0, label='聚类中位数')
    else:
        lengedname = '类别' + str(i+1)
        plt.plot(linelabel, Rm1[i], label=lengedname)

plt.legend(loc='best')
plt.title('2016年汽车企业月用电量聚类图1')
plt.ylabel('聚类中心')
plt.xlabel('月份')
name1 = '2016汽车聚类1'
plt.savefig(name1)

plt.figure()
for i in range(len2):
    if i == (len2 - 1):
        plt.plot(linelabel, Dm2[i], color='blue', linestyle='--', marker='^', linewidth=0.5, label='用电量中位数')
    elif i == (len2 - 2):
        lengedname = '各企业'
        plt.plot(linelabel, Dm2[i], color='darkgray', linewidth=1.0, label=lengedname)
    else:
        plt.plot(linelabel, Dm2[i], color='darkgray', linewidth=1.0)

plt.legend(loc='best')
plt.title('2016年汽车企业月用电量图1')
plt.ylabel('用电量/千瓦时')
plt.xlabel('月份')
name2 = '2016汽车聚类2'
plt.savefig(name2)

plt.figure()
for i in range(len3):
    if i == (len3 - 1):
        plt.plot(linelabel, Dm21[i], color='red', linestyle='--', marker='*', linewidth=0.5, label='聚类中位数')
    elif i == (len3 - 2):
        plt.plot(linelabel, Dm21[i], color='blue', linestyle='--', marker='^', linewidth=0.5, label='用电量中位数')
    elif i == (len3 - 3):
        lengedname = '各企业'
        plt.plot(linelabel, Dm21[i], color='darkgray', linewidth=1.0, label=lengedname)
    else:
        plt.plot(linelabel, Dm21[i], color='darkgray', linewidth=1.0)

plt.legend(loc='best')
plt.title('2016年汽车企业月用电量图2')
plt.ylabel('用电量/千瓦时')
plt.xlabel('月份')
name3 = '2016汽车聚类3'
plt.savefig(name3)

plt.figure()
countA = 0
countB = 0
countC = 0
countD = 0

for i4 in range(len4):
    if label1[i4] == 0:
        countA = countA + 1
        if countA == 1:
            plt.scatter(linelabel, E2[i4], color='r', linewidth=1.0, label='类别1')
        else:
            plt.scatter(linelabel, E2[i4], color='r', linewidth=1.0)
    if label1[i4] == 1:
        countB = countB + 1
        if countB == 1:
            plt.scatter(linelabel, E2[i4], color='b', linewidth=1.0, label='类别2')
        else:
            plt.scatter(linelabel, E2[i4], color='b', linewidth=1.0)
    if label1[i4] == 2:
        countC = countC + 1
        if countC == 1:
            plt.scatter(linelabel, E2[i4], color='y', linewidth=1.0, label='类别3')
        else:
            plt.scatter(linelabel, E2[i4], color='y', linewidth=1.0)
    if label1[i4] == 3:
        countD = countD + 1
        if countD == 1:
            plt.scatter(linelabel, E2[i4], color='g', linewidth=1.0, label='类别4')
        else:
            plt.scatter(linelabel, E2[i4], color='g', linewidth=1.0)
plt.legend(loc='best')
title4 = '2016年汽车企业月用电量聚类图2'
plt.title(title4)
plt.ylabel('用电量/千瓦时')
plt.xlabel('月份')
name4 = '2016汽车聚类4'
plt.savefig(name4)

plt.show()
