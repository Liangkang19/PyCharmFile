# 获取行数和列数

import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 'A', '3%'], [2, 'B', '5%']],
                  index=['row_0', 'row_1'],
                  columns=['col_0', 'col_1', 'col_2'])
print(df)

rows = df.shape[0]  # 获取行数
cols = df.shape[1]  # 获取列数
print(rows)
print(cols)

list1 = [15, 30, 45, 100, 115, 130, 145, 200, 215, 230, 245,
         300, 315, 330, 345, 400, 415, 430, 445, 500, 515, 530, 545,
         600, 615, 630, 645, 700, 715, 730, 745, 800, 815, 830, 845,
         900, 915, 930, 945, 1000, 1015, 1030, 1045, 1100, 1115, 1130, 1145,
         1200, 1215, 1230, 1245, 1300, 1315, 1330, 1345, 1400, 1415, 1430, 1445,
         1500, 1515, 1530, 1545, 1600, 1615, 1630, 1645, 1700, 1715, 1730, 1745,
         1800, 1815, 1830, 1845, 1900, 1915, 1930, 1945, 2000, 2015, 2030, 2045,
         2100, 2115, 2130, 2145, 2200, 2215, 2230, 2245, 2300, 2315, 2330, 2345, 2400]
list2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
shuzu1 = np.array(list1)
shuzu2 = np.array(list2)
shuzu = shuzu1 - shuzu2
list3 = list(shuzu)
print(list3)
