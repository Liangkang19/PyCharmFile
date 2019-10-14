# 编写一个程序，用户输入文件名和开始搜索的路径，
# 搜索该文件是否存在。若遇到文件夹，则进入文件夹中继续寻找。


import os
def Search_file(start,target):
    os.chidr(start)               #更改当前工作目录
    list1 = os.listdir(os.curdir)
    for each in list1:
        (name,ext) = os.path.splitext(each)
        if ext == target:
            print(os.getcwd() + os.sep + each)  # os.sep:添加分隔符\\
        if os.path.isdir(each):       #判断是否是文件夹
            Search_file(each,target)  #递归调用
            os.chdir(os.pardir)       #递归结束后返回上一级目录

start = input('请输入待查找的初始目录：')
target = input('请输入需要查找的目标文件：')
Search_file(start,target)



            
