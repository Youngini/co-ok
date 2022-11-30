#모임명 group_name
#모임정원 group_limit
#현재모임정원 pgroup_number
#공동구매모임 상품개수 pgroup_product_number
#할인 가격 discount_price
class Group:
	def __init__(self, group_name, group_limit, pgroup_number, pgroup_product_number, discount_price):
		self.group_name = group_name
		self.group_limit = group_limit
		self.pgroup_number = pgroup_number
		self.pgroup_product_number = pgroup_product_number
		self.discount_price = discount_price

	def setGroupName(self, group_name):
		self.group_name = group_name

	def setGroupLimit(self, pgroup_number):
		self.group_limit = pgroup_number

	def setPGroupNumber(self, pgroup_number):
		self.pgroup_number = pgroup_number

	def setPGroupProductNumber(self, pgroup_product_number):
		self.pgroup_product_number = pgroup_product_number
    
	def setDiscountPrice(self, discount_price):
		self.discount_price = discount_price

	def getGroupName(self):
		return self.group_name

	def getGroupLimit(self):
		return self.group_limit

	def getPGroupNumber(self):
		return self.pgroup_number

	def getPGroupProductNumber(self):
		return self.pgroup_product_number

	def getDiscountPrice(self):
		return self.discount_price


    