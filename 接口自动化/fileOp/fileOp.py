__author__ = 'Administrator'
import os
t = os.getcwd()
print(t)

print(os.path.abspath("."))

s = os.path.join(t, "python_test")

os.mkdir(s)
print(os.listdir())
os.rmdir(s)
print(s)
print(os.path.split(s))

print(type(os.path.splitext(s)))

'''
f = open("G:\\test.txt", "rb")

f.seek(3, 0)
f.seek(-10, 2)
print(f.tell())
'''
'''
list = ["xjnioando", "xncuincs", "ncuind"]
print(f.name)

f.write("my name is yuangungun")
f.write("我现在在找工作")
f.writelines(list)
f.writelines(list)
f.writelines(list)
f.writelines(list)
f.writelines(list)
f.close()
'''


#print(f.read(10))


