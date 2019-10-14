# coding=utf-8
# 对全行业的原始数据进行聚类
# 将聚类结果中位数等结果，进行可视化显示

import pandas as pd
import numpy as np
from pandas import DataFrame
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

A = pd.read_excel(r'D:\Program Files\JetBrains\PyCharmFile\K-means\d2.xlsx', sheet_name="Sheet1", header=0)
tabtop = A.columns.values.tolist()        # 读出表头
B = np.array(A)                           # 转化为矩阵
C = B[0:1543, 0:1]                        # 取出第一列数据
C = C.reshape(-1)                         # 转为行矩阵
C = C.astype(str)                         # 变换为字符串形式
lenth1 = len(C)
count = []
temp = []
linelabel = list(range(1, 13))
year1 = ['2016年', '2017年', '2018年']

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
    for j in year1:
        # 对某一行业的进行聚类(三次)
        D1 = B[a:b, x:y]
        model = KMeans(n_clusters=3)           # 聚类函数参数设置
        model.fit(D1)                          # 开始聚类
        R = DataFrame(model.cluster_centers_)  # 找出聚类中心
        D = DataFrame(D1)

        m1 = np.median(R, axis=0)    # 求出每列的中位数
        Rm1 = np.vstack((R, m1))     # 将中位数的列合并
        len1 = Rm1.shape[0]          # 求出行的数目
        print(len1)

        m2 = np.median(D, axis=0)   # 求出每列的中位数
        Dm2 = np.vstack((D, m2))    # 将中位数的列合并
        len2 = Dm2.shape[0]         # 求出行的数目
        print(len2)

        Dm21 = np.vstack((Dm2, m1))  # 将原始数据和两组中位数合并
        len3 = Dm21.shape[0]  # 求出行的数目

        print(len3)

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示正常中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        plt.figure()
        for i1 in range(len1):
            if i1 == (len1 - 1):
                plt.plot(linelabel, Rm1[i1], linestyle='--', marker='*', linewidth=1.0, label='聚类中位数')
            else:
                lengedname = '类别' + str(i1 + 1)
                plt.plot(linelabel, Rm1[i1], label=lengedname)

        plt.legend(loc='best')
        title1 = j + '企业月用电量聚类图'
        plt.title(title1)
        plt.ylabel('聚类中心值')
        plt.xlabel('月份')

        name1 = temp[t] + '行业' + j + '企业聚类1'
        plt.savefig(name1)
        plt.close()
        plt.figure()
        for i2 in range(len2):
            if i2 == (len2 - 1):
                plt.plot(linelabel, Dm2[i2], color='blue', linestyle='--', marker='^', linewidth=0.5, label='用电量中位数')
            elif i2 == (len2 - 2):
                lengedname = '各企业'
                plt.plot(linelabel, Dm2[i2], color='darkgray', linewidth=1.0, label=lengedname)
            else:
                plt.plot(linelabel, Dm2[i2], color='darkgray', linewidth=1.0)

        plt.legend(loc='best')
        title2 = j + '企业月用电量图1'
        plt.title(title2)
        plt.ylabel('用电量/千瓦时')
        plt.xlabel('月份')
        name2 = temp[t] + '行业' + j + '企业聚类2'
        plt.savefig(name2)
        plt.close()

        plt.figure()
        for i3 in range(len3):
            if i3 == (len3 - 1):
                plt.plot(linelabel, Dm21[i3], color='red', linestyle='--', marker='*', linewidth=0.5, label='聚类中位数')
            elif i3 == (len3 - 2):
                plt.plot(linelabel, Dm21[i3], color='blue', linestyle='--', marker='^', linewidth=0.5, label='用电量中位数')
            elif i3 == (len3 - 3):
                lengedname = '各企业'
                plt.plot(linelabel, Dm21[i3], color='darkgray', linewidth=1.0, label=lengedname)
            else:
                plt.plot(linelabel, Dm21[i3], color='darkgray', linewidth=1.0)

        plt.legend(loc='best')
        title3 = j + '企业月用电量图2'
        plt.title(title3)
        plt.ylabel('用电量/千瓦时')
        plt.xlabel('月份')
        name3 = temp[t] + '行业' + j + '企业聚类3'
        plt.savefig(name3)
        plt.close()
        x = y
        y = y + 12
    t = t + 1
