class consumer(userAccount):

    def __init__(self,location,nickname):
        self.location = location # location 객체
        self.consumername = nickname

    def setLocation(self,location):
        self.location = location
    
    def setNickname(self,nickname):
        self.nickname = nickname

    def getLocation(self):
        return self.location

    def getNickname(self):
        return self.nickname
