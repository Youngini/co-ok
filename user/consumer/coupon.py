import datetime

class coupon:
    def __init__(self, name, discount, experation_date):
        self.name = name
        self.discount = discount
        self.experation_date = experation_date # 질문
    
    def set_name(self, name):
        self.name = name
    
    def set_discount(self, discount):
        self.discount = discount
    
    def set_experation_date(self, experation_date):
        self.experation_date = experation_date

    def get_name(self):
        return self.cname

    def get_discount(self):
        return self.discount

    def get_experation_date(self):
        return self.experation_date
    
