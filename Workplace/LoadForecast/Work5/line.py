# 获取行数和列数

import pandas as pd

df = pd.DataFrame([[1, 'A', '3%'], [2, 'B', '5%']],
                  index=['row_0', 'row_1'],
                  columns=['col_0', 'col_1', 'col_2'])
print(df)

rows = df.shape[0]   # 获取行数
cols = df.shape[1]   # 获取列数
print(rows)
print(cols)


