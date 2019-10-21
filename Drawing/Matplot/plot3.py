# 绘制聚类中心横向条形图

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

P1 = pd.read_excel('f1.xlsx', sheet_name="Sheet1", header=0)
tabtop = P1.columns.values.tolist()          # 读出表头
P2 = np.array(P1)                            # 读出了索引和最后一列的聚类号
P3 = P2[0:4, 1:13]                           # 读出相应数据(不包含最后一列)
P4 = P2[0:4, 0:1]                            # 读出索引所在列
P5 = P4.reshape(-1)                          # 转置

M2 = np.median(P3, axis=0)                   # 求出每列的中位数
M3 = np.vstack((P3, M2))                     # 将中位数的列合并
len1 = M3.shape[0]                           # 求出行的数目
print(M3)
print(len1)
linelabel = list(range(1, 13))

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示正常中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
color1 = ['red', 'blue', 'orange', 'green', 'black', 'gray', 'pink', 'brown',  'yellow', 'purple']
temp = ['2016年', '2017年', '2018年']
plt.figure()
ind = np.arange(len(linelabel))            # the x locations for the groups
print(ind)
width = 0.15                                # the width of the bars
dis = [-0.3, -0.15, 0, 0.15, 0.3]
for i in range(len1):
    if i == (len1-1):
        plt.barh(ind + dis[i], M3[i],  width, color=color1[i], label='聚类中位数')
    else:
        plt.barh(ind + dis[i], M3[i],  width, color=color1[i], label='类别' + str(i + 1))
plt.yticks(ind, ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))  # x轴的刻度
plt.legend(loc='best')
plt.title('企业聚类图4')
plt.xlabel('用电量/千瓦时')
plt.ylabel('月份')
plt.savefig('横向条形图2')
plt.show()

