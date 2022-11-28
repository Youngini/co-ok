class User:
	def __init__(self, identifier, password, phone_number, name):
		self.identifier = identifier
		self.password = password
		self.phoneNumber = phone_number
		self.name = name
	
	def set_identifier(self, identifier):
		self.identifier = identifier
	
	def set_password(self, password):
		self.password = password
	
	def set_phone_number(self, phoneNumber):
		self.phone_number = phone_number
	
	def set_name(self, name):
		self.name = name

	def get_identifier(self):
		return self.identifier
	
	def get_password(self):
		return self.password

	def get_phone_number(self):
		return self.phone_number

	def get_name(self):
		return self.name
