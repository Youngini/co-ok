class MoneyTransfer:
    def __init__(self,account,bank,password):
        self.account = account
        self.bank = bank
        self.password = password

    def set_account(self,account):
        self.account = account

    def set_bank(self,bank):
        self.bank = bank
    
    def set_password(self,password):
        self.password = password

    def get_account(self):
        return self.account
    
    def get_bank(self):
        return self.bank
    
    def get_password(self):
        return self.password