# 基于车辆地点BN，将trip1604等每月数据进行分类，
# 取NY和NJ等两类进行对比

import pandas as pd

date_name = ['trip1604', 'trip1605', 'trip1606', 'trip1607',
             'trip1608', 'trip1609', 'trip1610', 'trip1611',
             'trip1612', 'trip1701', 'trip1702', 'trip1703',
             'trip1704']
cut_name = [1, 2, 3, 4, 5, 6, 7]
connect_name = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7']

dict1 = {}         # 创建空字典
key_list = []
value_list = []

for i in range(0, 13):
    trip_name = date_name[i] + '.xlsx'
    df = pd.read_excel(trip_name)                # 读取trip1604文件
    gb = df.groupby(df['TRAVDAY'])               # 对TRAVDAY进行分组
    for j in range(0, 7):
        df1 = gb.get_group(cut_name[j])          # 按照组名得到每组数据

        key_name = date_name[i] + connect_name[j]     # 获取文件名
        key_list.append(key_name)
        value_rows = df1.shape[0]                     # 获取行数
        value_list.append(value_rows)
        dict1[key_name] = value_rows

        real_name = date_name[i] + connect_name[j] + '.xlsx'
        print(real_name)
        df1.to_excel(real_name, index=False)                  # 导出到文件

key = pd.DataFrame(key_list)
key.to_excel('key.xlsx', index=False)
value = pd.DataFrame(value_list)
value.to_excel('value.xlsx', index=False)

print(dict1)

