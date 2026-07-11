#변수 : 데이터를 저장하는 작은 공간(문자)

#변수에 담을 데이터의 종류들 마다 명칭이 있음.  이를 자료형 data type 이라고 함
#파이썬의 자료형 종류
#1. 기본 자료형 : int, float, str, bool
#2. 배열 자료형 : list, tuple, dict
#3. None : nothing

#자료형별 데이터의 표기모습 확인
print(10)  #int
print(3.14) #float
print(True) #bool
print('hello') #str
print("Hello") #str
print()

# 변수 선언 : 그냥 변수명과 =대입연산자로 값을 대입하면 됨. (스네이크 표기법 _ 권장)
a= 100
print(a)

b=5.55
print(b)

c=False
print(c)

d= 'sam'
print(d)

e="robin"
print(e)

f= None
print(f)

# 변수 자료형 확인
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print()

# 변수이기에 가지고 있는 값을 바꿀 수 있음. 자료형이 달라도 됨 (동적타입언어 특성)
a='nice'  #int --> str
print(a)
print(type(a))

# 변수는 한번에 1개의 값만 가질 수 있음. 그런데 여러개를 대입해도 에러 안남
a=100, 200
print(a)
print(type(a)) #int가 아니라.. tuple 타입임. 즉, 변수는 tuple 1개를 가진 것임
print(a[0])
print(a[1])

# 여러개의 변수에 여러개의 값을 한번에 대입가능
a,b= 100,200  # 실제로는 튜플의 구조분해할당
print(a, type(a))
print(b, type(b))

#당연히 대입 양쪽의 개수가 같아야 함.
#a,b= 100 -- error
#a,b= 100,200,300 -- errror

#문자열 타입 데이터만의 연산자 3개 +, *, []
print("aa"+"bb") #산술연산이 아니라.. 결합연산
print("Hello"*3) #반복 연산자 - "Hello"를 3번 붙이기
s="Good"*5
print(s)

#문자열 인덱싱/슬라이싱 연산자 []
print( "Hello world"[1] ) #1번 인덱스 위치의 한글자 추출 - 'e'
print( "Hello world"[1:7] ) #1번 인덱스 부터 7번 전까지 위치의 글자 추출 - 'ello w'
print( "Hello world"[1:] ) #1번 인덱스 부터 끝까지 위치의 글자 추출 - 'ello world'
print( "Hello world"[:7] ) #처음부터 7번 전까지 위치의 글자 추출 - 'Hello w'
print( "Hello world"[-1] ) #뒤에서 첫번째 인덱스 한글자 추출 - 'd'
print( "Hello world"[-5] ) #뒤에서 5번째 인덱스 한글자 추출 - 'w'
print( "Hello world"[:-1] ) #마지막 요소만 빼고 모두 추출 - 'Hello worl'

# 문자열의 글자수를 확인
s= 'machine learning'
print(len(s))

# 문자열데이터는 가장 많이 사용하는 데이터 유형
# 그래서 문자열이 가진 주요 기능함수들 확인
print("{}만원".format(5000))
print("Hello".upper())
print("Hello".lower())
print("    Hello world    ".strip()) #양쪽공백제거
print("Hello world. android. ios. web".find('ios')) #찾은 글자의 첫번째 자리 인덱스 번호
print("Hello world. android. ios. web".find('mac')) #없으면 -1

#csv 데이터에서, 기준으로 글씨를 분리시키기
csv= "sam,20,seoul"
values=csv.split(',')
print(type(values)) #리스트
print(values[0],type(values[0]))
print(values[1],type(values[1]))
print(values[2],type(values[2]))

# 특정 글자가 포함되어있는지 여부 (True/False)
print("sam" in csv)
print("robin" in csv)

# 문자열 데이터를 만들때 3따옴표.. ''',"""
print('''
이 안에 쓰면.
써있는 고대로.. 줄바꿈도 가능
      ㅇㅇ
''')
# 위 3따옴표는 함수의 doc string 에 활용하는 경우가 많음. (doc string: 함수를 설명하는 글씨 -- AI가 이 글씨를 확인하여 답변에 활용할 수 있음.)
# AI에게 제공하는 프롬프트를 자세히 길게 쓸 때 많이 활용
promt="데이터 분석해줘."
promt_eng='''
[역할]
너는 전문 데이터 분석가야.

[제한사항]
초등학생도 이해하게 분석결과를 알려줘.
'''

# 3.5 버전 이상에서 새로 등장한 자료형 힌트
score:int= 10  #score 변수가 int형을 가지도록 만들었다고 표식!!

def aaa(message:str):
    print(message)
