def countstr(*p):
    '统计出输入n个字符串中，英文，数字，空格，其它字符的次数'
    ying = 0
    kong = 0
    shuz = 0
    qita = 0
    lenth1 = len(p)
    for i in range(lenth1):
        for each in p[i]:
            if each.isalpha():
                ying = ying + 1
            elif each.isdigit():
                shuz = shuz + 1
            elif each == ' ':
                kong = kong + 1
            else:
                qita = qita + 1
        print('第%d个字符串有：%d个英文，%d个数字，%d个空格，%d个其它'%(i+1,ying,shuz,kong,qita))
# print 中的表示方法
    
