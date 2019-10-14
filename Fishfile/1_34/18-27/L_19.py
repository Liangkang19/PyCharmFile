#函数变量的作用域：局部变量与全局变量
#可以在函数中使用 global x 的形式，重新定义全局变量x

def discounts(price,rate):
	f_price = price * rate      # 其中f_price称为局部变量，函数外无法访问该局部变量
        global x
        x = 5                       # 此时x为全局变量，可在任意位置调用
	return f_price

o_price = float(input('原价：'))
n_rate = float(input('新折扣率：'))
n_price = discounts(o_price,n_rate) # 其中n_prince称为全局变量，任何位置中都可以访问
print('折后价：',n_price)

#在某一函数中修改全局变量，被修改的全局变量只能在该函数中使用
#但在函数外的全局变量值，不会因为函数里的改变而改变。
