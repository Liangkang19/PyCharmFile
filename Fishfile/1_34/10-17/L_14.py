#字符串
str1 = '小甲鱼小布丁'
str1[2]
str1[1:]
str1[:3]
str1[1:3]
str1 = str1[:3]+'插入的字符串'+str1[3:]

str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1[0::3]       #从第0个元素开始，每隔2个元素，打印第三个元素
'ilovefishc.com'

#字符串操作
str1 = ('xiaojiayu')
str1.capitalize()    #字符串首字母大写
'Xiaojiayu'
str2 = ('DAXIE')
str2.casefold()      #将整个字符串改为小写
'daxie'
str2.center(10)      #将文本居中，并用空格填充至10的长度
'  DAXIE   '
str2.count('A')      #计算字符串中‘A’出现的次数
1
>>> str2.endswith('E')  #判断字符串是否以相应字符结尾
True
str2.endswith('ET')
False
str3 = 'I\tlove\tyou'
str3.expandtabs()
'I       love    you'
str3.find('l')
2
str3.islower()
False
str4 = 'FishC'
str4.istitle()
False
str4 = 'Fishc'
str4.istitle()
True
str4.join('12345')
'1Fishc2Fishc3Fishc4Fishc5'
str5 = '    abcdef'
str5.lstrip()
'abcdef'
str6 = 'I love FishC'
str6.partition('ov')
('I l', 'ov', 'e FishC')
str6.replace('FishC','fishc')
'I love fishc'
str6.split()
['I', 'love', 'FishC']
str6.split('o')
['I l', 've FishC']
str7 = '    dddddkkkkk    '
str7.strip()
'dddddkkkkk'

#字符串的格式化
"{0} love {1}.{2}".format("I","FishC","com")
'I love FishC.com'
 "{a} love {b}.{c}".format(a="I",b="FishC",c="com")
'I love FishC.com'
"{0} love {b}.{c}".format("I",b="FishC",c="com")
'I love FishC.com'
"{{0}}".format("不打印")
'{0}'
'{0:.1f}{1}'.format(27.658,'GB')
'27.7GB'



>>> '%c' % 97
'a'
>>> '%c %c %c' % (97,98,99)
'a b c'
>>> '%s' % 'I love FishC.com'
'I love FishC.com'
>>> '%d + %d + %d' % (97,98,97+98)
'97 + 98 + 195'
>>> '%d + %d = %d' % (97,98,97+98)
'97 + 98 = 195'
>>> '%o' % 10
'12'
>>> '%x' % 10
'a'
>>> '%X' % 10
'A'
>>> '%f' % 10
'10.000000'
>>> '%e' % 10.555566666
'1.055557e+01'
>>> '%E' % 10.55666655
'1.055667E+01'
>>> '1.055667E+01'
'1.055667E+01'


>>> '%5.1f' % 27.658
' 27.7'

>>> '%.2e' % 27.658
'2.77e+01'
>>> '%10d' % 5
'         5'
>>> '%-10d' % 5
'5         '
>>> '%+d' % 5
'+5'
>>> '%-d' % 5
'5'
>>> '%#o' % 10
'0o12'
>>> '%#x' % 10
'0xa'
>>> '%#d' % 10
'10'
>>> '%010d' % 5
'0000000005'











 
