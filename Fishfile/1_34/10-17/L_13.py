#元组不可以被修改

tuple1 = (1,2,3,4,5,6,7,8,9)                              #","是元组的关键
tuple1[2]                                                 #访问元组中的元素
tuple1[3:]
tuple1[:5]
tuple1[1:8:2]

tuple2 = tuple3[:]                                        #复制元组
temp = ('小甲鱼','小布丁','黑夜','迷途','HBO')
temp = temp[:2]+('TVB',)+temp[2:]                         #拼接元组时","不可省
temp = ('小甲鱼', '小布丁', 'TVB', '黑夜', '迷途', 'HBO') #新的temp
temp = ()                                                 #创建新元组

