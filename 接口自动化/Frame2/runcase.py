__author__ = 'Administrator'

import mysql.connector

class Runcase:
    def run_Case(self, http, cnn):
        cursor = cnn.cursor()
        sql = 'SELECT * FROM test_data WHERE case_id = 1'
        try:
            cursor.execute(sql)
            list = cursor.fetchone()
            http.reg_url = list[3]
            mobile_phone = list[4]
            regname = list[5]
        except mysql.connector.Error as e:
            print(e)
        finally:
            cursor.close()
            cnn.close()

        http.data = {
            "mobilephone":mobile_phone,
            "regname":regname,
            "pwd":"123456"
        }
        print("这是get方法")
        http.get_req()
        print("这是post方法")
        http.post_req()