__author__ = 'Administrator'
import mysql.connector

'''
#组装查询列表
assemble_testList(cursor, test_list)
#根据列表数据，执行对应sql
exe_sql(cursor, test_list, http)
'''

def assemble_testList(cursor, test_list):
    sql = 'SELECT COUNT(*) FROM test_data'
    try:
        cursor.execute(sql)
    except mysql.connector.Error as e:
        print("组装查询id列表失败，错误原因如下：\n",e)

    list = cursor.fetchone()
    num = list[0]
    for i in range(1, num + 1):
        test_list.append(i)

#执行sql语句
def exec_select_sql(cursor, test_case, http, datalist):
        sql = 'SELECT * FROM test_data WHERE case_id = %s'%test_case
        try:
            cursor.execute(sql)
        except mysql.connector.Error as e:
            print(e)

        list = cursor.fetchone()

        test_url = list[3]
        http_method = list[1]
        mobile_phone = list[4]
        test_method = list[6]


        regname = list[5]
        test_data = {
            "mobilephone":mobile_phone,
            "regname":regname,
            "pwd":"123456"
        }
        datalist.append(test_url)
        datalist.append(test_data)
        datalist.append(http_method)
        datalist.append(test_method)


def test_begin(test_method, http, test_url, test_data):
    if test_method == "GET":
        http.get_req(test_url, test_data)
    elif test_method == "POST":
        http.post_req(test_url, test_data)
    else:
        print("test_method错误，只支持POST和GET方法")