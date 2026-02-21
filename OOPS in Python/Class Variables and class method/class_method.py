
class Students:
    school_name = "ABC School" # class Variable

    def __init__(self,name):
        self.name = name

    @classmethod
    def change_schoolName(cls,newName):
        cls.school_name = newName

Students.change_schoolName("XYZ School")
print(Students.school_name)
        