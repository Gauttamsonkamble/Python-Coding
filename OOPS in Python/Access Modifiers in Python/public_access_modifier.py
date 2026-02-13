
class Students:
    def __init__(self,name):
        self.name = name   #public variable

    def display(self):
        print("Student name : ",self.name)

s = Students("Rahul")

print(s.name)

s.display()


        