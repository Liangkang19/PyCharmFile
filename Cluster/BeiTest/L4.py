import pandas as pd
import numpy as np
from pandas import DataFrame
A = pd.read_excel('x4.xlsx', sheet_name="Sheet1")
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
d1 = DataFrame(a1)
d2 = d1.to_excel('d2.xlsx')
