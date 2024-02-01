import re
class app:
    print("Welcome to World Bank Online")
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    # def home():
    #     print("\n>> World Bank Home:")
    #     print("1. Create New Profile\n2. Login\n3. Info\n4. Log Out")
    #     Task=int(input("> Please select your option (1/2/3/4): "))
    #     while(Task !='4'):
    #         if (Task==1):
    #             #new proflie
    #         elif(Task==2):
    #             #login
    #         elif(Task==3):
    #             #info
    #         elif(Task==4):
    #             print("=== GOOD BYE, SEE YOU AGAIN! ===\n\n")
    #             main_menu()
    #         else:
    #             print("!!! Invalid Option! Please read the option carefully! !!!\n")
    #     Task=int(input("Please select your option (1/2/3/4): "))

        
    # def create_account(self):
        
    #     credit_card_number = "400000" + format(randint(0000000000, 9999999999), '010d')
    #     pin_number = format(randint(0000, 9999), '04d')

    #     self.card_numbers.append(credit_card_number)
    #     self.pin_numbers.append(pin_number)
    
    def login(self):
        print("Welcome to the World Bank!! Please Login Below!")
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