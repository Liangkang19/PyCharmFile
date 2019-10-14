# 使用seaborn绘图

import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

# 设置风格，尺度
sns.set_style('darkgrid')
sns.set_context('paper')


# sns.lineplot()           # 折线图
# sns.barplot()            # 条形图
# sns.countplot()          # 计数条形图
# sns.scatterplot()        # 散点图
# sns.stripplot()          # 分类散点图
# sns.swarmplot()          # 分簇散点图与stipplot()的区别就是点不重叠
# sns.boxplot()            # 箱型图
# sns.boxenplot()          # 增强箱型图，适合大数据集，显示更多分位数
# sns.violinplot()         # 小提琴图
# sns.pointplot()          # 点图纵轴是均值，置信区间用标准差表示
# sns.kdeplot(x,bw=2.0, shade=True) # 核密度估计图，bw为带宽
# sns.rugplot(x)           # 地毯图直接将数据标记在坐标轴上
# sns.regplot()            # 回归线图，散点图附加回归线
# sns.heatmap(annot=True)  # 热图，annot表示显示数值
# # 饼图
# # explode表示部分扇形突出，x,label,explode均为数组形式数据
# plt.pie(x, label, explode, shadow=True,pctdistance=0.6,labeldistance=1.1,startangle=90)
# # 极坐标图
# ax = plt.subplot(111,projection='polar')  # projection指投影到极坐标
# ax.plot(x, y)     # x为角度(弧度制),y为径长




