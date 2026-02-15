
class MathOP:
    
    @staticmethod
    def add(a,b):
        return a+b
    
result = MathOP.add(5,3)

print(result)

obj = MathOP()

result2 = obj.add(10,2)

print(result2)