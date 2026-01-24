
class parent:
    def house(self):
        print("parent owns the house")

class Child(parent):
    def car(self):
        print("Child owns the car")

c = Child()

c.house()
c.car()