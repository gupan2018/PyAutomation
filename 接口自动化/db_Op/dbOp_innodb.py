__author__ = 'Administrator'
import mysql.connector

config = {'host':'120.24.235.105',
          'user':'student2',
          'password':'student2@',
          'port':3306,
          'database':'python',
          'charset':'utf8'}

cnn = mysql.connector.connect(**config)

cursor = cnn.cursor()

#建表

sql_create_table_innodb = 'CREATE TABLE python_4_yuangungun_innodb02\
    (id int(10) NOT NULL AUTO_INCREMENT,\
    name varchar(10) DEFAULT NULL,\
    age int(3) DEFAULT NULL,\
    PRIMARY KEY (id))\
    ENGINE=InnoDB DEFAULT CHARSET=utf8'

#插入数据

sql_insert1 = 'insert into python_4_yuangungun_innodb02 (name, age) values ("测试数据01", 24)'

sql_insert2 = 'insert into python_4_yuangungun_innodb02(name , age) values (%s, %s)'
data1 = ("放羊", 28)

sql_insert3 = 'insert into python_4_yuangungun_innodb02(name, age) values (%(name)s, %(age)s)'
data2 = {"name":"甜甜", "age":18}

sql_insert4 = 'insert into python_4_yuangungun_innodb02(name, age) values (%s, %s)'
data3 = [
    ("测试数据1", 25),
    ("测试数据2", 21),
    ("测试数据3", 18),
]

#删除数据
'''
sql_delete = 'delete from python_4_yuangungun_innodb02 where id > 1'
'''

#查询数据

sql_select = 'select * from python_4_yuangungun_innodb02'

try:
    #新建表

    cursor.execute(sql_create_table_innodb)


    #删除数据
    '''
    cursor.execute(sql_delete)
    '''

    #插入数据

    cursor.execute(sql_insert1)

    cursor.execute(sql_insert2, data1)

    cursor.execute(sql_insert3, data2)

    cursor.executemany(sql_insert4, data3)

    #查询
    cursor.execute(sql_select)
    print(cursor.fetchall())

except mysql.connector.Error as e:
    print("sql error\n", e)
finally:
    cnn.commit()
    cursor.close()
    cnn.close()