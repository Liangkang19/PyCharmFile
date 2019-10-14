# 数据分箱

import numpy as np
import pandas as pd
from pandas import DataFrame

score_list = np.random.randint(0, 100, size=100)  # 随机创建100个学生分数，分数从0-100
bins = [0, 59, 79, 89, 100]                       # 分数分段区间即0,59]，（60,79]，（80，90]，（90,100]
score_cut = pd.cut(score_list, bins)              # 通过pd.cut()函数把分数按照bins进行分割
score_num = pd.value_counts(score_cut)            # 查看每个区间的人数
df = DataFrame()                                  # 创建一个空DataFrame数据
df['score_list'] = score_list                     # 把数据填充进去
df['Categories'] = pd.cut(df['score_list'], bins, labels=['D等', 'C等', 'B等', 'A等'])
print(df.head(10))
