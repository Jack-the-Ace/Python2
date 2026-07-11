import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option('detach',True)
chrome=webdriver.Chrome(options=options)

chrome.maximize_window()

chrome.get('https://www.w3schools.com/')
time.sleep(0.5)

chrome.execute_script('window.scrollTo({top:700, behavior: "smooth"});')
time.sleep(1)

e= chrome.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]')
e.click()
time.sleep(0.5)

e= chrome.find_element(By.XPATH, '//*[@id="subtopnav"]/a[12]')
e.click()
time.sleep(0.5)

chrome.execute_script('window.scrollTo({top:700, behavior:"smooth"});')

e= chrome.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[120]')
e.click()
time.sleep(0.5)

e= chrome.find_element(By.XPATH, '//*[@id="fname"]')
from selenium.webdriver.common.keys import Keys

input1= chrome.find_element(by=By.CSS_SELECTOR, value='#fname')
input1.send_keys('홍')
time.sleep(0.5)
input1.send_keys(Keys.TAB)

input2=chrome.find_element(by=By.CSS_SELECTOR, value='#lname')
input2.send_keys('길동')
time.sleep(1)
chrome.execute_script('window.scrollTo({top:500, behavior:"smooth"});')
time.sleep(1)
input2.send_keys(Keys.TAB)

input3=chrome.find_element(by=By.CSS_SELECTOR, value='#country')
input3.send_keys('USA')
time.sleep(0.5)
input3.send_keys(Keys.TAB)

input4=chrome.find_element(by=By.CSS_SELECTOR, value='#main > div.test > textarea')
input4.send_keys('자동화 수행 완료~!!')
time.sleep(2)
input4.send_keys(Keys.TAB)

input5=chrome.find_element(by=By.CSS_SELECTOR, value='#main > div.test > a')
input5.send_keys(Keys.ENTER)
time.sleep(2)

#---------------------------------------
chrome.quit()