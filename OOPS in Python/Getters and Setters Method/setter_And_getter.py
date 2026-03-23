
class Student:
    def __init__(self,age):
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if ( value > 0):
            self.__age = value
        else:
            print("Age must be positive..!")

s = Student(20)

print(s.age) #getter

s.age = 25


print(s.age)