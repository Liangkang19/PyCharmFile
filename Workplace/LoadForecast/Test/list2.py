import pandas as pd
import numpy as np

df1 = pd.read_excel('trip1604HBO-mi.xlsx')
df2 = pd.read_excel('trip1604HBSHOP-mi.xlsx')
df3 = pd.concat([df1, df2], axis=0)

df_empty = pd.DataFrame()
df4 = pd.concat([df_empty, df3], axis=0)
print(df4)





