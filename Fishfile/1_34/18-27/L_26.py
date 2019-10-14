# 字典的各种内置方法
# fromkeys(): 创建并返回新的字典,原字典不变
dict1 = {}
dict1.fromkeys((1,2,3))            #输入一个参数时：{1: None, 2: None, 3: None}
dict1.fromkeys((1,2,3),('Number')) #输入两个参数时：{1: 'Number', 2: 'Number', 3: 'Number'}
dict1.fromkeys((1,2,3),('One','Two','Three')) #输出：{1: ('One', 'Two', 'Three'),
                                              #       2: ('One', 'Two', 'Three'),
                                              #       3: ('One', 'Two', 'Three')}
# 访问字典的方法
# keys():   访问字典中的key
# values(): 访问字典中的values
# items():  访问字典中的key 和 value
# get()  :  访问字典中key中的value值
# update(): 更新字典

dict2 = dict1.fromkeys(range(10),'迷')   
for key in dict2.keys():         
    print(key,end = '')

for value in dict2.values():
    print(value,end = '')

for item in dict2.items():
    print(item,end = '')
    
dict2.get(10)            #输入单个参数时，若找不到字典中对应的值，返回：None
dict2.get(10,'找不到')   #输入两个参数时，若找不到字典中对应的值，返回：第二个参数值(找不到)
dict2.get(5)             #字典中有对应的值，可返回该值
dict2.clear()            #清空字典
dict2.copy()             #拷贝字典
dict2.pop(2)             #将字典中2对应的value值弹出，此时字典中该值被删除
dict2.popitem(2)         #将字典中2对应的value值弹出(同时显示key和value),此时字典中该值被删除
dict2.update(6 = '失')   #将字典中6对应的value值更改为'失'

                                              
