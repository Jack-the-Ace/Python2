# handle : 브라우저의 창(tab)마다 다른 handle값(일종의 식별자)을 가지고 제어 가능

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options= Options()
options.add_experimental_option('detach',True)
chrome=webdriver.Chrome(options=options)

chrome.get('https://www.w3schools.com/TAgs/att_input_type_radio.asp')
print(chrome.title)

# 현재 핸들값 확인가능
current_handle= chrome.current_window_handle
print(current_handle)
time.sleep(1)

#[Try it Yourself] 요소를 클릭하여 새 탭이 만들어짐
chrome.find_element(By.XPATH, '//*[@id="main"]/div[2]/a').click()
time.sleep(1)

# 새 탭이 생겼으니 핸들이 여러개..
handles= chrome.window_handles
for handle in handles:
    chrome.switch_to.window(handle)
    print(chrome.title)
    time.sleep(1)

#현재 탭 닫기
chrome.close()

chrome.switch_to.window(current_handle)  # 처음에 저장했던 핸들.. 메인페이지
print(chrome.title)