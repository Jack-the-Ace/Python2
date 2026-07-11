from openpyxl import load_workbook
wb= load_workbook('./01_excel/Scores.xlsx')
sheet= wb.active
#-------------------------------------------------------------------------------
for d in range(2,12):
    sheet[f'D{d}'].value= 10

sheet['H1'].value='총점'
sheet['I1'].value='성적정보'

for total in range(2,12):
    sheet[f'H{total}'].value= sum(cell.value for cell in sheet[f'B{total}:G{total}'][0])

for info in range(2,12):
    if sheet[f'H{info}'].value >=90:
        sheet[f'I{info}']= 'A'
    elif sheet[f'H{info}'].value >=80:
        sheet[f'I{info}']='B'
    elif sheet[f'H{info}'].value >=70:
        sheet[f'I{info}']='C'
    else:
        sheet[f'I{info}']='D'

for absc in range(2,12):
    if int(sheet[f'B{absc}'].value)<5:
        sheet[f'I{absc}']='F'



#-------------------------------------------------------------------------------
wb.save('./01_excel/Scores.xlsx')
wb.close()