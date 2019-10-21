# coding=utf-8
# 对全行业的原始数据(清洗全零行),进行MiniBatchKMeans聚类
# 将聚类结果中位数等结果，进行可视化显示
# 1.条形图+折线图/(# 横向条形图) 2.(#折线图) 3.折线图 4.气泡图

import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from sklearn.cluster import MiniBatchKMeans
import matplotlib.pyplot as plt

A = pd.read_excel(r'D:\Program Files\JetBrains\PyCharmFile\Cluster\Data\d2.xlsx', sheet_name="Sheet1", header=0)
tabtop = A.columns.values.tolist()  # 读出表头
B = np.array(A)                     # 转化为矩阵
X1 = B[0:1543, 0:1]                 # 取出第一列数据
X2 = X1.reshape(-1)                 # 转为行矩阵
C = X2.astype(str)                  # 变换为字符串形式
lenth1 = len(C)
print(C)

linelabel = list(range(1, 13))           # 生成月份数据列表，作为x轴数据
year1 = ['2016年', '2017年', '2018年']   # 用于命名
dalei = ['1类', '2类', '3类', '4类']

count = []
temp = []
for k in range(lenth1 - 1):
    if (C[k])[0:1] == (C[k + 1])[0:1]:
        temp.append((C[k])[0:1])
        continue
    else:
        count.append(k + 1)
count.append(lenth1 + 1)
print(count)                                # 取出第一列数据的聚类起始位置/用于数据分割
temp = sorted(set(temp), key=temp.index)    # 去掉列表中的重复值/用于命名
print(temp)

