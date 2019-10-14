# json数据类型的应用

import json
str1 = '''
[
    {"name": "老四",
    "gender": "male",
    "age": "38"},
    {"name": "ayi",
    "gender": "female",
    "age": "27"}
]
'''
# json数据必须用"双引号"来包围，不能用'单引号'
print(type(str1))
json1 = json.loads(str1)      # 使用loads()将str数据转换成json对象
print(type(json1))
print(json1[0].get('name'))   # 使用get()获取json对象中的数据

# 从文件中读入json类型数据
with open('json2.json', 'r') as f:
    str2 = f.read()
    json2 = json.loads(str2)
    print(json2)

# 将str数据转换为json数据写入文件中，dumps()
with open('json3.json', 'w') as f:
    f.write(json.dumps(str1, indent=2, ensure_ascii=False))  # 正常显示中文
