class Account:
    account = []

    def __init__(self,name,accNo,password,type):
        self.name = name
        self.accNo = accNo
        self.password = password
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

myacc = Account("ratin",1234,1234,"saving")
myacc.changeInfo("gorib",123)
