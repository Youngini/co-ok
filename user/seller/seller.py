import pymysql
from user.user import User

class Seller(User):
	def __init__(self, identifier, password, phone_number, name, business_name, email_address, seller_account, telephone_number, business_address, teleselling_registration):
		super().__init__(identifier, password, phone_number, name)
		self.business_name = business_name
		self.email_address = email_address
		self.seller_account = seller_account
		self.telephone_number = telephone_number
		self.business_address = business_address
		self.teleselling_registration = teleselling_registration
	
	def set_business_name(self, business_name):
		self.business_name = business_name
	
	def set_email_address(self, email_address):
		self.email_address = email_address
	
	def set_seller_account(self, seller_account):
		self.seller_account = seller_account
	
	def set_telephone_number(self, telephone_number):
		self.telephone_number = telephone_number

	def set_business_address(self, business_address):
		self.business_address = business_address
	
	def get_business_name(self):
		return self.business_name

	def get_email_address(self):
		return self.email_address

	def get_seller_account(self):
		return self.seller_account
	
	def get_telephone_number(self):
		return self.telephone_number

	def get_business_address(self):
		return self.business_address

	def get_item_number(self):
		connect = pymysql.connect(host='localhost', user='root', password='password', db='cook', charset='utf8')
        
		cursor = connect.cursor()
        
		sql = f"select count(*) from product where seller_id = '{self.identifier}'"
        
		cursor.execute(sql)
		result = cursor.fetchall()
		
		connect.commit()
		connect.close()
        
		return int(result[0][0])

class IndividualSeller(Seller):	
	def __init__(self, identifier, password, phone_number, name, business_name, email_address, seller_account, telephone_number, business_address, teleselling_registration):
		super().__init__(identifier, password, phone_number, name, business_name, email_address, seller_account, telephone_number, business_address, teleselling_registration)

class CorporateSeller(Seller):
	def __init__(self, identifier, password, phone_number, name, business_name, email_address, seller_account, telephone_number, business_address, teleselling_registration, business_registration):
		super().__init__(identifier, password, phone_number, name, business_name, email_address, seller_account, telephone_number, business_address, teleselling_registration)
		self.business_registration = business_registration
