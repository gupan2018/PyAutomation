__author__ = 'Administrator'
import random
import string

print("作业1：第一题\n")
age = input("请输入年龄：\n")
nameNum = input("请问想要输出多个个字的名字？\n")

list_xing = ["赵", "钱", "孙", "李"]
list_ming = ["闯", "想", "美", "登", "阳", "贱","攀", "梦", "军", "铁"]

class MyPrint:
    def __init__(self,list_xing, list_ming, nameNum, age):
        self.list_xing = list_xing
        self.list_ming = list_ming
        self.nameNum = nameNum
        self.age = age

    def myprint(self):
        print("我的名字是%s,我的年龄是%s"%(random.choice(self.list_xing).join(random.sample(self.list_ming, self.nameNum - 1)), self.age))

test = MyPrint(list_ming, list_xing,int(nameNum),int(age))

test.myprint()


#作业1：第二题
print("作业2：第二题：\n")
num = input("请输入要输入的字符串的长度：\n")
list_Table = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

class StrPrint:
    def __init__(self, list_Table, num):
        self.list_Table = list_Table
        self.num = num

    def StrPrint(self):
        print("本次输出的字符串为：%s"%"".join(random.sample(self.list_Table, self.num)))

Test02 = StrPrint(list_Table, int(num))
Test02.StrPrint()


#作业2
print("作业2：\n")
class ReverseStr:
    def __init__(self, str):
        self.str = str
        self.print = ""

    def reverse(self):
        for i in range(len(self.str) - 1, -1, -1):
            self.print += self.str[i]
        print(self.print)

testStr = input("请输入要倒序输出的字符串：\n")

reverseTest = ReverseStr(testStr)
reverseTest.reverse()