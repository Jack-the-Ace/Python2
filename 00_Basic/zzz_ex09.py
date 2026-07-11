class Person:
    def __init__(self, name=" - ", age=0, address=" - "):
        self.name=name
        self.age=age
        self.address=address
    def show(self):
        print('Name:',self.name)
        print('Age:', self. age)
        print('Address',self.address)
p=Person()
p.show()