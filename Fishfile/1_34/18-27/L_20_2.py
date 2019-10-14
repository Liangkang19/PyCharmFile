str1 = 'ABCaEFDb456ABCbDCE'
lenth = len(str1)
countA = 0
countB = 0
countC = 0
for i in range(lenth):
    if str1[i] == '\n':
        continue
    if str1[i].isupper():
        if countB == 0:
            countA = countA + 1
        else:
            countC = countC + 1
        continue
    if str1[i].islower() and countA == 3:
        countB = 1
        countA = 0
        target = i
        continue
    if str1[i].islower() and countC == 3:
        print(str1[target],end='')
    countA = 0
    countB = 0
    countC = 0
  
            

