__author__ = 'Administrator'
import random
import xlrd
import xlwt3
import string

#第一题
seq_1 = [
    "赵",
    "钱",
    "孙",
    "李",
    "周",
    "吴",
    "郑",
    "王",
    "黄",
    "沈"
]

seq_2 = [
    "浩",
    "依",
    "学",
    "从",
    "武",
    "灵",
    "飞",
    "大",
    "狗",
    "胖"
]

wb = xlwt3.Workbook()
sheet = wb.add_sheet("名册")

sheet.write(0, 0, "name")
sheet.write(0, 1, "sex")
wNum = 1

for i in range(0, 100):
    name = random.choice(seq_1) + "".join(random.sample(seq_2, i % 2 + 1))
    sheet.write(wNum, 0, name)
    wNum += 1

for i in range(0, 100):
    sheet.write(i + 1, 1, random.choice("12"))

wb.save("G:\\yuangungun.xls")

#第二题
workbook = xlrd.open_workbook("G:\\yuangungun.xls")
sheet_obj = workbook.sheet_by_index(0)

rowNum = sheet_obj.nrows
menNum = 0

for i in range(1, rowNum):
    if sheet_obj.cell_value(i, 1) == "1":
        menNum += 1

print("该表单男生有%s人，女生有%s人"%(menNum, rowNum - menNum - 1))