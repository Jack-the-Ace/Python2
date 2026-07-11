from openpyxl import load_workbook
wb= load_workbook('./01_excel/sample4.xlsx')
sheet= wb.active

# 한줄삭제
sheet.delete_rows(8)  # 8번 줄에 있는 7번 학생의 데이터 삭제

# 여러줄 삭제
sheet.delete_rows(8,3) # 8번줄 데이터부터 3명의 학생 데이터 삭제

# 칸 삭제
sheet.delete_cols(2)
sheet.delete_cols(1,2)

wb.save('./01_excel/sample4_delete.xlsx')
wb.close()