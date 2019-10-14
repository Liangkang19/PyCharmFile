# 写入和读取CSV文件
import pandas as pd
import csv
with open(file='csv1.csv', mode='w', encoding='utf-8', newline='') as cf:
    w = csv.writer(cf, delimiter=' ')          # 初始化写入对象cf
    w.writerow(['id', 'name', 'age'])          # 写入数据
    w.writerows([['10086', 'laosi', 38], ['10010', 'afeng', 28]])  # 注意writerow和writerows

with open(file='csv2.csv', mode='w', encoding='utf-8', newline='') as cf:
    file_name = ['id', 'name', 'age']
    w = csv.DictWriter(cf, fieldnames=file_name, delimiter=' ')  # 初始化写入字典对象
    w.writeheader()                                              # 写入字典头
    w.writerow({'id': '12580', 'name': '同城', 'age': '5'})       # 写入数据
    w.writerows([{'id': '12306', 'name': '火车票', 'age': '6'},
                 {'id': '95533', 'name': '银行', 'age': '12'}])

with open(file='csv2.csv', mode='r', encoding='utf-8') as cf:
    r = csv.reader(cf)                        # 初始化读出cf
    for row in r:
        print(row)

df = pd.read_csv('csv2.csv')                  # 使用pandas读取 .csv数据
print(df)
