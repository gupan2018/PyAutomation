__author__ = 'Administrator'
from runcase import Runcase
from database import Database
from HttpRequest import HttpRequest

path = "C:\\Users\\Administrator\\PycharmProjects\\test\\Frame2\\db.conf"

http = HttpRequest(path)
cnn = Database(path).connect_db()
runcase = Runcase()
runcase.run_Case(http, cnn)
