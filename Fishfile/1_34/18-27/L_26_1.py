dict1 = {}
def Load():
    while 1:
        print('---新建用户：N/n---')
        print('---登录账号：E/e  ---')
        print('---退出程序：Q/q  ---')
        temp = input('请输入指令代码:')
        if (temp == 'N') or (temp == 'n'):
            name = input('请输入用户名：')
            while 1:
                if name in dict1.keys():
                    name = input('此用户名已被注册，请重新输入用户名：')
                else:
                    break
            password = input('请输入密码：')
            dict1[name] = password
            print(name,'恭喜你成为本站会员')
            print('注册成功，请登录...')
        if (temp == 'E') or (temp == 'e'):
            name = input('请输入用户名：')
            while 1:
                if name not in dict1.keys():
                    name = input('输入的用户名不存在，请重新输入用户名：')
                else:
                    break
            password = input('请输入密码：')
            i = 3
            while 1:
                if password != dict1.get(name):
                    password = input('密码错误，请重新输入密码：')
                else:
                    break     
            print('欢迎进入本系统......')
            break
        if (temp == 'Q') or (temp == 'q'):
            print('程序退出中......')
            break
                
            
            
            
       
