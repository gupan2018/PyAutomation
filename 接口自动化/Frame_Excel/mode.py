__author__ = 'Administrator'
import configparser

class Mode:
    def __init__(self, path):
        conf = configparser.ConfigParser()
        conf.read(path)
        self.__mode = conf.get("mode", "mode_value")
        str = conf.get("mode", "case_list")
        self.__list = str.split(",")

    def getMode(self):
        return self.__mode

    def getList(self):
        newList = []
        for x in self.__list:
            newList.append(int(x))
        return newList