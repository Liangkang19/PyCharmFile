# 编写一个程序，比较用户输入的两个文件，如果文件中对应行数的字符串不同，
# 显示出不同处的行号和第一个不同处字符的位置
def Compare_files(file1,file2):
    f1 = open(file1,'w')
    f2 = open(file2,'w')
    count = 0      # 统计行数
    differ = []    # 统计不一样的数目

    for line1 in f1:
        line2 = f2.readline()
        count = count + 1
        if line1 in f1:
            differ.append(count)

    f1.close()
    f2.close()
    return differ
file1 = input('请输入第一个文件名：')
file1 = input('请输入第二个文件名：')

differ = file_compare(file1,file2)

if len(differ) == 0:
    print('两个文件完全相同！')
else:
    print('两个文件共有[%d]处不同：' % len(differ))
    for each in differ:
        print('第%d行不一样'% each)

   






    
