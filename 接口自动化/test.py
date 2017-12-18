'''
2.利用random 模块完成下列操作
编程要求：
1)写一个类，包含初始化函数以及其他两个函数。初始化函数里面传递sequence范围以及长度值。
2)第一个函数：利用sample生成一个指定长度的列表。
3)第二个函数：类内部调用第一个函数，完成指定列表转换成字符串。作为人的姓名。
4)第三个函数：利用randint随机生成一个整数值，作为人的年龄。
5)第四个函数：利用choice随机生成男女二字，作为人的性别。
6)第五个函数：类内部调用第二个 第三个 第四个函数，实现一个功能：打印这个人的姓名、年龄、性别
7)创造实例完成调用
'''
import random

class PrintName:
    #初始化函数
    def __init__(self,range,length):
        self.range=range
        self.length=length

    #利用sample生成一个指定长度的列表
    def list(self):
        list=random.sample(self.range,self.length)
        return list

    #类内部调用第一个函数，完成指定列表转换成字符串。作为人的姓名
    def name(self):
        a=self.list()
        b="".join(a)
        return b

    #利用randint随机生成一个整数值，作为人的年龄
    def test_age(self):
         self.age=random.randint(1,100)
         return self.age

    #利用choice随机生成男女二字，作为人的性别
    def test_sex(self):
         self.sex=random.choice(["男","女"])
         return self.sex

    #类内部调用第二个 第三个 第四个函数，实现一个功能：打印这个人的姓名、年龄、性别
    def printFunction(self):
        name=self.name()
        age=self.test_age()
        sex=self.test_sex()
        msg="姓名："+name + "年龄：" + str(age) + ", "+ "性别：" + sex
        return msg

    #存储到本地
    # def save(self):
    #     f=open("E:\\homework0928.txt",'w+')
    #     printResult=self.printFunction()
    #     print(printResult,file=f)
    #     f.close()

printName=PrintName("若雨婷晟涵雅梦舒婳檀雅若熙雯语嫣妍洋滢沐卉琪涵佳琦伶韵思睿清菡欣溶雪娴梦梵",2)
f=open("E:\\homework0928.txt",'w+')
for i in range(100):
    msg = printName.printFunction()
    print(msg,file=f)
f.close()