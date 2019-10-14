# 对国家地理网站中图片进行爬取
# 为了跨平台使用方便：统一采用左斜杠'/'来进行文件分割
# 例如：C:/windows/system

import requests
import os           # 文件系统模块os

url = 'http://image.ngchina.com.cn/userpic/45580/2019/0608153932455806172.jpeg'
root = 'D:/BaiduDownload/pics'
path = root + '/' + url.split('/')[-1]       # 将url中最后一个'/'中的右边部分分割出来
try:
    if not os.path.exists(root):             # 判断根目录root是否存在
        os.mkdir(root)                       # 若不存在，则创建相关文件夹
    if not os.path.exists(path):             # 判断图片文件是否存在
        r = requests.get(url)                # 若不存在，则开始爬取
        r.raise_for_status()
        with open(path, 'wb') as f:          # 创建相关的path路径
            f.write(r.content)               # 将爬取的内容写入f文件中
            f.close()                        # 关闭f文件
            print('文件保存成功！')
    else:
        print('文件已经存在！')
except:
    print('爬取失败！')


# url = 'http://image.ngchina.com.cn/userpic/45580/2019/0608153932455806172.jpeg'
# path = 'D:/BaiduDownload/pics.jpeg'
# r = requests.get(url)
# print(r.status_code)
# with open(path, 'wb') as f:
#     f.write(r.content)
#
# f.close()



