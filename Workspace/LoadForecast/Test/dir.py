import os
# 获得当前目录的路径
current_dir = os.path.abspath('.')                    # 获得dir.py-->Test(其路径)
# 获得当前目录的父目录的路径
father_dir = os.path.dirname(os.path.abspath('.'))    # 获得dir.py-->Test-->LoadForecast(其路径)
data_dir = father_dir + '/Data/'                      # 跳转到与Test同级的Data路径下
print(current_dir)
print(father_dir)
print(data_dir)
