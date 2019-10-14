# 使用for循环对Array数据进行的行列进行求和

import pandas as pd
import numpy as np
A = pd.read_excel(r'D:\Program Files\JetBrains\PyCharmFile\Work1\x4.xlsx', sheet_name="Sheet1")
B = np.array(A)
x = 1
y = 4
a1 = (np.sum(B[0:6, x:y], axis=1)).reshape(-1, 1)
for i in range(2):
    x = x + 3
    y = y + 3
    a2 = (np.sum(B[0:6, x:y], axis=1)).reshape(-1, 1)
    c = np.hstack((a1, a2))
    a1 = c
print(a1)
