def next1():
    print('我在next()函数里...')
    pre1()

def pre1():
    print('我在pre()函数里...')

def fun(x):
    x = 1314
    print(x,end = '')
x = 520                 #由于fun(x)函数输入实参后，该实参在函数内已经被固定为其它值
fun(x)                  #所以实参x，不影响函数的运行
print(x)                #但实参x的值只是被函数调用，并没有改变原本实参的值
                        #输出结果为： 1314520
                      
