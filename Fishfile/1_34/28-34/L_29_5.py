# 编写一个程序，当输入文件名和行数(N1:N2)之后，打印出该文件的N1:N2之间的内容。
def Read_file2(name,lines):
    if lines.strip() == ':':
        begin = '1'
        end   = '-1'
        
    (begin, end) = lines.split(':')

    if begin == '':
        begin = '1'
    if end == '':
        end = '-1'
    if begin == '1' and end == '-1':
        prompt = '的全文'
    elif begin == '1':
        prompt = '从开始%s' % end
    elif end == '-1':
        prompt = '从%s到结束' % begin
    else:
        prompt = '从第%s行到第%s行' % (begin,end)
    print('\n文件%s%s的内容如下：\n' % (begin,end))
    begin = int(begin)
    end = int(end)
    lines = end - begin
    f = open(name)
    for i in range(begin):
        f.readline()
    if lines < 0:
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline(),end='')
    f.close()
name = input('请输入要打开的文件：')
lines = input('请输入需要显示的行数[格式如13:21,:21或13:]：')
Read_file2(name,lines)






    
    
     
