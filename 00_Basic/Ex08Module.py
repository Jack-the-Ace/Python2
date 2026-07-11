# 모듈: 특정 기능을 모아놓은 폴더/파일 라이브러리

#1. 표준모듈 : 파이썬에 기본으로 내장되어있는 모듈. 별도의 다운로드 설치 필요없음. [표준함수와 다르게 기능을 사용하려면 import 필요]
#2. 외부모듈 : 별도의 다운로드 설치 필요(pip install xxxx)

#표준함수 중 많이 사용되는 모듈 몇가지
#1) math 모듈 : 수학적 연산기능 모듈
import math
print(math.cos(1))  #cosine 함수
print(math.floor(3.7)) #소수점 내리기 [바닥]
print(math.ceil(3.2)) #소수점 올림 [천장]
#반올림은 표주ㅠㅜㄴ함수 round() 사용

#모듈명을 매번 풀네임으로 쓰기 짜증
import math as m
print(m.pow(4,2))  #4의 2제곱

#모듈 안에서 자주 사용하는 함수를 더 간단히 사용하기 위해...
from math import floor, cos, pow
print(floor(3.8))
print()

#2. random 모듈 : 랜덤값을 만들어주는기능모듈
import random

print( random.random())  # 0.0 ~ 0.9999999999999....
print( random.randrange(10)) # 0~9
print( random.randrange(5,16)) # 5~15

# 리스트의 값 중에 1개를 랜덤하게 뽑기
aaa=[10,20,30,40,50]
print(random.choice(aaa)) # 1개 선택
print(random.sample(aaa,3)) #3개 선택

# 로또번호 추천
lotto= list(range(1,46)) #range로 만든 1~45를 리스트로...
print(lotto)

#번호 6개 추출
for n in range(5):
    nums=random.sample(lotto,6)
    nums.sort()
    print('당첨예상번호:',nums)
print()

#3. os 모듈 : 운영체제와 관련된 기능 모듈 (파일경로에 많이 사용)
import os
print('현재 운영체제:', os.name)
print('현재 작업폴더:', os.getcwd())
print('현재 폴더목록:', os.listdir())

#폴더 만들기
#os.mkdir('image') # 이 폴더가 이미 있으면 에러!!
if not os.path.isdir('image'):  # image 폴더가 없으면 만들어
    os.mkdir('image')

# 폴더 삭제
if os.path.isdir('image'):
    os.rmdir('image')

#4. datetime 모듈: 날짜와 시간 모듈
import datetime

#현재날짜와 시간 얻어오기
now= datetime.datetime.now()
print(now)
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

#특정 날짜로 변경하기
future=now.replace(year=(now.year+1))
print(future)
print()

#5. urllib 모듈 : 네트워크 작업 관련 모듈
from urllib import request  # urllib 모듈의 하위모듈 request를 import

url=request.urlopen('https://jack.dothome.co.kr')
data= url.read()
print(data)
print('='*100)
print(data.decode('UTF-8'))
print('+'*100)

############################################################################################
# 외부모듈 사용 : pip install 로 설치...

#1) requests - 네트워크작업을 urllib 보다 편하게.. 해주는 모듈
import requests
response=requests.get('https://jack.dothome.co.kr')
print(response.text)  # utf-8로 자동 디코딩

#2) Beautiful Soup 모듈 : HTML 문서를 분석(파싱)해주는 모듈 -- 웹 스크래핑할때 필수
# pip install beautifulsoup4
from bs4 import BeautifulSoup
soup= BeautifulSoup(response.text, "html.parser") #파싱할 html글씨, 파서 지정

#id가 "aa"인 요소를 선택하여 src속성값을 추출
img= soup.select_one('#aa') #css선택자
print(img['src'])
print()

#p요소들 모두 선택하여 글씨 추출
for p in soup.select('p'):
    print(p.string)


