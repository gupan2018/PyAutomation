# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import configparser
import os
import sys


class IniParser():
    def __init__(self, ini_file_path):
        self.cf = configparser.ConfigParser()
        if not os.path.isfile(ini_file_path):
            sys.stderr.write('file not exists %s' % ini_file_path)
            sys.exit(1)
        self.cf.read(ini_file_path)

    def get_sections(self):
        return self.cf.sections()

    def get_options(self, section):
        return self.cf.options(section)

    def get_item(self, section, option):
        return self.cf.get(section, option)