
def My_Decorators(func):
    def wrapper():
        print("before function Execution")
        func()
        print("After function execution")
    return wrapper

@My_Decorators
def say_hello():
    print("Hello Python")

# say_hello = My_Decorators(say_hello)

say_hello()

