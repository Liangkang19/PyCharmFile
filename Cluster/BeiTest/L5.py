import pandas as pd
import numpy as np
from pandas import DataFrame

A = pd.read_excel('x4.xlsx', sheet_name="Sheet1", header=0)
B = A.columns.values.tolist()  # 读出表头
print(B)
n = 1
count = []
lenth1 = len(B)
for i in range(lenth1-1):
    if (B[i])[0:5] == (B[i+1])[0:5]:
        n = n + 1
    else:
        count.append(n)
        n = 1
count.append(n)
print(count)

C = np.array(A)
x = 0
y = 0
a1 = np.zeros(shape=(5, 1))
for j in count:
    x = y
    y = y + j
    a2 = (np.sum(C[0:6, x:y], axis=1)).reshape(-1, 1)
    c = np.hstack((a1, a2))
    a1 = c
d1 = DataFrame(a1)
print(d1)
d2 = d1.to_excel('d2.xlsx')





