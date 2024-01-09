import re
class user:
    print("Welcome to World Bank Online")
    def __init__(self, username, password):
        self.username = str(input("Please Enter Your Username: "))
        self.password = str(input("Please Enter Your Password: "))
    
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