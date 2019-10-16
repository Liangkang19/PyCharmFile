# 对BN数据，按照行车辆停留时间(AB)分类

import pandas as pd

list3 = ['trip1604NJ', 'trip1604NY',
         'trip1605NJ', 'trip1605NY',
         'trip1606NJ', 'trip1606NY',
         'trip1607NJ', 'trip1607NY',
         'trip1608NJ', 'trip1608NY',
         'trip1609NJ', 'trip1609NY',
         'trip1610NJ', 'trip1610NY',
         'trip1611NJ', 'trip1611NY',
         'trip1612NJ', 'trip1612NY',
         'trip1701NJ', 'trip1701NY',
         'trip1702NJ', 'trip1702NY',
         'trip1703NJ', 'trip1703NY',
         'trip1704NJ', 'trip1704NY']
bin1 = [-9]
bin2 = list(range(15, 300, 15))
bin3 = list(range(300, 1301, 100))

bins = bin1 + bin2 + bin3
key_list = []

for i in range(0, 26):
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
for k in range(0, 26):
    name4 = list3[k] + '-de' + '.xlsx'
    dfa = pd.read_excel(name4)
    dfb = pd.concat([dfc, dfa], axis=0)
    dfc = dfb

    name5 = list3[k] + '-dekey' + '.xlsx'
    dfx = pd.read_excel(name5)
    dfy = pd.concat([dfz, dfx], axis=0)
    dfz = dfy

result = pd.concat([dfz, dfc], axis=1)
result.to_excel('num4_4.xlsx', index=False)
