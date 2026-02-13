
class Bank:
    def __init__(self,balance):
        self.__balance = balance

    def showBalance(self):
        print("Balance : ",self.__balance)

b = Bank(50000)

# print(b.__balance) # not accessible

b.showBalance()

        