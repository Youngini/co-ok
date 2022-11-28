class card:
    def __init__(self,card_id,card_name,card_psw,card_cvc):
        self.card_id = card_id
        self.card_name = card_name
        self.card_psw = card_psw
        self.card_cvc = card_cvc

    def setCardID(self,card_id):
        self.card_id = card_id
    
    def setCardname(self,card_name):
        self.card_name = card_name

    def setCardpsw(self,card_psw):
        self.card_psw = card_psw
    
    def setCardCVC(self,card_cvc):
        self.card_cvc = card_cvc

    def getCardID(self):
        return self.card_id
    
    def getCardname(self):
        return self.card_name

    def getCardpsw(self):
        return self.card_psw
    
    def getCardCVC(self):
        return self.card_cvc
