# 编写一个程序，当用户输入整数时正常返回，否则提示出错并要求重新输入
def Input_int():
    while 1:
        try:
            temp1 = input('请输入一个整数:')
            temp2 = int(temp1)
            return print(temp2)
            break
        except ValueError:
            print('输入错误！请重新输入。')

Input_int()
