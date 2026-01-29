
class Parent:
    def show(self):
        print("This is Parent class method")

class Child(Parent):
    def show(self):
        print("This is child class method")

c = Child()

c.show()