# requests模块应用测试1
# requests模块: 自动爬取HTML页面，自动网络请求提交
# Response应答对象：常用r表示
# Request需求对象：

# r.status_code        :状态码
# r.encoding           :http中的编码
# r.apparent_encoding  :内置备选编码格式
# r.content            :http响应内容的二进制形式
# r.text               :网页内容

import requests
r = requests.get('http://www.baidu.com')    # 使用get访问相关网页，r为Response对象
code1 = r.status_code                       # 状态码: status_code
print(code1)                                # code1为200：表示访问网页成功，404表示失败
r.encoding = 'utf-8'                        # 将网页编码格式改为：utf-8
# r.encoding = r.apparent_encoding          # 用备选编码替换原始编码后，能解析出部分内容
content1 = r.text                           # 转码后的网页内容：text
content2 = r.content                        # http响应内容的二进制形式：content
print(content1)

# requests库中 head(): 访问链接的头部信息
# requests库中 post():
# requests库中 put():

r = requests.head('http://httpbin.org/get')
print(r.headers)
print(r.text)
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/get', data=payload)
print(r.text)










