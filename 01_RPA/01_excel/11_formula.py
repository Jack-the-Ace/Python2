#셀에 수식[formula] 적용하기
from openpyxl import Workbook
wb= Workbook()
sheet= wb.active

sheet['A1']= '=SUM(10,20,30)'  #3개의 값을 덧셈
sheet['A2']= '=AVERAGE(10,20,30)' #3개 값의 평균

# 범위 연산도 가능
sheet['A3']=100
sheet['A4']=200
sheet['A5']=300
sheet['A6']='=sum(A3:A5)'

wb.save('./01_excel/sample5.xlsx')
wb.close()