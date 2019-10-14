# 文件分割
def Save_files(Laosi,Afeng,Axiong,count):
    file_name_Laosi = 'Laosi'+str(count)+'.txt'  #定义相应的文件名
    file_name_Afeng = 'Afeng'+str(count)+'.txt'
    file_name_Axiong = 'Axiong'+str(count)+'.txt'
        
    Laosi_file = open(file_name_Laosi,'w')       #在指定文件夹创建该文件
    Afeng_file = open(file_name_Afeng,'w')
    Axiong_file = open(file_name_Axiong,'w')

    Laosi_file.writelines(Laosi)                 #将分割出来的字符串写入相应文件中
    Afeng_file.writelines(Afeng)
    Axiong_file.writelines(Axiong)

    Laosi_file.close()                           #关闭相应文件后，指定文件才被写入数据
    Afeng_file.close()
    Axiong_file.close()

def Split_files(file_name):
    f1 = open(file_name)
    Laosi = []
    Afeng = []
    Axiong = []
    count = 1

    for each_line in f1:
        if each_line[0:6] != '======':
            #文件分割操作
            (role,line_spoken) = each_line.split(':',1)  #'：'是分隔符号，1 表示分隔1次
                                                          #role存储的是分隔符左边的字符串，line_spken存储的是分隔符右边的字符串
            if role == '老四':
                Laosi.append(line_spoken)
            if role == '阿峰':
                Afeng.append(line_spoken)
            if role == '阿雄':
                Axiong.append(line_spoken)
        else:
            #文件分别保存操作
            Save_files(Laosi,Afeng,Axiong,count)
            Laosi = []                                   #重新定义空列表
            Afeng = []
            Axiong = []
            count = count + 1                            #分段计数器加一
    Save_files(Laosi,Afeng,Axiong,count)       
    f1.close()                                           #关闭原始文件夹

Split_files('SeaKing.txt')
# 当使用split()分割时，出现：ValueError:not enough values to unpack(expected 2,got 1)的错误
# 将txt文件中的“换行”去掉即可。即某行不能为“空”，特别注意最后几行是否具有“换行”










        
