# 셀병합

from openpyxl import Workbook
wb=Workbook()
sheet=wb.active

sheet.merge_cells('B2:D2')
sheet['B2'].value='Hello python excel'

wb.save('./01_excel/sample6.xlsx')
wb.close()