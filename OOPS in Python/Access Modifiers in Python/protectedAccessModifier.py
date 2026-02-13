
class Person:
    def __init__(self,age):
        self._age = age  # protected Variable

class Employee(Person):
    def show(self):
        print("Age : ",self._age)

e = Employee(30)

e.show()
print(e._age)
        