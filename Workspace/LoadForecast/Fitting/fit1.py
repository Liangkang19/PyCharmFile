# 数据拟合

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def Get_data_dir():
    """
    获取数据文件夹所在的路径
    :return: data_dir
    """
    current_dir = os.path.abspath('.')         # 获得当前目录的路径
    father_dir = os.path.dirname(current_dir)  # 获得当前目录的父目录的路径
    data_dir = father_dir + '/Data/'           # 获得Data文件的路径
    return data_dir


data_dir1 = Get_data_dir()
list1 = ['num']
dir1 = data_dir1 + list1[0] + '.xlsx'
df = pd.read_excel(dir1)

plt.rcParams['font.sans-serif'] = ['SimHei']   # 显示正常中文标签
plt.rcParams['axes.unicode_minus'] = False     # 用来正常显示负号

plt.figure()
xlabel = ['1604', '1605', '1606', '1607', '1608', '1609', '1610',
          '1611', '1612', '1701', '1702', '1703', '1704']
ylabel = df[df.columns[1]]
listx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = np.array(listx)
y = np.array(ylabel)
f1 = np.polyfit(x, y, 3)
p1 = np.poly1d(f1)
y1 = p1(x)           # 拟合y值

print('三次多项式拟合:\n', p1)

plt.bar(x, ylabel, label='各月份出行次数', color='grey')
plt.plot(x, y1, label='拟合曲线', color='black')
plt.legend(loc='best')
title1 = '2016-2017年各月份出行次数图'
plt.title(title1)
plt.xlabel('年月')
plt.ylabel('出行次数')
plt.show()


