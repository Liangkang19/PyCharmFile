#列表相关命与令操作

empty = []               #创建空列表
mix.append('Baidu')      #向列表尾部添加元素
mix.extend(['HY','def']) #向列表尾部添加新的列表
mix.insert(0,'牡丹')     #向列表指定位置添加新的元素
mix.insert(1,'小甲鱼')

mix = ['abc',3.14,'黑夜',55,3.14,[1,2,3]]
mix[0]                   #访问列表中的元素
mix[5][1]
mix2 = [1,[1,2,['小甲鱼']],3,5,8,13,18]
mix2[1][2][0] = '小鱿鱼' #替换列表中的元素

mix[1:3]                 #从列表中索引元素(不包含3)
mix[:3]
mix[1:]
mix[1:5:2]

mix1 = mix[:]            #拷贝列表 
mix1 = mix.copy()

mix.remove('小甲鱼')     #从列表删除元素
del mix[5]
del mix                  #删除列表
mix.pop()                #删除某元素，并将该元素返回显示
mix.pop(2)
mix.clear()              #清空列表


mix.count(3.14)          #某元素在列表中出现的次数
mix.index(3.14)          #某元素在列表中首次出现的位置
mix.index(3.14，2,5)     #某元素在列表中指定范围内首次出现的位置
mix.reverse()            #首尾顺序互换
mix.sort()               #元素从小到大排列
mix.sort(reverse = True) #元素从大到小排列


list1=[123,567]
list2=[234,123]          
list1 < list2            #list1与list2比较时，只比较第0个元素
list3 = list1 + list2    #列表相加
list3 * 3                #将列表中的元素复制3次
123 in list3             #判断某元素是不是在列表中
123 not in list3
123 in list3[1]          #判断某元素是不是在列表中的字列表


mix = [x**2 for x in range(10)]   #列表解析








