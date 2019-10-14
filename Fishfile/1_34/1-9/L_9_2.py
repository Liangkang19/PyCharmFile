count = 3
password = '2019lk'
while count:
    p1 = input('请输入密码 :')
    p2 = str(p1)
    if p2 ==  password:
        print('密码正确，进入程序......',end = '')
        break               # 执行break语句时，跳出上一个while处退出循环
    elif '*'in p2:
        print('密码中不能有"*"号! 您还有',count,'次机会。')
        continue            # 执行continue语句时，跳到上一个while处继续循环
    else:
        count = count - 1
        if count > 0:
            print('密码错误，您还有',count,'次机会。')
        else:
            print('输入密码错误次数过多，账号被锁定！')
        

