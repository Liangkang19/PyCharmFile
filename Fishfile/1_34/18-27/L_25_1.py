print('---欢迎进入通信录程序---')
print('---1:查询联系人信息  ---')
print('---2:插入新的联系人  ---')
print('---3:删除已有联系人  ---')
print('---4:退出通信录程序  ---')

dict1 = {'阿峰':'12580','阿雄':'10010'}
while 1:
    num = int(input('请输入指令代码：'))
    if num == 1:
        name = input('请输入联系人姓名：')
        print(name,':',dict1[name])
    elif num == 2:
        name = input('请输入联系人姓名：')
        if name in dict1:
            print('您输入的联系人资料已存在-->',name,':',dict1[name])
            temp1 = input('是否修改用户资料(Yes/No):')
            if temp1 == 'Yes':
                number = input('请输入新的联系电话：')
                dict1[name] = number
                print(name,':',dict1[name])
            else:
                print(name,'的联系电话未修改，仍为:',dict1[name])
        else:
            number = input('请输入用户联系电话：')
            dict1[name] = number
            print(name,':',dict1[name])    
    elif num == 3:
        name = input('请输入联系人姓名：')
        if name in dict1:
            temp2 = input('是否要删除该用户资料(Yes/No):')
            if temp2 == 'Yes':
                del(dict1[name])
                print('该联系人信息已经被删除！')
            else:
                print(name,'的联系电话未被删除，仍为:',dict1[name])
        else:
            print('输入联系人姓名不存在！')
    elif num ==4:
        print('---  程序正在退出... ---')
        break
print('---感谢使用通信录程序！  ---')
