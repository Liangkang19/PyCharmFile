#字符串操作命令：
str1 = 'abcA DEFA 12 aLK14  '
str1[2]               #索引列表中的某个值
str1[1:]              #从第1个元素索引到最后一个元素
str1[:3]              #从第0个元素索引到第2个元素
str1[1:3]             #从第0个元素索引到第2个元素
str1[1:10:2]          #从第0个元素索引到第9个元素，中间间隔1个元素

str1.capitalize()     #将字符串首字母大写
str1.casefold()       #将字符串中的大写字母改为小写字母
str1.lower()          #将字符串中的小写字母改为大写字母

str1.center(10)       #将文本居中，并用空格填充至10的长度，参数长度要大于字符串长度
str1.ljust(20)        #将字符串左对齐，并使用空格填充至长度为 20
str1.rjust(20)        #将字符串右对齐，并使用空格填充至长度为 20

str1.count('a')       #计算字符串中‘a’出现的次数
str1.endswith('14')   #判断字符串是否以相应字符（串）结尾，
str1.startswith('ab'1,6) #判断字符串是否以相应字符（串）开头，可选字符串中的起始和结束检测点
str1.find('l2')       #检测‘12’是否在字符串中，不在，返回-1；在，返回该字符的起始位置数
str1.rfind('l2')      #从字符串右侧开始查找
str1.index('12')      #与find类似，若不在字符串中，返回错误

str1.isalnum()        #若字符串中都是字母或数字，则返回 True，否则返回 False
str1.isalpha()        #若字符串中都是字母，则返回 True，否则返回 False
str1.isdecimal()      #若字符串只包含十进制数字，则返回 True，否则返回 False
str1.isdigit()        #若字符串只包含数字则返回 True，否则返回 False
str1.islower()        #若字符串中的字符都是小写，则返回 True，否则返回 False
str1.isnumeric()      #若字符串中只包含数字字符，则返回 True，否则返回 False
str1.isspace()        #若字符串中只包含空格，则返回 True，否则返回 False
str1.istitle()        #若字符串中单词都以大写开始，其余字母均小写，则返回 True，否则返回 False

str1.isupper()        #若字符串中字符都是大写，则返回 True，否则返回 False
str1.swapcase()       #翻转字符串中的大小写字母


str1.join('12345')    #以字符串作为分隔符，插入到'12345' 中所有的字符之间
str1.lstrip()         #去掉字符串左边的所有空格
str1.rstrip()         #删除字符串末尾的空格。
str1.replace('AA','BB',1) #将字符串‘BB’替换字符串‘AA’，替换次数不超过1次（可省参数）
str1.split()          #以将字符串中的空格为基准，将字符串分割为列表
str1.split('A')       #以将字符串中的‘A’为基准，将字符串分割为列表
str1.strip()          #删除字符串前边和后边所有的空格
str1.strip('A')       #删除字符串前边和后边所有的‘A’
str1.istitle()        #将字符串中单词都以大写开头，其余字母小写
str1.translate(str.maketrans('AA', 'BB')) #将字符串中的‘BB’替换‘AA’
str1.zfill(10)        #返回长度为‘10’的字符串，原字符串右对齐，前边用 0 填充。

str2 = 'I\tlove\tyou'
str2.expandtabs()     #将\t转换为8个空格（默认），可添加参数




