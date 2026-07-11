from openpyxl import load_workbook
wb= load_workbook('./01_excel/sample4.xlsx')
sheet= wb.active

# 특정 범위의 cell 을 잡아서 이동
sheet.move_range('B1:C11', rows=0, cols=1)  #줄은 0줄 이동.. 칸으로 1칸 이동

sheet['B1'].value='수학'

wb.save('./01_excel/sample4_move.xlsx')
wb.close()