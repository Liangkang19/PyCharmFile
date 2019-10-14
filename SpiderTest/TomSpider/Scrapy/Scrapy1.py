# Scrapy框架
# http://python123.io/ws
# win10中切换磁盘路径的命令
# C:\Users\57307>    d:
# win10中在D盘/C盘中进入子文件夹的命令
# D:\>  cd ScrapyTest

# Scrapy框架建立步骤
# 1.建立一个scrapy工程：
#   d:\ScrapyTest>   scrapy startproject spider123  (spider123是工程名，任取)
#   d:\ScrapyTest>   cd spider123                   (切换到spider123工程目录下操作)
# 2.在工程中建立一个scrapy爬虫：
#   d:\ScrapyTest\spider123>   scrapy genspider dome python123.io
#   (-> dome是.py文件的名称，任取。-> dome后为爬取的初始网站。)
# 3.配置产生的spider爬虫
#   使用Pycharm等编写dome.py程序
# 4.运行爬虫，获取网页
#   d:\ScrapyTest\spider123>   scrapy crawl dome    (运行dome.py程序)
#   在spider123工程中出现xxx.html文件


