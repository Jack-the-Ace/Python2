# selenium : 사용자가 브라우저에서 수행하는 행동을 파이썬 코드가 대신 움직이도록 해주는 모듈
# 웹 크롤러 or RPA 자동화 서비스 개발에 많이 활용됨.

# 설치 : pip install selenium
# 셀레니움으로 웹브라우저를 제어할때 버전에 따라.. 각 브라우저의 웹드라이버를 설치해야 할 수도 있음. [현재 셀레니움 버전에서는 추가설치 안해도 됨]

#자동화 웹브라우저가 종료되지 않도록... 옵션생성
from selenium.webdriver.chrome.options import Options
options= Options()
options.add_experimental_option('detach',True)

#1. 기본 셀레니움으로 특정 웹페이지를 열기
from selenium import webdriver
chrome= webdriver.Chrome(options)   # 기본적으로 자동화 웹브라우저는 코드를 모두 실행한 후 자동 종료됨. 옵션으로 계속 유지되도록..
chrome.get('https://www.naver.com')

import time
time.sleep(3)

# 웹 크롤링... 웹페이지를 돌아다니면서 데이터를 긁어오는 기술
# 페이지 변경 -- 웹페이지(html)에서 데이터를 추출하는 것도 살짝 다뤄보기 위해..
# 우선 간단한 .html 페이지를 만들어서 실습

# 내가 만든 웹페이지의 절대경로(전체경로) 만들기
import os
print(os.getcwd()) #현재 작업 위치.. 확인

# index.html 의 절대경로 만들기
chrome.get(os.path.join(os.getcwd(), "./03_web/index.html"))
time.sleep(2)

###### 셀레니움을 이용하여 웹페이지 안에서 데이터를 수집하기!!!! #######
from selenium.webdriver.common.by import By

#1) 아이디로 요소 찾기
p1= chrome.find_element(By.ID, 'p1')
print(p1)   # 요소가 출력됨
print(p1.text)

#2) 클래스명으로 요소들 찾기
es= chrome.find_elements(By.CLASS_NAME, value='aaa')
print(len(es))  #1
print(es[0].tag_name) #div

#3) 태그 이름
es= chrome.find_elements(By.TAG_NAME, value='h2')
for e in es:
    print(e.text)  # TITLE, 파이썬......

#4) CSS 선택자로 찾기
es= chrome.find_elements(By.CSS_SELECTOR, 'ul.sss > li > a')
for e in es:
    print(e.text)  # 네이버, 구글, 다음

#5) xPath  ----  요소를 쉽게 찾기 위한 경로..
e= chrome.find_element(By.XPATH, "/html/body/div/p/strong")
print(e.text)

#6) 링크 텍스트로 찾기
e= chrome.find_element(By.LINK_TEXT, "네이버")
print(e.get_attribute('href'))  # 속성값 취득

#7) imput 요소에 글씨 입력하기
e= chrome.find_element(By.NAME, 'title')
e.send_keys('자동화 글씨 입력')  # 키보드 값을 보낸다...
print(e.get_attribute('value'))

# 선택한 요소를 제어하기(클릭하기)
time.sleep(2)
e= chrome.find_element(By.LINK_TEXT,"구글")
e.click()

time.sleep(2)
chrome.back()

time.sleep(2)
chrome.forward()

time.sleep(2)
chrome.refresh()
