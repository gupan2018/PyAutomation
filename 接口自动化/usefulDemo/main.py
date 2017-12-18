__author__ = 'Administrator'
from Frame_db.database import Database
import mysql.connector
import configparser
from usefulDemo.runCase import RunCase
from usefulDemo.wb import Workbook

path_db = "db.conf"
path_read_Excel = "test_data.xlsx"
path_save_Ecxcel = "result.xls"
path_data = "test_data.conf"

cnn = Database(path_db).connect_db()
cousor = cnn.cursor()
wb = Workbook(path_read_Excel, path_save_Ecxcel)

RunCase(path_data, cousor, wb).runcase()
cousor.close()
cnn.close()
'''conf = configparser.ConfigParser()
conf.read(path_data)

url = conf.get("url", "register")
print(url)'''