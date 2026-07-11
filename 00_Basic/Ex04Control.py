# 제어문

#1. 조건문 if, if else, if elif -- JS와 다르게 {}사용하지 않고 : 과 들여쓰기로 영역구분
age=25
if(age<20):
    print('미성년')
print('여기는 if문과 상관없이 출력')

#if-else
age=28
if(age<20):
    print('꺼져!')
else:
    print('환영합니다. 문나이트 입니다.')

# if-elif
score=75
if(90<=score<=100):
    print('A학점')
    print('참 잘했어요!')
elif(score>=80):
    print('B학점')
    print('잘했어요.')
elif(score>=70):
    print('C학점')
    print('준수하네요..')
elif(score>=60):
    print('D학점')
    print('분발하세요..')
else:
    print('F학점')
    print('거 너무한거 아녀!!')

# 특이한 키워드 pass -- 개발중에 ... 잠시 미완성일때 사용
a= 100
if(a<100):
    print('aaa')
elif(a<200):
    pass
elif(a<300):
    pass
# 먼저 구조를 만들고 세부내용을 작성할때 유용

# if 조건식의 소괄호()를 생략할 수 있음 (생략하는 사람이 더 많음)
if a<10:
    print('aaa')
elif a<20:
    print('bbb')

print('='*100)

#2. 새로생긴 문법 분기문 match-case [JS의 switch-case와 비슷]
menu=8
match menu:
    case 1:
        print('hello')
    case 2:
        print('nice to meet you')
    case 3|4:  # 3 or 4
        print('how are you, today?')

    case _:  # 와일드 case -- 위 경우 말고 나머지 다...
        print('wrong menu number')
print()

#3. 반복문 while
a=0
while(a<5):
    print('aaa')
    a+=1

level=1
while True:
    print('level: ', level)
    level+=1
    if level>10:
        break  # 반복문 멈추기

# 4. 반복문 for -- 소괄호()를 쓰면 에러 (대량의 데이터를 요소 개수만큼 반복수행)
aaa=[10,20,30,40,50]  # list
for n in aaa:
    print(n)

# 0부터 9까지 숫자를 반복하고 싶다면..
for n in range(10):  # 0~9 까지의 숫자들을 만들어줌
    print(n)

for n in range(5,10): # 5~9까지
    print(n)

for n in range(1,51,2): # 1~50까지 2씩 증가
    print(n)

for n in range(10,0,-1): # 10~1까지 1씩 감소
    print(n)

#기타 제어문 : break, continue
for n in range(1,11):
    if n==5:
        break
    print('n:',n)
print()

for n in range(1,11):
    if n==5:
        continue  # 현재 번째 작업을 더이상 하지 않고 다음 번호로 넘어가기.
    print('n:',n)
