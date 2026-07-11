from openpyxl import Workbook
wb= Workbook()
sheet= wb.active

#엑셀파일에 이미지를 그리려면.. jpg를 파이썬에서 다룰 수 있는 이미지로드 외부모듈 필요 -- pillow
from openpyxl.drawing.image import Image
img= Image('./01_excel/paris.jpg')

sheet.add_image(img, 'C3')

img.width=100
img.height=100

#엑셀기본눈금선 안보이도록
sheet.sheet_view.showGridLines=False

wb.save('./01_excel/sample7.xlsx')