# 编写一个程序，当输入文件名和行数(N)之后，打印出该文件的前N行内容。
def Read_file1(name,N):
    'name = 文件名， 1ine = 行数'
    print('\n将显示%s文件中前%s行的内容\n' % (name,line))
    f = open(name)
    n = int(N)
    for i in range(n):
        print(f.writelines(),end='')

    f.close()
name = input('请输入要打开的文件：')
N = input('请输入行数：')
Read_file1(name,line)
