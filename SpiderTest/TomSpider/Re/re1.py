# 正则表达式re的特性：
# 通用的字符串表达框架
# 简洁表达一组字符串的表达式
# 拥有“简洁”和“特征”思想的工具
# 判断字符串的特征归属
# re库的应用:search,match,findall,split,finditer,compile

import re
match1 = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match1:
    print(match1.group(0))

print(type(match1))
print(match1.string)
print(match1.re)
print(match1.pos)
print(match1.endpos)
print(match1.start())
print(match1.end())
print(match1.span())

match2 = re.match(r'[1-9]\d{5}', '100081 BIT')
if match2:
    print(match2.group(0))

list1 = re.findall(r'[1-9]\d{5}', 'XY100081BIT TUS100085')
print(list1)

list2 = re.split(r'[1-9]\d{5}', 'XY100081BIT TUS100085')
print(list2)

list3 = re.split(r'[1-9]\d{5}', 'XY100081BIT TUS100085', maxsplit=1)
print(list3)

for m in re.finditer(r'[1-9]\d{5}', 'XY100081BIT TUS100085'):
    if m:
        print(m.group(0))

string1 = re.sub(r'[1-9]\d{5}', 'abcdefg', 'XY100081BIT TUS100085')
print(string1)

regex = re.compile(r'[1-9]\d{5}')
print(regex.sub('abcdefg', 'XY100081BIT TUS100085'))

