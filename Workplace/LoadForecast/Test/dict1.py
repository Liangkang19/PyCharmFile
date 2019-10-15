# 存储字典/列表测试
import pandas as pd
import numpy as np

dict1 = {1: 'A', 2: 'B', 3: 'C'}         # 创建字典
list1 = [1, 2, 3, 6, 5, 9, 8]
list2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
list3 = np.vstack((list1, list2))    # 将中位数的列合并
df_list1 = pd.DataFrame(list1)
df_list2 = pd.DataFrame(list2)

df_list3 = np.hstack((df_list1, df_list2))

print(df_list3)
