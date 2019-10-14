# redis数据库检测

from redis import StrictRedis
red = StrictRedis(host='localhost', port=6379, db=0, password='2003asdf')
# red.set('name', 'Bob')
# print(red.get('name'))
# print(red.exists('mykey1'))
print(red.dbsize())

