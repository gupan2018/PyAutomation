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

sql_select = 'select * from python_4_yuangungun_innodb'
try:
    cursor.execute(sql_select)
    #查询
    #fetchone()函数用法
    '''
    i = cursor.fetchone()
    while(i):
        print(i)
        i = cursor.fetchone()
    '''

    #fetchall()函数用法
    result = cursor.fetchall()
    print(result)
    for i in result:
        print(type(i))
        print(i)


except mysql.connector.Error as e:
    print("sql error\n", e)
finally:
    cursor.close()
    cnn.close()