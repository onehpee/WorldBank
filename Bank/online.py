
class user:
    print("Welcome to World Bank Online")
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance
    
    def signIn(self):
        self.username = str(input("Please Enter Your Username: "))
        self.password = str(input("Please Enter Your Password: "))