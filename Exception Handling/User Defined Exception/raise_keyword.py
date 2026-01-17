
# age = -5

age = int(input("Enter age : "))

if age < 0:
    raise ValueError("Age can not be negative")