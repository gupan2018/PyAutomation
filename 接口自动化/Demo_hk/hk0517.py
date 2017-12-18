__author__ = 'Administrator'

#第一题
a = [1, 2, 3, "this is a list"]
b = [4, 5, 6, "这是第二个列表"]

print(a + b)

#第二题
print(a * 2)

#第三题
print(a[2])

#第四题
print(b[1], b[2])

#第五题
print(a[2:len(a)])

#第六题
L = [['Apple', 'Google', 'Microsoft'],
     ['java', 'python', 'Ruby', 'PHP'],
     ['Adam', 'Bart', 'Lisa']]

print(L[0][0], L[1][1], L[2][2])

#第七题
list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]

list1.extend(list2)
list1 = list(set(list1))
print(list1)

#第九题
s = "lemon python"
print(s)
print(s)

#第10题
date = input("请输入日期\n")
print("%s年%s月%s日"%(str(date[0:4]),str(date[4:6]),str(date[6:8])))

#第11题
dic = {"0":"星期天",
       "1":"星期一",
       "2":"星期二",
       "3":"星期三",
       "4":"星期四",
       "5":"星期五",
       "6":"星期六",}
a = input("请输入要查询的日期\n")
a = int(a)
a = a % 7

print(dic.get(str(a), "输入有误"))