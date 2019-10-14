# 按照出行时间分类

import pandas as pd

list1 = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]
list2 = [29, 44, 59, 74, 89, 104, 119, 134, 149, 164, 179, 1000]
list3 = ['trip1604HBO', 'trip1604HBSHOP', 'trip1604HBSOCREC', 'trip1604HBW', 'trip1604NHB',
         'trip1605HBO', 'trip1605HBSHOP', 'trip1605HBSOCREC', 'trip1605HBW', 'trip1605NHB',
         'trip1606HBO', 'trip1606HBSHOP', 'trip1606HBSOCREC', 'trip1606HBW', 'trip1606NHB',
         'trip1607HBO', 'trip1607HBSHOP', 'trip1607HBSOCREC', 'trip1607HBW', 'trip1607NHB',
         'trip1608HBO', 'trip1608HBSHOP', 'trip1608HBSOCREC', 'trip1608HBW', 'trip1608NHB',
         'trip1609HBO', 'trip1609HBSHOP', 'trip1609HBSOCREC', 'trip1609HBW', 'trip1609NHB',
         'trip1610HBO', 'trip1610HBSHOP', 'trip1610HBSOCREC', 'trip1610HBW', 'trip1610NHB',
         'trip1611HBO', 'trip1611HBSHOP', 'trip1611HBSOCREC', 'trip1611HBW', 'trip1611NHB',
         'trip1612HBO', 'trip1612HBSHOP', 'trip1612HBSOCREC', 'trip1612HBW', 'trip1612NHB',
         'trip1701HBO', 'trip1701HBSHOP', 'trip1701HBSOCREC', 'trip1701HBW', 'trip1701NHB',
         'trip1702HBO', 'trip1702HBSHOP', 'trip1702HBSOCREC', 'trip1702HBW', 'trip1702NHB',
         'trip1703HBO', 'trip1703HBSHOP', 'trip1703HBSOCREC', 'trip1703HBW', 'trip1703NHB',
         'trip1704HBO', 'trip1704HBSHOP', 'trip1704HBSOCREC', 'trip1704HBW', 'trip1704NHB']

for i in range(0, 65):
    name1 = list3[i] + '.xlsx'
    df = pd.read_excel(name1)
    df1 = df.sort_values(by='TRVLCMIN', ascending=True)   # 排序
    for j in range(0, 12):
        left = list1[j]
        right = list2[j]
        data1 = df1[df1.TRVLCMIN.between(left, right)]
        name2 = list3[i] + str(list1[j]) + '.xlsx'
        print(name2)
        data1.to_excel(name2, index=False)
