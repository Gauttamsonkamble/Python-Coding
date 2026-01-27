
class students:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = students("Gauttam",25)
s2 = students("Rahul",26)

s1.display()
s2.display()
        