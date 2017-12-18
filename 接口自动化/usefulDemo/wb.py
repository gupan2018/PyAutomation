__author__ = 'Administrator'
import xlrd
import xlwt3

class Workbook:
    def __init__(self, path_read, path_save):
        self.__read_wb = xlrd.open_workbook(path_read)
        self.__write_wb = xlwt3.Workbook()
        self.__path_save = path_save

    def getReadWb(self):
        return self.__read_wb

    def getWriteWb(self):
        return self.__write_wb

    def saveWriteWb(self):
        self.__write_wb.save(self.__path_save)