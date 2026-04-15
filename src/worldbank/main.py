from py_compile import main
import re
import math

class Members():
    def __init__(self, accNo, prefix, firstName, lastName, SOS, type, PIN, balance = 0):
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
        if self.accNo < 100000 or self.accNo > 999999:
            print("Invalid account number. Please enter a 6-digit number.")
            return
        self.firstName = str(input("Enter The Account Holder's First Name: "))
        self.lastName = str(input("Enter The Account Holder's Last Name: "))
        address = str(input("Enter your address including country"))
        self.SOS = int(input("Enter The Account Holder's Social Security Number"))
        if self.SOS < 100000000 or self.SOS > 999999999:
            print("Invalid Social Security Number. Please enter a 9-digit number.")
            return
        self.type = str(input("Pick an account you would like to create Checking or Saving"))
        if self.type.lower() not in ["checking", "saving"]:
            print("Invalid account type. Please enter 'Checking' or 'Saving'.")
            return
        self.PIN = int(input("Create a 4-digit pin"))
        if self.PIN < 1000 or self.PIN > 9999:
            print("Invalid PIN. Please enter a 4-digit number.")
            return
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
        
        
        
        
member = Members()
member.createAccount()
    
        
if __name__ == "__main__":
    main()
