__author__ = 'Administrator'
import xlwt3

class Excel_write:
    def __init__(self, path, sheet_name):
        self.__wb = xlwt3.Workbook()
        self.__path = path
        self.__sheet_name = sheet_name
        self.__sheet = self.__wb.add_sheet(self.__sheet_name)
        pass

    def getWb(self):
        return self.__wb

    def getSheet(self):
        return self.__sheet

    def saveSheet(self):
        self.__wb.save(self.__path)