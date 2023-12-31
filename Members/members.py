class Members:
    #constructor
    def __init__(self, id, prefix, firstName, lastName, SOS, money = 0):
        #instance attributessssssss
        self.id = id
        self.prefix = prefix
        self.firstName = firstName
        self.lastName = lastName
        self.SOS = SOS
        self.money = money
        
    def deposit(self):
        print("You have deposited" + self.money)