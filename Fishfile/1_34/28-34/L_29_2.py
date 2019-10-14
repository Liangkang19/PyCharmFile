# 由用户输入文件名(.txt)和拥有换行的文件字符串，并以某新行的字符"##"结束
# 创建相应的同名文件，并保存字符串的内容。

def Write_files(name):
    name1 = name + '.txt'  #定义相应的文件名
    f = open(name1,'w')
    print('请输入内容(在最后一行单独输入"##"保存退出)：')
    while 1:
        write_words = input()
        if write_words != '##':
            f.write('%s\n' % write_words)  #  \n 用于在文件中换行
        else:
            break
    f.close()
name = input('请输入文件名：')
Write_files(name)
