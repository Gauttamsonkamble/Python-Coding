
class Account:
    def __init__(self):
        self.__balance = 1000 # Private varaible

    def showbalance(self):
        print(self.__balance)

    def deposit(self,ammount):
        self.__balance += ammount

acc = Account()

acc.showbalance()
acc.deposit(500)
acc.showbalance()