# 对BN数据,按照结束时间(E)分类

import pandas as pd

list1 = [0, 15, 30, 45, 100, 115, 130, 145, 200, 215, 230, 245,
         300, 315, 330, 345, 400, 415, 430, 445, 500, 515, 530, 545,
         600, 615, 630, 645, 700, 715, 730, 745, 800, 815, 830, 845,
         900, 915, 930, 945, 1000, 1015, 1030, 1045, 1100, 1115, 1130, 1145,
         1200, 1215, 1230, 1245, 1300, 1315, 1330, 1345, 1400, 1415, 1430, 1445,
         1500, 1515, 1530, 1545, 1600, 1615, 1630, 1645, 1700, 1715, 1730, 1745,
         1800, 1815, 1830, 1845, 1900, 1915, 1930, 1945, 2000, 2015, 2030, 2045,
         2100, 2115, 2130, 2145, 2200, 2215, 2230, 2245, 2300, 2315, 2330, 2345]

list2 = [14, 29, 44, 59, 114, 129, 144, 159, 214, 229, 244, 259,
         314, 329, 344, 359, 414, 429, 444, 459, 514, 529, 544, 559,
         614, 629, 644, 659, 714, 729, 744, 759, 814, 829, 844, 859,
         914, 929, 944, 959, 1014, 1029, 1044, 1059, 1114, 1129, 1144, 1159,
         1214, 1229, 1244, 1259, 1314, 1329, 1344, 1359, 1414, 1429, 1444, 1459,
         1514, 1529, 1544, 1559, 1614, 1629, 1644, 1659, 1714, 1729, 1744, 1759,
         1814, 1829, 1844, 1859, 1914, 1929, 1944, 1959, 2014, 2029, 2044, 2059,
         2114, 2129, 2144, 2159, 2214, 2229, 2244, 2259, 2314, 2329, 2344, 2359]

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

dict1 = {}         # 创建空字典
key_list = []
value_list = []

for i in range(0, 26):
    name1 = list3[i] + '.xlsx'
    df = pd.read_excel(name1)
    df1 = df.sort_values(by='ENDTIME', ascending=True)   # 排序
    for j in range(0, 96):
        left = list1[j]
        right = list2[j]
        data1 = df1[df1.ENDTIME.between(left, right)]

        key_name = list3[i] + '-end' + str(list1[j])  # 获取文件名
        key_list.append(key_name)
        value_rows = data1.shape[0]  # 获取行数
        value_list.append(value_rows)
        dict1[key_name] = value_rows
        name2 = list3[i] + '-end' + str(list1[j]) + '.xlsx'
        print(name2)
        # data1.to_excel(name2, index=False)

key = pd.DataFrame(key_list)
value = pd.DataFrame(value_list)
result = pd.concat([key, value], axis=1)
result.to_excel('num4_2.xlsx', index=False)

