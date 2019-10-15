# 基于行驶日期BH，将trip1604等每月数据进行分类
# 分成周一，周二....周日
import pandas as pd

date_name = ['trip1604', 'trip1605', 'trip1606', 'trip1607',
             'trip1608', 'trip1609', 'trip1610', 'trip1611',
             'trip1612', 'trip1701', 'trip1702', 'trip1703',
             'trip1704']
cut_name = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7']
dict1 = {}         # 创建空字典

for i in range(0, 13):
    trip_name = date_name[i] + '.xlsx'
    df = pd.read_excel(trip_name)                # 读取trip1604文件
    gb = df.groupby(df['TRAVDAY'])               # 对TRAVDAY进行分组
    for j in range(0, 7):
        df1 = gb.get_group(cut_name[j])          # 按照组名得到每组数据
        value_rows = df1.shape[0]  # 获取行数
        key_name = date_name[i] + cut_name[j]
        dict1[key_name] = value_rows
        real_name = date_name[i] + cut_name[j] + '.xlsx'
        print(real_name)
        df1.to_excel(real_name, index=False)                  # 导出到文件
print(dict1)

