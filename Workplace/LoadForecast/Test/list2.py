import pandas as pd
import numpy as np

bin1 = list(range(0, 7695, 5))
score_cut = pd.cut(score_list, bins)              # 通过pd.cut()函数把分数按照bins进行分割
score_num = pd.value_counts(score_cut)            # 查看每个区间的人数



