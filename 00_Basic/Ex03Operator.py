# 연산자

#1. 산술연산자
a=10
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a%b)  #나머지 연산자 - 나눗셈의 나머지값
print(a//b) #나눗셈의 몫
# 몫과 나머지를 한번에 구해주는 함수
x,y = divmod(10+2,3.4)
print(x)
print(y)

print(b**2) #제곱
print(b**3) #세제곱
print(b**(1/2)) #제곱근 - 루트
print('='*100)

#2. 비교 연산자
print(a>b)  #True
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b) 

# 파이썬은 사람의 계산처럼 비교연산자를 연결하여 가용 가능(범위비교 가능)
age=25
print(20<age<30)
print('='*100)

#3. 논리 연산자 (비교연산에 사용할 변수가 여러개일때.. 즉, 조건이 여러개)
age=9
height=130
print(age>10 and height>120)  # 나이가 10살초과 이고, 키는 120 초과 (두 조건 모두 맞아야 True)
print(age>10 or height>120)  # 나이가 10살초과 이거나, 키가 120 초과 (둘 중에 하나만 맞으면 True)

# 성인이 아닌가?
print(not age>=20)
print('='*100)

#4. 비트연산자 (숫자를 2진수로 만들고 각 진수의 자리끼리 논리연산 수행)
print(7&4)
#   111
# & 100
#-------
#   100 --> 4

print(5|2)
#   101
# | 010
#-------
#   111 --> 7
print("="*100)

# JS에 있던 증감연산자 ++, -- 는 파이썬에 없음

#6. 복합대입연산자 : =와 산술연산자를 같이 사용하는 축약연산자
a=10
# a의 값에 3을 추가하기
a=a+3
print(a) #13

# a변수명을 두번 쓰기 짜증
a += 3
print(a) #16

a -= 2
print(a) #14
a *= 2
print(a) #28
a /= 7
print(a) #4

#7. 삼항연산자 - JS의 ?: 는 아님. 표기법은 if와 else
b= 'A' if(a>10) else 'B'
print(b)

#8. 형변환 연산자
a='10'
# print(a+20) #error
print(int(a)+20) #str --> int

a='3.14'
print(float(a)+5.12)

print(3+5)  #산술연산
print(str(3)+str(5)) #결합연산
