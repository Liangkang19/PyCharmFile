# 对AA数据，按照行车辆停留时间(AB)分类

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
bin1 = [-9]
bin2 = list(range(15, 300, 15))
bin3 = list(range(300, 1301, 100))

bins = bin1 + bin2 + bin3
key_list = []

for i in range(0, 65):
    name1 = list3[i] + '.xlsx'
    df = pd.read_excel(name1)
    df1 = df.sort_values(by='DWELTIME', ascending=True)  # 排序
    score_cut = pd.cut(df1['DWELTIME'], bins=bins, include_lowest=True, right=False)  # 通过pd.cut()函数把分数按照bins进行分割
    score_num = pd.value_counts(score_cut, sort=False)   # 查看每个区间的人数,不进行排序
    num = pd.DataFrame(score_num)
    name2 = list3[i] + '-de' + '.xlsx'
    name3 = list3[i] + '-dekey' + '.xlsx'
    num.to_excel(name2)
    for j in bins:
        if j != 1300:
            key_name = list3[i] + '-de' + str(j)
            key_list.append(key_name)
        else:
            break
    key = pd.DataFrame(key_list)
    key.to_excel(name3, index=False)
    key_list = []
    print(i+1)

dfc = pd.DataFrame()
dfz = pd.DataFrame()
for k in range(0, 65):
    name4 = list3[k] + '-de' + '.xlsx'
    dfa = pd.read_excel(name4)
    dfb = pd.concat([dfc, dfa], axis=0)
    dfc = dfb

    name5 = list3[k] + '-dekey' + '.xlsx'
    dfx = pd.read_excel(name5)
    dfy = pd.concat([dfz, dfx], axis=0)
    dfz = dfy

result = pd.concat([dfz, dfc], axis=1)
result.to_excel('num2_4.xlsx', index=False)