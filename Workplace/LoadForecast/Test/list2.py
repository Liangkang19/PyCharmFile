import pandas as pd
import numpy as np

# df1 = pd.read_excel('trip1604HBO-mi.xlsx')
# df2 = pd.read_excel('trip1604HBSHOP-mi.xlsx')
# df3 = pd.concat([df1, df2], axis=0)
#
# df_empty = pd.DataFrame()
# df4 = pd.concat([df_empty, df3], axis=0)
# print(df4)

bin1 = [-9]
bin2 = list(range(15, 300, 15))
bin3 = list(range(300, 1301, 100))

bins = bin1 + bin2 + bin3
print(bin2)
print(bin3)
print(bins)


