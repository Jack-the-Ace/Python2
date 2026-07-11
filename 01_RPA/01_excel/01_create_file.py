# 엑셀 사용을 위한 외부모듈 설치 openpyxl

# 0. pip install openpyxl

# 1. 엑셀파일 객체를 Workbook 클래스를 통해 만들 수 있음.
from openpyxl import Workbook

# 2. 워크북 객체 생성
wb= Workbook()
# 3. 워크북 안에 현재 활성화된 워크시트 참조(default sheet 이름 'Sheet1')
sheet= wb.active

# 4. 워크북 객체를 엑셀 파일로 저장
wb.save('./01_excel/sample.xlsx')

# 5. 워크북 닫기
wb.close()