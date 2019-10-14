# 编写一个程序，计算当前文件夹下所有文件的大小

def Count_size():
    import os
    list1 = os.listdir(os.curdir)
    for each in list1:
        size = os.path.getsize(each)
        print('文件:%s 大小:[%d Bytes]'% (each,size))
Count_size()

# 结果：
# 文件:L_30_1.py 大小:[522 Bytes]
# 文件:SeaKing.txt 大小:[712 Bytes]
