# 对array类型数据进行读写等操作

import numpy as np
import pandas as pd

array1 = np.array([[1, 2, 3], [4, 5, 6]])
print(array1)
print('数组维度：', array1.ndim)
print('数组的行和列：', array1.shape)
print('元素数：', array1.size)

a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])
c = a + b
print(c)

A = pd.read_excel(r'D:\Program Files\JetBrains\PyCharmFile\Work1\x4.xlsx', sheet_name="Sheet1")
B = np.array(A)

a1 = (np.sum(B[0:6, 1:4], axis=1)).reshape(-1, 1)
a2 = (np.sum(B[0:6, 5:8], axis=1)).reshape(-1, 1)

c1 = np.hstack((a1, a2))
# c2 = np.vstack((a1, a2))
print(c1)



