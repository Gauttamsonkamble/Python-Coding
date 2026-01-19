
class AgeNotValidException(Exception):
    pass

age = int(input("Enter age : "))
if age < 18:
    raise AgeNotValidException("Age must be 18 or above")
else:
    print("You are eligible")
