# 함수  - 코드가 써있는 영역..   함수 호출을 통해 코드가 실행되도록..

#. 함수 정의
def show():
    print('show function')
    print('aaa')

# 함수 호출
show()
show()

#. 파라미터를 전달받는 함수
def output(a,b):
    print('a:',a)
    print('b:',b)

output(10,20)
# output(100)   error
# output(10,20,30)  error

# 혹시 같은 이름의 함수를 또 정의하면.. 이전 함수는 없어짐(JS와는 다르게 위의 코드까지는 이전 함수 동작함)
def output():
    print('이건 새로만든 output function')

output()
# output(10,20)  error

# 파라미터에 default value 지정 가능
def display(a=1,b=2):
    print('a:',a)
    print('b:',b)

display(100,200)
display(100)
display()
display(b=200)

#. 리턴을 해주는 함수
def sum(a,b):
    return a+b

num= sum(5,3)
print(num)

#return은 함수영역의 실행을 멈추고 돌아가라는 키워드
def aaa():
    print('aaa function')
    return    # 이 뒤로 함수영역에 써있는 글씨는 실행안됨.
    print('aaaaaaaaaaaaaaaaa')

aaa()
#return 할때 값을 주지 않았는데... 혹시 대입받으면?? 뭐가올까요? 안옴.. 안오면 None
m=aaa()
print(m)

# return에 값을 여러개 할 수 없지만.. 만약 여러개를 쓰면.. 자동으로 튜플묶어서 리턴함
def bbb():
    return 100,200,300

n1, n2, n3= bbb()
print(n1,n2,n3)

# 람다 lambda 함수. -- 함수코드의 간단표현 [JS의 화살표함수와 비슷]
#1) 간단한 함수
def eee(n):
    return n*10
num=eee(3)
print(num)

#2) 람다함수
eee=lambda n:n*10
num=eee(4)
print(num)




