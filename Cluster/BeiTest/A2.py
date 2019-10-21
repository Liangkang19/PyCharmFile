# coding=utf-8
# 计算不同聚类算法下的数据平均值

import pandas as pd
import numpy as np
from pandas import DataFrame

A = pd.read_excel('2017年行业产增表.xlsx', sheet_name="Sheet1", header=0)
B = np.array(A)             # 将产增数据转化为矩阵格式
C1 = B[0:, 1:]              # 取矩阵中相应的数据
C2 = C1.T                   # 转置

ax = pd.read_excel('A2.xlsx', sheet_name="Sheet2", header=0)
a1 = ax.fillna(0)           # 将数据中为NaN的值转换为0
b1 = np.array(a1)           # 将聚类结果数据转化为矩阵格式

bx = b1[0:, 0:1]            # 取出聚类方法名称对应的列
b2 = bx.reshape(-1)         # 转置为行向量
by = b1[0:, 1:2]            # 取出日期对应的列
b3 = by.reshape(-1)         # 转置为行向量
len1 = len(b3)              # 读出b3的长度


c1 = b1[0:, 3:]             # 取出聚类结果行业数据
c2 = c1.astype(np.int)      # 将所有数据转化为int型

count = []
for t in range(len1-1):
    if b2[t] == b2[t+1]:
        continue
    else:
        count.append(t+1)
count.append(len1+1)
print(count)                                # 取出第一列数据的起始位置，便于切分数据

temp1 = []
temp2 = []
result1 = [0, 0, 0, 0]                      # 建立一个列表，用于合并数据

z = 0                                       # z 用于取产增数据
y = 0                                       # x,y用于取区域数据
date = 0                                    # date用于统计次数，区分不同日期数据
for i in count:
    x = y
    y = i
    d1 = c2[x:y, 0:]                        # 如取出2017年2月中Kmeans聚类中的5行数据
    len2 = len(d1)
    for j in range(len2):
        list1 = d1[j]                       # 取Kmeans聚类中的5行数据的第n行
        for k in list1:                     # 得到行业号
            if k != 0:
                temp1.append(C2[z][k-1])    # 将行业号对应的总产值数据加入temp1中
                temp2.append(C2[z+1][k-1])  # 将行业号对应的同比增长数据加入temp2中

        meanx = np.mean(temp1)              # 计算平均值
        meany = np.mean(temp2)
        mean1 = '%.2f' % meanx              # 保留小数点后两位
        mean2 = '%.2f' % meany
        # print('算法名称', '日期', mean1, mean2,  (j+1), len(temp1))
        result2 = [mean1, mean2,  (j+1), len(temp1)]   # 得到一行结果
        result3 = np.vstack((result1, result2))        # 将结果按行合并
        result1 = result3
        temp1 = []
        temp2 = []

    date = date + 1                                    # 当date=6时，换到下个月的产值和增长数据
    if date == 6:
        z = z + 2
        date = 0

# print(result1)
result4 = np.delete(result1, 0, axis=0)               # 删除第一行
result5 = np.hstack((bx, by, result4))                # 合并聚类名称和日期
r = DataFrame(result5)                                # 结果转为数据框形式
print(r)
file1 = r.to_excel('聚类平均值.xlsx')
