
class AgeNotValidException(Exception):
    pass

try:
    age = int(input("Enter age : "))

    if age < 18:
        raise AgeNotValidException("Age must be 18 or above")
    print("you are eligible")

except AgeNotValidException as e:
    print("Custom Exception : ",e)