class moneyTransfer:
    def __init__(self,bankaccount,bank,accountpsw):
        self.bankaccount = bankaccount
        self.bank = bank
        self.accountpsw = accountpsw

    def setBankaccount(self,bankaccount):
        self.bankaccount = bankaccount
    
    def setBank(self,bank):
        self.bank = bank
    
    def setAccountpsw(self,accountpsw):
        self.accountpsw = accountpsw

    def getBankaccount(self):
        return self.bankaccount
    
    def getBank(self):
        return self.bank
    
    def getAccountpsw(self):
        return self.accountpsw