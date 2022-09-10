import openpyxl
import os

os.chdir('/Users/julia/dev')

workbook = openpyxl.load_workbook('example.xlsx')
print(workbook.get_sheet_names())
type(workbook)

sheet = workbook.get_sheet_by_name('Sheet1')
