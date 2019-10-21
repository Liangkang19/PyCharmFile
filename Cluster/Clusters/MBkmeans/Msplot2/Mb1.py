# coding=utf-8
# 单行业小批量K均值聚类
# 输出聚类结果的.xlsx表格数据
# 散点图

import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from sklearn.cluster import MiniBatchKMeans
import matplotlib.pyplot as plt

A = pd.read_excel(r'D:\Program Files\JetBrains\PyCharmFile\Cluster\Data\d2.xlsx', sheet_name="Sheet1", header=0)
tabtop = A.columns.values.tolist()        # 读出表头
B = np.array(A)
C = B[0:17, 6:18]
linelabel = list(range(1, 13))


model = MiniBatchKMeans(n_clusters=4)        # 聚类函数参数设置
model.fit(C)                                 # 开始聚类
r2 = DataFrame(model.cluster_centers_)       # 找出聚类中心
num = Series(model.labels_)                  # 按顺序列出类别标签

r1 = num.value_counts()                      # 按顺序统计出各个类别的数目
r = pd.concat([r2, r1], axis=1)              # 横向连接数据
r.columns = tabtop[6:18] + [u'类别数目']     # 修改表头
print(r)
file1 = r.to_excel('f1.xlsx')
D = DataFrame(C)
t = pd.concat([D, Series(model.labels_, index=D.index)], axis=1)
t.columns = tabtop[6:18] + [u'聚类类别']
print(t)
file2 = t.to_excel('f2.xlsx')

label1 = model.labels_
R = DataFrame(model.cluster_centers_)        # 找出聚类中心
D = DataFrame(C)
len4 = D.shape[0]

m1 = np.median(R, axis=0)                  # 求出每列的中位数
Rm1 = np.vstack((R, m1))                   # 将中位数的列合并
len1 = Rm1.shape[0]                        # 求出行的数目
m2 = np.median(D, axis=0)                  # 求出每列的中位数
Dm2 = np.vstack((D, m2))                   # 将中位数的列合并
len2 = Dm2.shape[0]                        # 求出行的数目
Dm21 = np.vstack((Dm2, m1))                # 将原始数据和两组中位数合并
len3 = Dm21.shape[0]                       # 求出行的数目

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
plt.title('不同月份用电量聚类中心图')
plt.ylabel('聚类中心')
plt.xlabel('月份')
name1 = '企业聚类1'
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
plt.title('不同月份用电量图')
plt.ylabel('用电量/千瓦时')
plt.xlabel('月份')
name2 = '行业聚类2'
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
plt.title('不同月份用电量图')
plt.ylabel('用电量/千瓦时')
plt.xlabel('月份')
name3 = '行业聚类3'
plt.savefig(name3)

plt.figure()
countA = 0
countB = 0
countC = 0
countD = 0

for i in range(len4):
    if label1[i] == 0:
        countA = countA + 1
        if countA == 1:
            plt.scatter(linelabel, C[i], color='r', linewidth=1.0, label='类别1')
        else:
            plt.scatter(linelabel, C[i], color='r', linewidth=1.0)
    if label1[i] == 1:
        countB = countB + 1
        if countB == 1:
            plt.scatter(linelabel, C[i], color='b', linewidth=1.0, label='类别2')
        else:
            plt.scatter(linelabel, C[i], color='b', linewidth=1.0)
    if label1[i] == 2:
        countC = countC + 1
        if countC == 1:
            plt.scatter(linelabel, C[i], color='y', linewidth=1.0, label='类别3')
        else:
            plt.scatter(linelabel, C[i], color='y', linewidth=1.0)
    if label1[i] == 3:
        countD = countD + 1
        if countD == 1:
            plt.scatter(linelabel, C[i], color='g', linewidth=1.0, label='类别4')
        else:
            plt.scatter(linelabel, C[i], color='g', linewidth=1.0)

plt.legend(loc='best')
plt.show()