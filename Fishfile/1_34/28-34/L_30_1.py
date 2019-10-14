#os模块相关操作过程

import os                   #先引入os模块
os.getcwd()                 #返回当前工作目录：'D:\\Program Files\\Python3.7'
os.chdir('D:\\Program Files\\Python3.7\\Pythonfiles') #修改当前工作目录
os.system('cmd')            #系统命令操作

os.path.basename('D:\\Program Files\\Python3.7\\Pythonfiles')#os的路径操作

import time                 #引入时间模块
time.gmtime(os.path.getatime('D:\\Program Files\\Python3.7\\Pythonfiles\\A\\text.txt'))

