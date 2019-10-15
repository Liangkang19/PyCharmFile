# 按照月份数据(BR),将20month分类
# 分成201604，201605，...,201704等13类
import pandas as pd

date_name = [201604, 201605, 201606, 201607,
             201608, 201609, 201610, 201611,
             201612, 201701, 201702, 201703,
             201704]
dict1 = {}         # 创建空字典

df = pd.read_excel('tripmonths.xlsx')        # 读取tripmonths文件
gb = df.groupby(df['TDAYDATE'])               # 对TDAYDATE进行分组
for i in range(0, 13):
    df1 = gb.get_group(date_name[i])         # 按照组名得到每组数据
    value_rows = df1.shape[0]                # 获取行数
    key_name = 'trip' + str(date_name[i])
    dict1[key_name] = value_rows
    real_name = 'trip' + str(date_name[i]) + '.xlsx'
    print(real_name)
    df1.to_excel(real_name, index=False)                  # 导出到文件

print(dict1)

