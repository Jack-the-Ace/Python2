from openpyxl import load_workbook

wb= load_workbook('./01_excel/sample4.xlsx')
sheet= wb.active

# 한줄 삽입 - append()는 무조건 마지막 줄에 추가됨
sheet.insert_rows(8)  # 8번 줄에 새로운 한 줄이 삽입됨

# 여러 줄 삽입
sheet.insert_rows(10, 5) #10번 줄 위치에 5줄 삽입[빈 5줄]

# 한칸, 여러칸 삽입
sheet.insert_cols(2)  # 2번칸 삽입
sheet.insert_cols(4,3) # 4번칸 위치에 3칸 삽입

wb.save('./01_excel/sample4_insert.xlsx')
wb.close()