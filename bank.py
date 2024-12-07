from abc import ABC,abstractmethod
class Account(ABC):
    account = []

    def __init__(self,name,accNo,password,type):
        self.name = name
        self.accNo = accNo
        self.password = password
        self.balance = 0
        self.type = type

        Account.account.append(self)

    def changeInfo(self,name):
        self.name = name
        print(f"name change to{name}")
    #overload the changeInfo method
    def changeInfo(self,newName,newsPass):
        self.newName = newName
        self.newPass = newsPass
        print(f"name change to {newName},{newsPass}")
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self,amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
    
    @abstractmethod
    def ShowInfo(self):
        pass

class SavingAccount(Account):
    def __init__(self, name, accNo, password,irate):
        super().__init__(name, accNo, password, "saving")
        self.irate = irate

    def ShowInfo(self):
        print("Account name : {self.name}")
        print("Account type : {self.type}")
class SpecialAccount(Account):
    def __init__(self, name, accNo, password,limit):
        super().__init__(name, accNo, password, "special")
        self.limit = limit

    def ShowInfo(self):
        print("Account name : {self.name}")
        print("Account type : {self.type}")

    def withdraw(self, amount,name):
         if amount > 0 and self.limit >= amount:
            self.balance -= amount


myacc = Account("ratin",1234,1234,"saving")
myacc.changeInfo("gorib",123)
