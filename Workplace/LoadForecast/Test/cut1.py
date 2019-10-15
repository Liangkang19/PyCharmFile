# 数据分箱

import numpy as np
import pandas as pd
from pandas import DataFrame

score_list = np.random.randint(0, 100, size=100)  # 随机创建100个学生分数，分数从0-100
bins = [0, 59, 79, 89, 100]                       # 分数分段区间即0,59]，（60,79]，（80，90]，（90,100]
score_cut = pd.cut(score_list, bins=bins, include_lowest=True, right=False)              # 通过pd.cut()函数把分数按照bins进行分割
score_num = pd.value_counts(score_cut)            # 查看每个区间的人数
num = pd.DataFrame(score_num)
print(num)

