import datetime

class coupon:
    def __init__(self,cname,discount,date):
        self.cname = cname
        self.discount = discount
        self.date = date # 질문
    
    def setCname(self,cname):
        self.cname = cname
    
    def setDiscount(self,discount):
        self.discount = discount
    
    def setDate(self,date):
        self.date = date

    def getCname(self):
        return self.cname

    def getDiscount(self):
        return self.discount

    def getDate(self):
        return self.date
    