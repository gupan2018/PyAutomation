from Frame_db.database import Database
import mysql.connector
import configparser
from usefulDemo.runCase import RunCase
from usefulDemo.wb import Workbook

path_db = "db.conf"
path_read_Excel = "G:\\Python\\ExcelOp\\data.xlsx"
path_save_Ecxcel = "G:\\Python\\ExcelOp\\result.xls"
path_data = 'test_data.conf'

cnn = Database(path_db).connect_db()
cousor = cnn.cursor()
wb = Workbook(path_read_Excel, path_save_Ecxcel)

sql_create_table='CREATE TABLE ygg_test_data02 ' \
                 '(case_id int(10) NOT NULL AUTO_INCREMENT, ' \
                 'http_method varchar(10) DEFAULT NULL, ' \
                 'request_name varchar(30) DEFAULT NULL, ' \
                 'request_url varchar(100) DEFAULT NULL, ' \
                 'mobilephone varchar(11) DEFAULT NULL,'\
                 'regname varchar(20) DEFAULT NULL,'\
                 'pwd varchar(20) DEFAULT NULL,'\
                 'amount varchar(10) DEFAULT NULL,'\
                 'memberId varchar(10) DEFAULT NULL,'\
                 'title varchar(20) DEFAULT NULL,'\
                 'loanRate varchar(10) DEFAULT NULL,'\
                 'loanTerm varchar(4) DEFAULT NULL,'\
                 'loanDateType varchar(1) DEFAULT NULL,'\
                 'repaymemtWay varchar(2) DEFAULT NULL,'\
                 'biddingDays varchar(2) DEFAULT NULL,'\
                 'id varchar(10) DEFAULT NULL,'\
                 'status varchar(2) DEFAULT NULL,'\
                 'test_method varchar(100) DEFAULT NULL,' \
                 'test_desc varchar(100) DEFAULT NULL,'\
                 'PRIMARY KEY (case_id)) ' \
                 'ENGINE=MyISAM ' \
                 'DEFAULT CHARSET=utf8'

'''
sql_create_table='CREATE TABLE ygg_test_result02 ' \
                 '(case_id int(10) NOT NULL AUTO_INCREMENT, ' \
                 'http_method varchar(10) DEFAULT NULL, ' \
                 'request_name varchar(30) DEFAULT NULL, ' \
                 'request_url varchar(100) DEFAULT NULL, ' \
                 'mobilephone varchar(11) DEFAULT NULL,'\
                 'regname varchar(20) DEFAULT NULL,'\
                 'pwd varchar(20) DEFAULT NULL,'\
                 'amount varchar(10) DEFAULT NULL,'\
                 'memberId varchar(10) DEFAULT NULL,'\
                 'title varchar(20) DEFAULT NULL,'\
                 'loanRate varchar(10) DEFAULT NULL,'\
                 'loanTerm varchar(4) DEFAULT NULL,'\
                 'loanDateType varchar(1) DEFAULT NULL,'\
                 'repaymemtWay varchar(2) DEFAULT NULL,'\
                 'biddingDays varchar(2) DEFAULT NULL,'\
                 'id varchar(10) DEFAULT NULL,'\
                 'status varchar(2) DEFAULT NULL,'\
                 'test_method varchar(100) DEFAULT NULL,' \
                 'test_desc varchar(100) DEFAULT NULL,'\
                 'result_status int(1) DEFAULT NULL,'\
                 'code varchar(10) DEFAULT NULL,'\
                 'msg varchar(100) DEFAULT NULL,'\
                 'PRIMARY KEY (case_id)) ' \
                 'ENGINE=MyISAM ' \
                 'DEFAULT CHARSET=utf8'
                 '''


#RunCase(path_data, cousor, wb)


try:
    cousor.execute(sql_create_table)
    pass
except mysql.connector.Error as e:
    print(e)