__author__ = 'Administrator'
import mysql.connector
from datetime import datetime
import time

'''
#组装查询列表
assemble_testList(cursor, test_list)
#根据列表数据，执行对应sql
exe_sql(cursor, test_list, http)
'''

def assemble_testList(test_Num, test_list):
    for i in range(1, test_Num):
        test_list.append(i)