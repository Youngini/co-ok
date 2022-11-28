class moneyTransfer:
    def __init__(self,bank_account,bank,bank_psw):
        self.bank_account = bank_account
        self.bank = bank
        self.bank_psw = bank_psw

    def setBankaccount(self,bank_account):
        self.bank_account = bank_account

    def setBank(self,bank):
        self.bank = bank
    
    def setAccountpsw(self,bank_psw):
        self.bank_psw = bank_psw

    def getBankaccount(self):
        return self.bank_account
    
    def getBank(self):
        return self.bank
    
    def getAccountpsw(self):
        return self.bank_psw