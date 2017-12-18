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

sql_create_table_innodb = 'CREATE TABLE python_4_yuangungun_innodb\
    (id int(10) NOT NULL AUTO_INCREMENT,\
    name varchar(10) DEFAULT NULL,\
    age int(3) DEFAULT NULL,\
    PRIMARY KEY (id))\
    ENGINE=INNODB DEFAULT CHARSET=utf8'

try:
    cursor.execute(sql_create_table_innodb)

except mysql.connector.Error as e:
    print("sql error\n", e)
finally:
    cnn.commit()
    cursor.close()
    cnn.close()
