# 웹 스크래핑 : 웹 페이지에서 원하는 데이터를 추출하는 기술 - html을 분석 BeautifulSoup 모듈
# [유사용어 : 웹 크롤링 - 여러 웹페이지를 돌아다니면서 데이터를 긁어모으는 기술 - selenium]

#0. beautifulsoup 모듈 설치
# pip install beautifulsoup4

#1. 모듈 사용
import requests
from bs4 import BeautifulSoup

#2. HTML 웹페이지를 읽어오기
response= requests.get('https://mbca2026aix.dothome.co.kr')  # index.html
print(response.text)
print()

# html 분석하기 위해 BeautifulSoup 객체를 생성하며 데이터를 전달
soup= BeautifulSoup(response.text, 'html.parser')  # 파서(분석가) 선택

# 분석 시작.  특정 요소를 찾아서 글씨나 속성값을 추출!
# [1] 요소 선택자를 이용하여 찾기 (CSS언어의 선택자 문법 사용)
ps= soup.select('p')  #p요소 모두 찾기
for p in ps:
    print('p요소의 글씨:', p.string)
print()

#[2] 아이디 선택자로 요소 1개 찾기
img= soup.select_one('#aa')
print('이미지 경로:', img.get('src'))
print()
print("="*100)
print()

# 네이버 코스피 지수 데이터 HTML 파싱하여 얻어오기
# 다만, 네이버 페이지는 robots.txt, 이용약관상 스크래핑, 크롤링을 모두 금지하고 있음. 학습목적으로 잠깐 해보는 정도....
response2= requests.get('https://finance.naver.com/')
#print(response2.text)
soup= BeautifulSoup(response2.text, 'html.parser')

# 코스피 지수값을 보여주는 요소를 찾아서 값을 출력해보기
span_element= soup.select_one('#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span > span.num')
print(span_element)
print('현재 코스피 지수:',span_element.string)




