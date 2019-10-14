# 实现一个用于登记用户账号信息的界面(带“*”号的为必填项，要求有输入并且不能为空)

import easygui
title1 = '账号中心'
msg1 = '''[请输入个人信息:]
[带*号的内容必填]'''
name1 = ['*用户名', '*真实姓名', '固定电话', '*手机号码', 'QQ号码', '*电子邮箱']
lenth1 = len(name1)
value1 = []
value1 = easygui.multenterbox(msg=msg1, title=title1, fields=name1, values=value1)
while 1:
    if value1 == 'None':
        break
    msg2 = ''
    for i in range(lenth1):
        name2 = name1[i].strip()    # 将name1中的元素去掉前后空格，形成一个字符串
        value2 = value1[i].strip()  # 将value1中的元素去掉前后空格，形成一个字符串
        if value2 == '' and name2[0] == '*':
            msg2 = msg2 + ('[%s]必须填\n' % name1[i])   # 若value2中值为空，name2字符串中第一个字符是'*'
    if msg2 == '':
        break
    value1 = easygui.multenterbox(msg=msg2, title=title1, fields=name1, values=value1)

print('用户资料如下:')
for i in range(lenth1):
    print('%s : %s' % (name1[i], value1[i]))









