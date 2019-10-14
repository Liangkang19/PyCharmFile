# DataFrame数据行列的读取

import pandas as pd
import numpy as np
from pandas import DataFrame

P1 = pd.read_excel(r'D:\Program Files\JetBrains\PyCharmFile\Matplot\f2.xlsx', sheet_name="Sheet1", header=0)
tabtop = P1.columns.values.tolist()        # 读出表头,返回矩阵
linelabel = DataFrame(range(1, 13))        # 使用DataFrame,返回列数据
P2 = P1.iloc[0:12, 1:13]                   # 读出数据，包含表头
P2.columns = list(range(0, 12))            # 更换表头

print(P2)
P3 = P2[1]                         # 根据表头名访问某一列,格式：P3[表头名称]/如P3[0]/P3['X2016']
P4 = P2[P2.columns[2]]             # 根据表头的索引访问某一列,返回-->列数据
P5 = P2[P2.columns[0:2]]           # 根据表头的索引访问某几列，返回->列数据

P6 = P2[0:1]                       # 根据索引范围访问某一/某几行,返回行数据
P7 = P2.iloc[0:1]                  # 根据索引范围访问某一/某几行,返回行数据
P8 = P2.iloc[0]                    # 根据索引范围访问某一行,返回---->列数据

P9 = P2.iloc[0:2, 0:3]             # 根据索引访问块数据
print(P5)



