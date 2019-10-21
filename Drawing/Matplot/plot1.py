# 绘制用电量数据属于哪一类的散点图

import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

P1 = pd.read_excel('f2.xlsx', sheet_name="Sheet1", header=0)
tabtop = P1.columns.values.tolist()        # 读出表头
P2 = np.array(P1)                          # 读出了索引和最后一列的聚类号
P3 = P2[0:12, 1:13]                        # 读出相应数据(不包含最后一列)
P4 = P2[0:12, 13:14]                       # 读出聚类类别所在列
P5 = P4.reshape(-1)                        # 转置
P6 = list(set(P5))                         # 删除矩阵中重复值
len1 = len(P6)                             # 类别数的长度
len2 = (DataFrame(P3)).shape[0]            # 返回数据框中的行数
linelabel = list(range(1, 13))

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示正常中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
color1 = ['red', 'blue', 'green',  'gray', 'pink', 'black', 'brown', 'orange', 'yellow', 'purple']
temp = ['2016年', '2017年', '2018年']
plt.figure()
for i in range(len1):
    count = 0
    for j in range(len2):
        if (P5[j] == P6[i]) and (count == 0):
            plt.scatter(linelabel, P3[j], color=color1[i], linewidth=1.0, label='类别' + str(i+1))
            count = count + 1
        if (P5[j] == P6[i]) and (count > 0):
            plt.scatter(linelabel, P3[j], color=color1[i], linewidth=1.0)

plt.legend(loc='best')
title4 = temp[0] + '企业月用电量聚类图2'
plt.title(title4)
plt.ylabel('用电量/千瓦时')
plt.xlabel('月份')
name4 = temp[0] + '行业' + '企业聚类4'
plt.savefig(name4)
plt.show()
