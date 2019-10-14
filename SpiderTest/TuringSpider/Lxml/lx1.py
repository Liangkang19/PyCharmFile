# XPath解析库的使用
from lxml import etree

html2 = etree.parse(source='LHT1.html', parser=etree.HTMLParser(encoding='utf-8'))  # 读取本地HTML文件
result2 = html2.xpath('//body//a')
result3 = html2.xpath('//p/a')
result4 = html2.xpath('//a[@href = "https://man.ilovefishc.com/css3/"]/../@class')
result5 = html2.xpath('//p[@class="bold"]')
result6 = html2.xpath('//p[@class="bold"]/a/text()')
result7 = html2.xpath('//p/a/@href')
result8 = html2.xpath('//p[contains(@class, "italic")]/a/text()')

print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)

# text1 = '''
#     <body>
#         <p> 课堂案例在线演示 <a href = "https://ilovefishc.com/html5/" target = "_blank"> 传送门 </a> </p>
#         <p> HTML5速查宝典 <a href = "https://man.ilovefishc.com/html5/" target = "_blank"> 传送门 </a> </p>
#         <p> CCS3速查宝典 <a href = "https://man.ilovefishc.com/css3/" target = "_blank"> 传送门 </a> </p>
#     </body>
# '''
# html1 = etree.HTML(text1)         # 初始化HTML类，XPath对象
# result1 = etree.tostring(html1)    # 输出修正后的HTML代码(bytes类型)
# text2 = result1.decode('utf-8')    # 转码
# print(text2)
