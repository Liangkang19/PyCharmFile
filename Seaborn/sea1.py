# 使用seaborn绘图

import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

P1 = pd.read_excel(r'D:\Program Files\JetBrains\PyCharmFile\Seaborn\g1.xlsx', sheet_name="Sheet1", header=0)
tabtop = P1.columns.values.tolist()        # 读出表头,返回矩阵
linelabel = DataFrame(range(1, 13))        # 使用DataFrame,返回列数据
P2 = P1.iloc[0:4, 1:13]                    # 读出数据，包含表头
P2.columns = list(range(0, 12))            # 更换表头
P3 = P2.T
print(P3)

plt.rcParams['font.sans-serif'] = ['SimHei']    # 显示正常中文标签
plt.rcParams['axes.unicode_minus'] = False      # 用来正常显示负号
color1 = ['red', 'blue', 'orange', 'green', 'black', 'gray', 'pink', 'brown',  'yellow', 'purple']

# for i6 in range(len1):
#     (P2.iloc[i6]).plot(color=color1[i6], label='类别'+str(i6+1), kind='bar')
# plt.legend()
# plt.show()

sns.stripplot(data=P3)                       # 直接调用plot()函数，会生成以索引为横坐标，
plt.show()                                   # 数值为纵坐标，表头为标注的按列绘制的折线图

