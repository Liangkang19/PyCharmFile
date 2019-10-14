# 按照出行目的(AA)对不同年月(BR)的数据进行分组
import pandas as pd

date_name = ['trip1604', 'trip1605', 'trip1606', 'trip1607',
             'trip1608', 'trip1609', 'trip1610', 'trip1611',
             'trip1612', 'trip1701', 'trip1702', 'trip1703',
             'trip1704']
cut_name = ['HBO', 'HBSHOP', 'HBSOCREC', 'HBW', 'NHB']

for i in range(0, 13):
    trip_name = date_name[i] + '.xlsx'
    df = pd.read_excel(trip_name)                # 读取trip1604文件
    gb = df.groupby(df['TRIPPURP'])              # 对TRIPPURP进行分组
    for j in range(0, 5):
        df0 = gb.get_group(cut_name[j])          # 按照组名得到每组数据
        real_name = date_name[i] + cut_name[j] + '.xlsx'
        print(real_name)
        df0.to_excel(real_name, index=False)                  # 导出到文件

