# 基于车辆地点BN，将trip1604等每月数据进行分类，
# 取NY和NJ等两类进行对比

# 基于出行目的(AA)，将trip1604等每月数据(BR)进行分类
# 分成HBO，HBSHOP等5类

import pandas as pd
import numpy as np

date_name = ['trip1604', 'trip1605', 'trip1606', 'trip1607',
             'trip1608', 'trip1609', 'trip1610', 'trip1611',
             'trip1612', 'trip1701', 'trip1702', 'trip1703',
             'trip1704']
# cut_name = ['AK', 'AL', 'AZ', 'CA', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID',
#           'IL', 'KY', 'MA', 'MD', 'MI', 'MN', 'MO', 'NC', 'NE', 'NH',
#           'NJ', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN',
#           'TX', 'UT', 'VA', 'WI', 'WV']

cut_name = ['NJ', 'NY']
dict1 = {}         # 创建空字典
key_list = []
value_list = []

for i in range(0, 13):
    trip_name = date_name[i] + '.xlsx'
    df = pd.read_excel(trip_name)                # 读取trip1604文件
    gb = df.groupby(df['HHSTATE'])               # 对HHSTATE进行分组
    for j in range(0, 2):
        df1 = gb.get_group(cut_name[j])          # 按照组名得到每组数据

        key_name = date_name[i] + cut_name[j]    # 获取文件名
        key_list.append(key_name)
        value_rows = df1.shape[0]                # 获取行数
        value_list.append(value_rows)
        dict1[key_name] = value_rows

        real_name = date_name[i] + cut_name[j] + '.xlsx'
        print(real_name)
        df1.to_excel(real_name, index=False)                  # 导出到文件

num_list = np.vstack((key_list, value_list))
num = pd.DataFrame(num_list)
num.to_excel('num.xlsx', index=False)
print(dict1)
