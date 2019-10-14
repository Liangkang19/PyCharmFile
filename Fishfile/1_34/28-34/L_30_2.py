# 编写一个程序，统计当前目录下不同类型文件的文件数目

def Count_files():
    import os
    list1 = os.listdir(os.curdir)  #使用curdir指定当前文件夹，使用listdir()列举出文件夹中的文件
    dict1 = dict()                 #创建一个空字典
    for each in list1:
        if os.path.isdir(each):                    #判断each是否是文件
            dict1.setdefault('文件夹',0)           #向字典中添加新元素
            dict1['文件夹'] = dict1['文件夹'] + 1  #该元素中的value加一
        else:
            (name,ext) = os.path.splitext(each)  #将each中的文件名和后缀名分开，放入name和ext中
            dict1.setdefault(ext,0)              #向字典中添加新元素
            dict1[ext] = dict1[ext] + 1          #该元素中的value加一
    for key1 in dict1.keys():        
        print('该文件夹下共有[%s]文件%d个' % (key1,dict1[key1]))  #将结果打印出来
Count_files()

# 运行结果：
# 该文件夹下共有[.py]文件3个
# 该文件夹下共有[.docx]文件1个
# 该文件夹下共有[文件夹]文件1个
# 该文件夹下共有[.txt]文件3个


    



    

