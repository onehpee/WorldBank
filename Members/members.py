import re
import math
from Bank import Bank

class Members:
    #constructor
    def __init__(self, accNo, prefix, firstName, lastName, SOS, type, balance = 0):
        #instance attributesssssssss
        self.accNo = accNo
        self.prefix = prefix
        self.firstName = firstName
        self.lastName = lastName
        self.SOS = SOS
        self.type = type
        self.balance = balance
     
     
    def createAccount(self):
        self.accNo = int(input("Enter the account No#: "))
        self.firstName = input("Enter The Account Holder's First Name: ")
        self.lastName = input("Enter The Account Holder's Last Name: ")
        self.SOS = input("Enter The Account Holder's Social Security Number")
        print("\n\n\nAccount Has Been Created")
        
    def passLenCheck(self):
        if len(self.password) >= 8:
            self.password = self.password
        else:
            print("This Password doesn't have 8 or more characters")
    
    def passSpecChar(self):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if regex.search(self.password) == None:
            self.password = self.password
        else:
            print("This Password doesn't contain a special character like: [@_!#$%^&*()<>?/\|}{~:]")
            
    def passUpperChar(self):
        check = False
        for char in self.password:
            if char.isupper():
                check = True
                break
        
    def deposit(self):
        amount = float(input(f"{self.firstName}, {self.lastName}, please enter how much you would like to deposit: "))
        print("Thank you for depositing....")
        self.balance += amount
        deposit_id = str(input("> Enter your Customer ID: "))
        deposit_balance = str(input("> Enter the BALANCE to be deposit: "))
        deposit_pass = str(input("> Enter your Password: "))
        return f"Your balance is now: {self.balance}"
        
    def withdraw(self):
        amount = float(input(f"{self.firstName}, {self.lastName}, please enter how much you would like to withdraw: "))  
        withdrawal_id = str(input("> Enter your Customer ID: "))
        withdrawal_balance = str(input("> Enter the BALANCE to be withdraw: "))
        withdrawal_pass = str(input("> Enter your Password: "))     
        if self.balance < amount:
            return "You don't have the funds to withdraw"
        else:
            print("Thank you for withdrawing...")
            self.balance -= amount
        
    def accInfo(self):
        print("Welcome" + self.firstName + self.lastName)
        
    def accPriv_Info(self):
        print("Account Info: " + self.accNo + self.firstName + self.lastName + self.SOS)
        
        
while True:
    print("Welcome to the World Bank")
    userFN = input("Enter Your First Name: ")
    userLN = input("Enter Your Last Name: ")
    userSOS = input("Enter Your Social Security Number: ")
    userType = input("Enter The Type of Banking Account: ")
    user = Members()
    new_user = input("Would you like to register a new user")