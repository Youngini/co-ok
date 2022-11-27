class card:
    def __init__(self,cardID,cardname,cardpsw,cardCVC):
        self.cardID = cardID
        self.cardname = cardname
        self.cardpsw = cardpsw
        self.cardCVC = cardCVC

    def setCardID(self,cardID):
        self.cardID = cardID
    
    def setCardname(self,cardname):
        self.cardname = cardname

    def setCardpsw(self,cardpsw):
        self.cardpsw = cardpsw
    
    def setCardCVC(self,cardCVC):
        self.cardCVC = cardCVC

    def getCardID(self):
        return self.cardID
    
    def getCardname(self):
        return self.cardname

    def getCardpsw(self):
        return self.cardpsw
    
    def getCardCVC(self):
        return self.cardCVC