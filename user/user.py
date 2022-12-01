class User:
	def __init__(self, identifier="", password="", phone_number="", name=""):
		self.__identifier = identifier
		self.__password = password
		self.__phone_number = phone_number
		self.__name = name
	
	def set_identifier(self, identifier):
		self.__identifier = identifier
	
	def set_password(self, password):
		self.__password = password
	
	def set_phone_number(self, phone_number):
		self.__phone_number = phone_number
	
	def set_name(self, name):
		self.__name = name

	def get_identifier(self):
		return self.__identifier
	
	def get_password(self):
		return self.__password

	def get_phone_number(self):
		return self.__phone_number

	def get_name(self):
		return self.__name
