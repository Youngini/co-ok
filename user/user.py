class User:
	def __init__(self, identifier, password, phoneNumber, name):
		self.identifier = identifier
		self.password = password
		self.phoneNumber = phoneNumber
		self.name = name
	
	def setIdentifier(self, identifier):
		self.identifier = identifier
	
	def setPassword(self, password):
		self.password = password
	
	def setPhoneNumber(self, phoneNumber):
		self.phoneNumber = phoneNumber
	
	def setName(self, name):
		self.name = name

	def getIdentifier(self):
		return self.identifier
	
	def getPassword(self):
		return self.password

	def getPhoneNumber(self):
		return self.phoneNumber

	def getName(self):
		return self.name
