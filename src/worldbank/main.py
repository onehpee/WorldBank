from py_compile import main
import re
import math

class Bank():
    def __init__(self):
        self.username = None
        self.password = None
        
    def members(self, accNo, prefix, firstName, lastName, SOS, type, PIN, balance = 0):
        self.accNo = accNo
        self.prefix = prefix
        self.firstName = firstName
        self.lastName = lastName
        self.SOS = SOS
        self.type = type
        self.PIN = PIN
        self.balance = balance
        
    def createAccount(self):
        print("Create Your New Account")
        print("--------------------------")
        acco_info = open("acco_info.txt","a")
        self.accNo = int(input("Enter the account No#: "))
        self.firstName = str(input("Enter The Account Holder's First Name: "))
        self.lastName = str(input("Enter The Account Holder's Last Name: "))
        address = str(input("Enter your address including country"))
        self.SOS = int(input("Enter The Account Holder's Social Security Number"))
        self.type = str(input("Pick an account you would like to create Checking or Saving"))
        self.PIN = int(input("Create a 4-digit pin"))
        acco_info.write(str(self.accNo) + "," + str(self.firstName) + "," + str(self.lastName) + "," + str(address) + "," + str(self.SOS) + "," + str(self.type) + "," + str(self.PIN))
        acco_info.close()
        print("\n\n\nAccount Has Been Created!")
        
        
    
    def convert_currency(amount, from_country, to_currency):
    # Map countries to their currency codes
        country_to_currency = {
            "USA": "USD",
            "United States": "USD",
            "UK": "GBP",
            "United Kingdom": "GBP",
            "Japan": "JPY",
            "India": "INR",
            "Canada": "CAD",
            "Australia": "AUD",
            "Eurozone": "EUR"
        }
        
        from_currency = country_to_currency.get(from_country)
        if from_currency is None:
            raise ValueError(f"Unsupported country: {from_country}")
        
        
        
        
first_account = Bank()
first_account.createAccount()
    
        
if __name__ == "__main__":
    main()