t = 0
b = 0
for i in count:
    a = b
    b = i
    x = 6
    y = 18
    for j in year1:
        # 对某一行业的进行聚类(三次)
        E1 = B[a:b, x:y]                        # 取出数据块
        E2 = DataFrame(E1)                      # 转化成数据块类型
        E3 = E2.loc[~(E2 == 0).all(axis=1), :]  # 清洗所取数据块中的全零行
        model = MiniBatchKMeans(n_clusters=4)   # 聚类函数参数设置
        model.fit(E3)                           # 开始聚类

        R = DataFrame(model.cluster_centers_)   # 找出聚类中心
        E4 = np.array(E3)                       # 矩阵类型
        D = DataFrame(E3)                       # 数据框类型

        # r1 = (Series(model.labels_)).value_counts()  # 统计各个类别的数目
        # r2 = DataFrame(model.cluster_centers_)       # 找出聚类中心
        # r = pd.concat([r2, r1], axis=1)              # 横向连接数据
        # r.columns = tabtop[x:y] + [u'类别数目']
        # nameA = temp[t] + '行业' + str(j) + '企业聚类中心1' + '.xlsx'
        # fileA = r.to_excel(nameA)
        #
        # g = pd.concat([D, Series(model.labels_, index=D.index)], axis=1)
        # g.columns = tabtop[x:y] + [u'聚类类别']
        # nameB = temp[t] + '行业' + str(j) + '企业聚类类别2' + '.xlsx'
        # print(nameB)
        # fileB = g.to_excel(nameB)

        m1 = np.median(R, axis=0)               # 求出聚类中心每列的中位数
        Rm1 = np.vstack((R, m1))                # 将中位数的列合并
        len1 = Rm1.shape[0]                     # 求合并后数据行的数目

        m2 = np.median(D, axis=0)               # 求出原始数据每列的中位数
        Dm2 = np.vstack((D, m2))                # 将中位数的列合并
        len2 = Dm2.shape[0]                     # 求合并后数据行的数目

        Dm21 = np.vstack((Dm2, m1))             # 将原始数据和两组中位数合并
        len3 = Dm21.shape[0]                    # 求出行的数目

        label1 = model.labels_                  # 找出聚类类别标志
        label2 = list(set(label1))              # 删除矩阵中重复值
        len4 = D.shape[0]                       # 原始数据的行长度
        len5 = len(label2)                      # 类别数的长度

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示正常中文标签
        plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
        color1 = ['red', 'blue', 'orange', 'green', 'black', 'gray', 'pink', 'brown', 'yellow', 'purple']

        # 画条形图和折线图，对Rm1中数据绘制
        plt.figure(figsize=(10, 6))
        ind = np.arange(len(linelabel))          # 条形图中x轴的位置量
        width = 0.2                              # 条形图的宽度
        dis = [-0.3, -0.1, 0.1, 0.3]             # 条形图中x轴的位置偏移量
        for i1 in range(len1):
            if i1 == (len1 - 1):
                plt.plot(ind, Rm1[i1], color=color1[i1], label='聚类中位数', linestyle='--', marker='^')
            else:
                plt.bar(ind + dis[i1], Rm1[i1], width, color=color1[i1], label='类别' + str(i1 + 1))

        plt.legend(loc='best')
        plt.xticks(ind, ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))  # x轴的刻度
        title1 = j + dalei[t] + '企业月用电量聚类中心图'
        plt.title(title1)
        plt.ylabel('聚类中心值')
        plt.xlabel('月份')
        name1 = temp[t] + '行业' + j + '企业聚类1'
        plt.savefig(name1)
        plt.close()

        for i8 in range(len1):
            if i8 == (len1 - 1):
                plt.plot(linelabel, Rm1[i8], linestyle='--', marker='*', linewidth=1.0, label='聚类中位数')
            else:
                lengedname = '类别' + str(i8 + 1)
                plt.plot(linelabel, Rm1[i8], label=lengedname)

        # # 画横向条形图，对Rm1数据绘制
        # plt.figure(figsize=(10, 6))
        # ind2 = np.arange(len(linelabel))
        # width2 = 0.2
        # dis2 = [-0.3, -0.15, 0, 0.15, 0.3]
        # for i12 in range(len1):
        #     if i12 == (len1 - 1):
        #         plt.barh(ind2 + dis[i12], Rm1[i12], width2, color=color1[i12], label='聚类中位数')
        #     else:
        #         plt.barh(ind2 + dis[i12], Rm1[i12], width2, color=color1[i12], label='类别' + str(i12 + 1))
        #
        # plt.legend(loc='best')
        # plt.yticks(ind2, ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))  # x轴的刻度
        # title12 = j + '企业月用电量聚类中心图'
        # plt.title(title12)
        # plt.xlabel('聚类中心值')
        # plt.ylabel('月份')
        #
        # name12 = temp[t] + '行业' + j + '企业聚类/横1'
        # plt.savefig(name12)
        # plt.close()

        # # 画折线图，对Dm2中数据绘制
        # plt.figure()
        # for i2 in range(len2):
        #     if i2 == (len2 - 1):
        #         plt.plot(linelabel, Dm2[i2], color='blue', linestyle='--', marker='^', linewidth=0.5, label='用电量中位数')
        #     elif i2 == (len2 - 2):
        #         lengedname = '各企业'
        #         plt.plot(linelabel, Dm2[i2], color='darkgray', linewidth=1.0, label=lengedname)
        #     else:
        #         plt.plot(linelabel, Dm2[i2], color='darkgray', linewidth=1.0)
        #
        # plt.legend(loc='best')
        # title2 = j + '企业月用电量图1'
        # plt.title(title2)
        # plt.ylabel('月用电量/kW·h')
        # plt.xlabel('月份')
        # name2 = temp[t] + '行业' + j + '企业聚类2'
        # plt.savefig(name2)
        # plt.close()

        # 画折线图，对Dm21中数据绘制
        plt.figure()
        for i3 in range(len3):
            if i3 == (len3 - 1):
                plt.plot(linelabel, Dm21[i3], color='red', linestyle='--', marker='*', linewidth=0.5, label='聚类中心中位数')
            elif i3 == (len3 - 2):
                plt.plot(linelabel, Dm21[i3], color='blue', linestyle='--', marker='^', linewidth=0.5, label='用电量中位数')
            elif i3 == (len3 - 3):
                lengedname = '各企业'
                plt.plot(linelabel, Dm21[i3], color='darkgray', linewidth=1.0, label=lengedname)
            else:
                plt.plot(linelabel, Dm21[i3], color='darkgray', linewidth=1.0)

        plt.legend(loc='best')
        title3 = j + dalei[t] + '企业月用电量图'
        plt.title(title3)
        plt.ylabel('月用电量/kW·h')
        plt.xlabel('月份')
        name3 = temp[t] + '行业' + j + '企业聚类3'
        plt.savefig(name3)
        plt.close()

        # 画气泡图，对E4中数据绘制
        plt.figure()
        for i4 in range(len5):
            count = 0
            for j2 in range(len4):
                if (label1[j2] == label2[i4]) and (count == 0):
                    lname = '类别' + str(i4 + 1)
                    plt.scatter(linelabel, E4[j2], s=E4[j2] / 400000 + 10, label=lname, color=color1[i4], linewidth=1.0,
                                alpha=0.4)
                    count = count + 1
                if (label1[j2] == label2[i4]) and (count > 0):
                    plt.scatter(linelabel, E4[j2], s=E4[j2] / 400000 + 10, color=color1[i4], linewidth=1.0, alpha=0.4)

        plt.legend(loc='best', markerscale=0.7, labelspacing=1)
        # markerscale=0.7    图例标记与原始标记的相对大小
        # labelspacing=1     图例条目之间的垂直间距
        # scatterpoints=1    为散点图图例条目创建的标记点数
        title4 = j + dalei[t] + '企业月用电量聚类类别图'
        plt.title(title4)
        plt.ylabel('用电量/kW·h')
        plt.xlabel('月份')
        plt.grid(True)
        name4 = temp[t] + '行业' + j + '企业聚类4'
        print(name4)
        plt.savefig(name4)
        plt.close()
        x = y
        y = y + 12
    t = t + 1
