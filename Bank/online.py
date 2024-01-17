import re
class user:
    print("Welcome to World Bank Online")
    def __init__(self, username, password):
        self.username = str(input("Please Enter Your Username: "))
        self.password = str(input("Please Enter Your Password: "))
        
    def create_account(self):
      credit_card_number = "400000" + format(randint(0000000000, 9999999999), '010d')
      pin_number = format(randint(0000, 9999), '04d')

      self.card_numbers.append(credit_card_number)
      self.pin_numbers.append(pin_number)
    
    def accountID(self):
        self.username = not yet
        self.password = not yet
        
        
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
        
        
if __name__ == '__main__' :
    u = user