# 인터렉티브 쉘과 다르게.. 값만 쓰면 출력되지 않음.
100

# 화면출력 기능함수 print()
print(10)
print(3.14)
print(True)
print('hello')

#줄바꿈 안하고 싶다면..
print(100,end=', ')
print(200)

#연산식을 출력하면.. 결과가 출력됨
print(3+5)
print('3+5')

# 변수를 만들고 변ㅅ이름을 출력하면 그 안의 값이 출력됨
a=1000
print(a)
print('a')

# 다른 자료형과 덧셈 연산
print(3+3.14)
print("aa"+"bb") #결합
#print("aa"+3)  # error
#숫자를 문자로 변환
print("aa"+str(3)) #형변환 연산자
print("a 변수의 값 : "+str(a))

# 매번 형변환 하면서 덧셈하기 짜증.. 문자열의 format()기능으로 특정위치에 값이 전달되도록
print("{}입니다.".format(1000))
print("{} + {} = {}".format(10,20,10+20))

#{}와 데이터가 서로 멀리 있어서.. 보기가 조금 불편... f-string
print(f"{a} x {20} = {a*20}")

# 여러개의 데이터 출력기능
print(10,20,30,40) # 띄어쓰기로 구분되어 출력됨
print("sam", 20, True)
print(10, "+", 20, "=", 10+20)