class Location:
	def __init__(self, road_name_address="", detailed_address="", zip_code=""):
		self.__road_name_address = road_name_address
		self.__detailed_address = detailed_address
		self.__zip_code = zip_code
	
	def set_road_name_address(self, road_name_address):
		self.__road_name_address = road_name_address

	def set_detailed_address(self, detailed_address):
		self.__detailed_address = detailed_address

	def set_zip_code(self, zip_code):
		self.__zip_code = zip_code

	def get_road_name_address(self):
		return self.__road_name_address

	def get_detailed_address(self):
		return self.__detailed_address

	def get_zip_code(self):
		return self.__zip_code
