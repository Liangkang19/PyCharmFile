# 按照行驶里程分类

import pandas as pd

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
bins = list(range(0, 7695, 5))
key_list = []

for i in range(0, 65):
    name1 = list3[i] + '.xlsx'
    df = pd.read_excel(name1)
    df1 = df.sort_values(by='TRPMILES', ascending=True)  # 排序
    score_cut = pd.cut(df1['TRPMILES'], bins=bins, include_lowest=True, right=False)  # 通过pd.cut()函数把分数按照bins进行分割
    score_num = pd.value_counts(score_cut, sort=False)  # 查看每个区间的人数,不进行排序
    num = pd.DataFrame(score_num)
    name2 = list3[i] + '-mi' + '.xlsx'
    print(num)
    for j in bins:
        key_name = list3[i] + '-mi' + str(j)
        key_list.append(key_name)
    key = pd.DataFrame(key_list)
    result = pd.concat([key, num], axis=1)
    result.to_excel(name2, index=False)


