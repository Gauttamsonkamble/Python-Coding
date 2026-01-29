
class Animal:
    def sound(self):
        print("Animal Make sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog sound in Bark")

d = Dog()
d.sound()