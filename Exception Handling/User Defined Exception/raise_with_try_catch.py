
try:
    x = int(input("Enter a number :"))
    if x == 0:
        raise ZeroDivisionError("zero is not allowed here")
except ZeroDivisionError as e:
    print(e)