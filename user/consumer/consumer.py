from user.user import User

class Consumer(User):
	def __init__(self, identifier, password, phone_number, name, location, nick_name):
		super().__init__(identifier, password, phone_number, name)
		self.location = location # location 객체
		self.nick_name = nick_name

	def set_location(self, location):
		self.location = location
    
	def set_nick_name(self, nick_name):
		self.nick_name = nick_name

	def get_location(self):
		return self.location

	def get_nick_name(self):
		return self.nick_name
