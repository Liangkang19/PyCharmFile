#编写函数，统计某长度为2的子字符串在另一个字符串中出现的次数
#输出'子字符串 x 在目标字符串中输出次数 n '

def findstr(str1,str2):
    count = 0
    lenth1 = len(str1)
    lenth2 = len(str2)
    lenth3 = lenth2 - lenth1 + 1
    lenth4 = lenth2 - 1
    if str1 not in str2:
        print(str1+'在'+str2+'中出现次数为0')
    else:
        for i in range(lenth3):
            if str2[i] == str1[0]:
                if str2[i+1] == str1[1]:
                    count = count + 1
        print(str1+'在'+str2+'中出现次数为',count)
        
