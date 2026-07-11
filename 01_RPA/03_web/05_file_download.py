# 웹페이지에 있는 미디어 파일을 내 컴퓨터로 다운로드 자동화

# 2가지 경우에 따라 이미지 다운로드 방식이 다름
#case1. <a>요소의 속성 중에 download 속성이 있는 경우는 링크를 클릭하면 다운로드
#case2. <img>요소로 이미지를 보여주는 경우. src 속성값을 통해 파일을 다운로드 해야 함.

#[case1] <a>요소에 download 속성이 있는 경우 [연습용 웹페이지 download_link.html]
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options= Options()
options.add_experimental_option('detach',True)
#기본 다운로드 경로를 지정하고 싶다면...
options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\mbc\MBCA\Python2\01_RPA\03_web\image'})

chrome=webdriver.Chrome(options=options)

#다운로드 링크가 있는 웹페이지 열기
chrome.get('http://127.0.0.1:5500/03_web/download_link.html') # Live server url
time.sleep(1)

#다운로드 링크 요소를 찾아서 클릭! ... 하면 자동 다운로드
anchor_element= chrome.find_element(By.XPATH, '/html/body/a[2]')
anchor_element.click()
time.sleep(1)

#---------------------------------------------------------------------------------------------------------------

#[case2] img 요소로 보여주는 이미지파일을 다운로드 하기!
chrome.get('https://m.etnews.com/')  #[전자신문 사이트] 열기
chrome.maximize_window()
time.sleep(2)

# 헤드라인 뉴스 이미지를 가진 요소 찾기
img_element= chrome.find_element(By.XPATH, '/html/body/main/section[1]/div/figure/a/img')

# 이미지 요소의 src 속성값을 가져오기
img_url= img_element.get_attribute('src')

# 이미지 URL의 파일을 다운로드 하기! - 표준 모듈로.. urllib
from urllib import request
if img_url:
    request.urlretrieve(img_url, filename='./03_web/image/download_image.jpg')
else:
    print('이미지 URL을 찾을 수가 없습니다.')    

