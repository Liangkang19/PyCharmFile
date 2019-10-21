# 读取合并数据测试代码

import pandas as pd
import numpy as np
from pandas import DataFrame

A = pd.read_excel('T1.xlsx', sheet_name="Sheet1", header=0)
B = A.columns.values.tolist()        # 读出表头
count = []
tabtop = [0]
lenth1 = len(B)
for i in range(lenth1-1):
    if (B[i])[0:7] == (B[i+1])[0:7]:
        tabtop.append((B[i])[0:7])
        continue
    else:
        count.append(i+1)
count.append(lenth1+1)
tabtop = sorted(set(tabtop), key=tabtop.index)     # 去掉列表中的重复值


C = np.array(A)
y = 0
a1 = np.zeros(shape=(1558, 1))     # 建立空矩阵
for j in count:
    x = y
    y = j
    a2 = (np.sum(C[0:1559, x:y], axis=1)).reshape(-1, 1)
    c = np.hstack((a1, a2))
    a1 = c

d1 = DataFrame(a1)
d1.columns = tabtop               # 更改数据表头
d2 = d1.to_excel('d2.xlsx')


