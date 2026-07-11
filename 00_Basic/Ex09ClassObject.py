#클래스와 객체

#클래스 : 연관있는 변수와 기능을 묶어놓은 설계도
#객체 : class 설계도를 기반으로 실제 메모리에 만들어진 제품

# 즉, 제품을 만들어야 기능을 사용하듯이.. 클래스를 객체로 만들어야 동작함.

#1. 클래스 선언
class Person:
    #멤버 변수(생성자 함수 안에서 만들어야 함)
    def __init__(self, name='익명', age=0, address='연고지 없음'):  #python constructor.. (객체를 생성할때 실행됨)
        self.name=name
        self.age=age
        self.address=address        

    #멤버 함수(클래스 안의 모든 함수는 무조건 self가 파라미터로 있어야 함)
    def show(self):
        print('name:',self.name)
        print('age:',self.age)
        print('address:',self.address)


#클래스를 설계했다고 뭐가 실행되진 않음. 객체를 생성해서 멤버를 사용
p= Person('sam',20,'seoul')  #객체 생성하면서 멤버값들 전달
p.show()

# 같은 모양으로 객체 또 생성 가능
p2= Person('robin',25,'busan')
p2.show()

#객체 생성할때 값을 주지 않으면??
p3= Person()  #error -- 안나게 하려면.. 생성자의 파라미터에 defalt value 지정해놓기
p3.show()


#3. 상속 (다른 클래스 설계도면을 그대로 가져와서 새로운 멤버만 추가)
# [이름, 나이, 주소, 전공] -- Person에 이미 [이름, 나이, 주소]가 있음.
class Student(Person):
    def __init__(self, name, age, address, major):
        # [이름, 나이, 주소]는 부모생성자에게 전달
        super().__init__(name,age,address)
        # [전공]만 새로 만들기
        self.major=major

    def show(self):
        #이름, 나이, 주소는 부모가 대신 출력
        super().show()
        #내가 만든 전공만 직접출력
        print('major:', self.major)

stu= Student('hong',26,'incheon','AI solution')
stu.show()




