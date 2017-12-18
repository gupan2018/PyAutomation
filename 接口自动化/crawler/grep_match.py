__author__ = 'Administrator'
import re

class Grep_match:
    def __init__(self, grep_exp, matched_str):
        self.grep_exp = grep_exp
        self.matched_str = matched_str

    def exec_grep(self):
        wordre = re.compile(self.grep_exp)
        list = wordre.findall(self.matched_str)
        return list