__author__ = 'Administrator'
#第一题
test = [2, 56, 98, 9, 34, 87, 1, 5]

def bubble(list):
    for i in range(0, len(list) - 1):
        for j in range(i + 1, len(list)):
            if test[i] > test[j]:
                test[i], test[j] = test[j], test[i]
    return list

print(bubble(test))

#第二题
a = [5, 6, 7, 9, 10, 23, 45]
'''def reverse(list):
    if len(list) >= 2:
        for i in range(0, int(len(list) / 2)):
            list[i], list[len(list) - i - 1] = list[len(list) - i - 1],  list[i]
    return list

print(reverse(a))
'''
a.reverse()
print(a)

#函数模块
#第一题
def print_eg01():
    return ("柠檬班帮帮达")

#第二题
def print_eg02(name):
    return ("%s说柠檬班帮帮达"%name)

#第三题
def print_eg03(a, b):
    print(a + b)

#第四题
def print_eg04(a, b = 8):
    print(a + b)

#第五题
def add(a, b, c):
    return a + b + c

#第一题调用
print(print_eg01())

#第二题调用
print(print_eg02("圆滚滚"))

#第三题调用
print_eg03(1, 2)

#第四题调用
print_eg04(2)
print_eg04(2, 5)

#第五题调用
print(add(1,2 ,3))
