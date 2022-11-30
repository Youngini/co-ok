class Card:
    def __init__(self,identifier,name,password,cvc):
        self.identifier = identifier
        self.name = name
        self.password = password
        self.cvc= cvc

    def set_identifier(self,identifier):
        self.identifier = identifier
    
    def set_name(self,name):
        self.name = name

    def set_password(self,password):
        self.password = password
    
    def set_cvc(self,cvc):
        self.cvc = cvc

    def get_identifier(self):
        return self.identifier
    
    def get_name(self):
        return self.name

    def get_password(self):
        return self.password
    
    def get_cvc(self):
        return self.cvc
