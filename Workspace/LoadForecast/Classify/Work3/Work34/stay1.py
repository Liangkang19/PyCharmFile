# 对BH数据，按照行车辆停留时间(AB)分类

import pandas as pd

list3 = ['trip1604d1', 'trip1604d2', 'trip1604d3', 'trip1604d4', 'trip1604d5', 'trip1604d6', 'trip1604d7',
         'trip1605d1', 'trip1605d2', 'trip1605d3', 'trip1605d4', 'trip1605d5', 'trip1605d6', 'trip1605d7',
         'trip1606d1', 'trip1606d2', 'trip1606d3', 'trip1606d4', 'trip1606d5', 'trip1606d6', 'trip1606d7',
         'trip1607d1', 'trip1607d2', 'trip1607d3', 'trip1607d4', 'trip1607d5', 'trip1607d6', 'trip1607d7',
         'trip1608d1', 'trip1608d2', 'trip1608d3', 'trip1608d4', 'trip1608d5', 'trip1608d6', 'trip1608d7',
         'trip1609d1', 'trip1609d2', 'trip1609d3', 'trip1609d4', 'trip1609d5', 'trip1609d6', 'trip1609d7',
         'trip1610d1', 'trip1610d2', 'trip1610d3', 'trip1610d4', 'trip1610d5', 'trip1610d6', 'trip1610d7',
         'trip1611d1', 'trip1611d2', 'trip1611d3', 'trip1611d4', 'trip1611d5', 'trip1611d6', 'trip1611d7',
         'trip1612d1', 'trip1612d2', 'trip1612d3', 'trip1612d4', 'trip1612d5', 'trip1612d6', 'trip1612d7',
         'trip1701d1', 'trip1701d2', 'trip1701d3', 'trip1701d4', 'trip1701d5', 'trip1701d6', 'trip1701d7',
         'trip1702d1', 'trip1702d2', 'trip1702d3', 'trip1702d4', 'trip1702d5', 'trip1702d6', 'trip1702d7',
         'trip1703d1', 'trip1703d2', 'trip1703d3', 'trip1703d4', 'trip1703d5', 'trip1703d6', 'trip1703d7',
         'trip1704d1', 'trip1704d2', 'trip1704d3', 'trip1704d4', 'trip1704d5', 'trip1704d6', 'trip1704d7']
bin1 = [-9]
bin2 = list(range(15, 300, 15))
bin3 = list(range(300, 1301, 100))

bins = bin1 + bin2 + bin3
key_list = []

for i in range(0, 91):
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
for k in range(0, 91):
    name4 = list3[k] + '-de' + '.xlsx'
    dfa = pd.read_excel(name4)
    dfb = pd.concat([dfc, dfa], axis=0)
    dfc = dfb

    name5 = list3[k] + '-dekey' + '.xlsx'
    dfx = pd.read_excel(name5)
    dfy = pd.concat([dfz, dfx], axis=0)
    dfz = dfy

result = pd.concat([dfz, dfc], axis=1)
result.to_excel('num3_4.xlsx', index=False)
