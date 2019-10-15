# 存储字典/列表测试
import pandas as pd

dict1 = {1: 'A', 2: 'B', 3: 'C'}         # 创建字典
list1 = [1, 2, 3, 6, 5, 9, 8]
df_list1 = pd.DataFrame(list1)
df_list1.to_excel('list1.xlsx', index=False)
print(df_list1)
