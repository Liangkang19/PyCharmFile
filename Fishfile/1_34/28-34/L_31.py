# pickle(腌菜)模块：存放模块
# unpickling      : 读取模块
import pickle
list1 = [123,3.14,'老四',[567,'afeng']]
dict1 = {1:'老四',
         2:'阿峰',
         3:'阿雄',
         4:'华农兄弟',
         5:'信誓蛋蛋',
         6:'阿一',
         7:'粤知一二'}
pickle_list1 = open('D:\\Program Files\\Python3.7\\Pythonfiles\\28-40\\list1.pkl','wb')
pickle_dict1 = open('D:\\Program Files\\Python3.7\\Pythonfiles\\28-40\\dict1.pkl','wb')
# 以二进制模式在指定文件夹中创建(.pkl)类型的文件

pickle.dump(list1,pickle_list1)    #使用pickle.dump(file,pickle_file)
pickle.dump(dict1,pickle_dict1)    #将file保存到pickle_file中

pickle_list1.close()               #指定文件夹中出现(.pkl)文件
pickle_dict1.close()

# 从(.pkl)文件中读取数据

pickle_list1 = open('D:\\Program Files\\Python3.7\\Pythonfiles\\28-40\\list1.pkl','rb')
pickle_dict1 = open('D:\\Program Files\\Python3.7\\Pythonfiles\\28-40\\dict1.pkl','rb')

list1 = pickle.load(pickle_list1)  #使用pickle.load(pickle_file)读取(.pkl)文件
dict1 = pickle.load(pickle_dict1)
print(list1)
print(dict1)






