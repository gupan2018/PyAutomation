__author__ = 'Administrator'
#import xlrd
import xlwt3

'''
workbook = xlrd.open_workbook("G:\\Python\\test.xlsx")
print(workbook.sheet_names())

sheet_obj1 = workbook.sheets()[0]

sheet_obj2 = workbook.sheet_by_index(0)

sheet_obj3 = workbook.sheet_by_name("Ti_0.1")

row_num = (sheet_obj2.nrows)
print("该表有%s行"%row_num)

col_num = int(sheet_obj2.ncols)
print("该表有%s列"%col_num)

print(sheet_obj2.row_values(1))

print(sheet_obj2.col_values(1))

print(sheet_obj2.cell_value(1, 1))
'''

wb = xlwt3.Workbook()
sheet = wb.add_sheet("test_sheet", cell_overwrite_ok=True)
sheet.write(0,1, "这是我写入的数据")
wb.save("G:\\test.xls")
