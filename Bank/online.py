import re
class user:
    print("Welcome to World Bank Online")
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance
    
    def signIn(self):
        self.username = str(input("Please Enter Your Username: "))
        self.password = str(input("Please Enter Your Password: "))
        
        
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