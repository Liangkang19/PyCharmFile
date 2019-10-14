#内嵌函数与闭包

def fun1():
	print('fun1正在被调用...')
	def fun2():                         #在fun1()函数中定义fun2()函数
		print('fun2正在被调用...')  
	fun2()                              #在函数中调用fun2()函数
	
def funx(x):                 #闭包：在funx(x)中定义funy(y)时，funx(x)的返回值是：函数funy
	def funy(y):
		return x*y
	return funy          #调用方法 funx(x):返回一个函数，funx(x)(y)：返回funy(y)中的返回值

# nonlocal 的应用
def fun1():                  #使用nonlocal之后，fun2()中的x值才能用fun1()中的x值
        x = 5                #与上一闭包不同，fun1()返回值是：调用fun2()函数
        def fun2():
                nonlocal x
                x = x + 2
		return x
	return fun2()           
        
    	
			
		
	
