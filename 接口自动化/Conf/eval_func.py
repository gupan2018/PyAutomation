__author__ = 'Administrator'
list = "[1,2,3,4,5]"
tuple = "(1,2,3,4,5)"
dic = "{'name':'gupan', 'age':18}"

list = eval(list)
tuple = eval(tuple)
dic = eval(dic)

print(type(list), type(tuple), type(dic))
