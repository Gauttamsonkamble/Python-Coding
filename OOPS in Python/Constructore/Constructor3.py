
class Employee:
    def __init__(self,empid,sal):
        self.empid = empid
        self.sal = sal

e1 = Employee(101,50000)
e2 = Employee(102,60000)

print(e1.empid,e1.sal)

print(e2.empid,e2.sal)
