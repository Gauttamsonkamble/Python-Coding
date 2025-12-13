
day = int(input("Enter day Number : "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednsday")
    case _:
        print("Invalid Number")