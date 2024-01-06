class Members:
    #constructor
    def __init__(self, accNo, prefix, firstName, lastName, SOS, type,money = 0):
        #instance attributesssssssss
        self.accNo = accNo
        self.prefix = prefix
        self.firstName = firstName
        self.lastName = lastName
        self.SOS = SOS
        self.type = type
        self.money = money
     
     
    def createAccount(self):
        self.accNo = int(input("Enter the account No#: "))
        self.firstName = input("Enter The Account Holder's First Name: ")
        self.lastName = input("Enter The Account Holder's Last Name: ")
        self.SOS = input("Enter The Account Holder's Social Security Number")
        print("\n\n\nAccount Has Been Created")

    def deposit(self):
        print("You have deposited: " + self.money)
        
    def info(self):
        print("Welcome" + self.firstName + self.lastName)
        
    def priv_info(self):
        print("Account Info: " + self.accNo + self.firstName + self.lastName + self.SOS)