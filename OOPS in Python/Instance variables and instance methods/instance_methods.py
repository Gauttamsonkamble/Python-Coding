
class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self): #instance methods
        print(f"Students : {self.name}")
        print(f"Marks : {self.marks}")

    
    def update_marks(self,updated_marks): #instance methods 
        self.marks = updated_marks

s1 = Students("Kiran",85)

s1.display()

s1.update_marks(92)
s1.display()