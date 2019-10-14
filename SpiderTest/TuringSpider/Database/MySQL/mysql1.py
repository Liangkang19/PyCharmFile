import pymysql

# 第三步：向表单中插入数据
id1 = '1008611'
user1 = 'Bob'
age1 = 20
db = pymysql.connect(host='localhost', user='root', password='2003asdf', port=3306, db='spdata1')
cursor = db.cursor()
sql = 'INSERT INTO students1(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id1, user1, age1))
    db.commit()
except:
    db.rollback()
db.close()


# 第二步：创建表单sql
# db = pymysql.connect(host='localhost', user='root', password='2003asdf', port=3306, db='spdata1')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students1 \
#         (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

# 第一步：创建数据库spdata1
# db = pymysql.connect(host='localhost', user='root', password='2003asdf', port=3306')
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version: ', data)
# cursor.execute('CREATE DATABASE spdata1 DEFAULT CHARACTER SET utf8mb4')
# db.close()
