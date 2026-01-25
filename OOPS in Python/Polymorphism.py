
class Animal:
    def sound(self):
        print("Animal Makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog Sounds Bark")

class Cat(Animal):
    def sound(self):
        print("Cat sound is meow")

d = Dog()
c = Cat()

d.sound()
c.sound()