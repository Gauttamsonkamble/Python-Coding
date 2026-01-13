
# x = 10 / 0

# print(x)

# try:
#     a = int(input("Enter a number : "))
#     print(10/a)
# # except ZeroDivisionError:
# #     print("You can not divide by zero")
# # except ValueError:
# #     print("Enter correct input")
# except:
#     print("Something is wrong")
# try:
#     x = 10 / 2
# except ZeroDivisionError:
#     print("Error accured")
# else:
#     print("Result is : ",x)

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error accured")
finally:
    print("Program finished")
