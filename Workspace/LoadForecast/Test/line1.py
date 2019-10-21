# 获取行数和列数
# 获取分类区间

import pandas as pd

df = pd.DataFrame([[1, 'A', '3%'], [2, 'B', '5%']],
                  index=['row_0', 'row_1'],
                  columns=['col_0', 'col_1', 'col_2'])
print(df)

rows = df.shape[0]  # 获取行数
cols = df.shape[1]  # 获取列数
print(rows)
print(cols)

bin1 = [-9]
bin2 = list(range(15, 300, 15))
bin3 = list(range(300, 1301, 100))

bins = bin1 + bin2 + bin3
print(bin2)
print(bin3)
print(bins)
