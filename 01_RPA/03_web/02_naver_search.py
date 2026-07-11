from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_experimental_option('detach',True)

chrome= webdriver.Chrome(options)
chrome.get('https://www.naver.com')

#네이버 검색어 입력창 요소 찾기
search_input= chrome.find_element(by=By.CSS_SELECTOR, value='#query')

#키보드 값 입력
search_input.send_keys('스타벅스')

#요청 후 잠시 딜레이.. [웹브라우저가 너무 빨리 움직이면 robot이라고 판단함.. 차단됨]
import time
time.sleep(4)

# # 입력버튼 클릭
# btn= chrome.find_element(By.CSS_SELECTOR, '#ke_kbd_btn')
# btn.click()

# time.sleep(2)

# # 검색 버튼 클릭
# search_button= chrome.find_element(By.CLASS_NAME, '#_nx_kbd > div > div > div.key_main > div:nth-child(5) > button.key._key.key_search._search')
# search_button.click()

# 키보드 엔터 입력으로..
from selenium.webdriver.common.keys import Keys
search_input.send_keys(Keys.ENTER)

time.sleep(2)

# 검색된 스타벅스 지점 목록 중 앞 2개의 지점명 수집..
store1= chrome.find_element(By.XPATH, '//*[@id="place-main-section-root"]/section/div/div[4]/ul/li[1]/div[1]/div[1]/a/span[1]')
store2= chrome.find_element(By.XPATH, '//*[@id="place-main-section-root"]/section/div/div[4]/ul/li[2]/div[1]/div[1]/a/span[1]')
store3= chrome.find_element(By.XPATH, '//*[@id="place-main-section-root"]/section/div/div[4]/ul/li[3]/div[1]/div[1]/a/span[1]')

print(store1.text)
print(store2.text)
print(store3.text)
