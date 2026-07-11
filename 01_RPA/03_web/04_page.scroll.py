# 웹 페이지 스크롤 제어

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#1. chrome 드라이버 생성
options= Options()
options.add_experimental_option('detach',True)
chrome= webdriver.Chrome(options=options)

#2. 브라우저 최대화
chrome.maximize_window()

#3. 쇼핑몰 페이지에 접근 시도. [대부분의 쇼핑몰이 자동화 기능을 막아놓았음... 인증페이지로 리다이렉트됨]
#chrome.get('https://shopping.naver.com/')
#뉴스
chrome.get('https://news.naver.com/')
time.sleep(2)

#4. 페이지 스크롤 - selenium에는 이 기능이 없음, 대신 웹페이지의 JS를 실행시킬 수 있음
chrome.execute_script('window.scrollTo(0, 500)')  # pixel
time.sleep(2)

#5. 페이지의 가장 마지막 위치로 스크롤
chrome.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(2)

