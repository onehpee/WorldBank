class Members:
    #constructor
    def __init__(self, id, prefix, firstName, lastName, SOS, money = 0):
        #instance attributesssssssss
        self.id = id
        self.prefix = prefix
        self.firstName = firstName
        self.lastName = lastName
        self.SOS = SOS
        self.money = money
        
    def deposit(self):
        print("You have deposited" + self.money)
        
    def info(self):
        print("Welcome" + self.firstName + self.lastName)
        
    def priv_info(self):
        print("Account Info: " + self.id + self.firstName + self.lastName + self.SOS)