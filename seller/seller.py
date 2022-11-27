import sys
sys.path.append('../user')

from user import User

class Seller(User):
	def __init__(self, identifier, password, phoneNumber, name, businessName, emailAddress, sellerAccount, telephoneNumber, businessAddress, telesellingRegistration):
		super().__init__(identifier, password, phoneNumber, name)
		self.businessName = businessName
		self.emailAddress = emailAddress
		self.sellerAccount = sellerAccount
		self.telephoneNumber = telephoneNumber
		self.businessAddress = businessAddress
		self.telesellingRegistration = telesellingRegistration
	
	def setBusinessName(self, businessName):
		self.businessName = businessName
	
	def setEmailAddress(self, emailAddress):
		self.emailAddress = emailAddress
	
	def setSellerAccount(self, sellerAccount):
		self.sellerAccount = sellerAccount
	
	def setTelephoneNumber(self, telephoneNumber):
		self.telephoneNumber = telephoneNumber

	def setBusinessAddress(self, businessAddress):
		self.businessAddress = businessAddress
	
	def getBusinessName(self):
		return self.businessName

	def getEmailAddress(self):
		return self.emailAddress

	def getSellerAccount(self):
		return self.sellerAccount
	
	def getTelephoneNumber(self):
		return self.telephoneNumber

	def getBusinessAddress(self):
		return self.businessAddress

	def getItemNumber(self):
		#get number of item by query to sql
		#develop soon
		pass

class IndividualSeller(Seller):	
	def __init__(self, identifier, password, phoneNumber, name, businessName, emailAddress, sellerAccount, telephoneNumber, businessAddress, telesellingRegistration):
		super().__init__(identifier, password, phoneNumber, name, businessName, emailAddress, sellerAccount, telephoneNumber, businessAddress, telesellingRegistration)

class CorporateSeller(Seller):
	def __init__(self, identifier, password, phoneNumber, name, businessName, emailAddress, sellerAccount, telephoneNumber, businessAddress, telesellingRegistration, businessResgistration):
		super().__init__(identifier, password, phoneNumber, name, businessName, emailAddress, sellerAccount, telephoneNumber, businessAddress, telesellingRegistration)
		self.businessRegistration = businessRegistration
