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
#插入数据

#sql_insert1 = 'insert into python_4_yuangungun (name, age) values ("测试数据01", 24)'

'''
sql_insert2 = 'insert into python_4_yuangungun(name , age) values (%s, %s)'
data1 = ("放羊", 28)'''
sql_insert2 = 'insert into python_4_yuangungun_innodb (name) values (%s)'
data1 = ("放羊",)

sql_insert3 = 'insert into python_4_yuangungun_innodb(name, age) values (%(name)s, %(age)s)'
data2 = {"name":"甜甜", "age":18}

sql_insert4 = 'insert into python_4_yuangungun(name, age) values (%s, %s)'
data3 = [
    ("测试数据1", 25),
    ("测试数据2", 21),
    ("测试数据3", 18),
]
try:
    #插入数据
    #cursor.execute(sql_insert1)
    #cursor.execute(sql_insert2, data1)
    cursor.execute(sql_insert3, data2)
    #cursor.executemany(sql_insert4, data3)

except mysql.connector.Error as e:
    print("sql error\n", e)
finally:
    cnn.commit()
    cursor.close()
    cnn.close()

