__author__ = 'Administrator'
import configparser

class Mode:
    def __init__(self, path):
        conf = configparser.ConfigParser()
        conf.read(path)
        self.mode = conf.get("mode", "mode_value")
        str = conf.get("mode", "case_list")
        self.list = str.split(",")

    def getMode(self):
        return self.mode

    def getList(self):
        return self.list