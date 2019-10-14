# 异常检测:try-except语句 
# try:
#    检测范围
# except Exception[as reason]:
#    出现异常(Exception)后的处理代码
try:
    int('abc')                         # 某处出现错误，直接跳到错误类型处执行
    sum1 = 1 + '1'                     # 此时本语句不执行
    f1 = open('Laosi.txt')
    print(f1.read())
    f1.close()
except OSError as reason:
    print('文件出错！错误原因：'+ str(reason))
except TypeError as reason:
    print('类型出错！错误原因：'+ str(reason))
except ValueError as reason:
    print('赋值出错！错误原因：'+ str(reason)) #只执行此处错误提示语句！

# 异常检测:try-except-finally语句 
# try:
#    检测范围
# except Exception[as reason]:
#    出现异常(Exception)后的处理代码
# finally:
#    即使异常发生也要执行的语句

try:
    f1 = open('Laosi.txt','w')
    print(f1.write())
    sum1 = 1 + '1'          # 此处异常发生后，需要对文件进行xxx.close()操作
except OSError as reason:
    print('文件出错！错误原因：'+ str(reason))
except TypeError as reason:
    print('类型出错！错误原因：'+ str(reason))
except ValueError as reason:
    print('赋值出错！错误原因：'+ str(reason)) 
finally:
    f1.close()              # 所以在finally之后添加相关语句








    
