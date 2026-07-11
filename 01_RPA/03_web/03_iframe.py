# 페이지 안에 다른 페이지가 있는 경우.. 그 안의 요소 찾아 제어
# iframe

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options= Options()
options.add_experimental_option('detach',True)
chrome= webdriver.Chrome(options)

# iframe을 가진 웹 페이지 열기
chrome.get('https://www.w3schools.com/TAgs/tryit.asp?filename=tryhtml5_input_type_radio')
time.sleep(2)

# 웹화면에 바로 보이는 radio 요소찾아보기 시도...
# e= chrome.find_element(By.XPATH, '//*[@id="html"]')
# e.click() -- error

# iframe 안에 있는 요소는 바로 찾아지지 않아요...
# iframe 으로 현재 셀레니움의 관찰위치를 이동
chrome.switch_to.frame('iframeResult') # frame의 id로 이동
print('프레임 이동 성공')  #화면에는 변화 없음.

# iframe 안에 있는 요소를 찾기
e= chrome.find_element(By.XPATH, '//*[@id="html"]')
e.click() 

time.sleep(2)

# 원래 html 페이지로 다시 복구
chrome.switch_to.default_content()
print('원래 위치로 이동')
time.sleep(2)

#원래 위치의 요소를 찾아서 클릭 해보기 (회전 버튼)
e= chrome.find_element(By.XPATH, '/html/body/div[2]/div/a[4]')
e.click()
time.sleep(1)
e.click()
