
class Students:

    school_name = "ABC School" #class variable

    def __init__(self,name):
        self.name = name        #instance variable

s1 = Students("Rahul")

s2 = Students("Anita")

print(s1.school_name)
print(s2.school_name)

print(Students.school_name)
        