def Hui(str1):
    L1 = len(str1)
    L2 = L1 // 2
    last = L1 - 1
    temp = 1
    for start in range(L2-1):
        if str1[start] != str1[last]:
            temp = 0
        last = last - 1
    if temp == 0:
        print(str1,'不是回文！')
    else:
        print(str1,'是回文！')
str1 = input('请输入一句话：')
Hui(str1)
        
    
