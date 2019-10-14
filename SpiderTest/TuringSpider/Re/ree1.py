# match匹配
import re

content1 = 'Hello everyone 1008611 为您服务￥'
content2 = '''Hello everyone 1008611
 为您服务￥'''
content3 = '(百度一下)http://www.baidu.com'
result1 = re.match(r'^Hello\s\w{8}\s\d{7}\s[\u4e00-\u9fa5]{4}￥$', content1, re.S)
result2 = re.match(r'^Hello\s(\w+)\s(\d+)\s([\u4e00-\u9fa5]+)￥$', content1, re.S)
result3 = re.match(r'^H.*?(\d+).*?￥$', content2, re.S)
result4 = re.match(r'\([\u4e00-\u9fa5]+\)[a-zA-z]+://[^\s]*', content3, re.S)
print(result4)
# print(result1)
# print(result2)
# print(result2.group())
# print(result2.group(1))
# print(result2.group(2))
# print(result2.group(3))
# print(result3)
# print(result3.group(1))
