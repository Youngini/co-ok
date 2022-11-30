# 주문번호 order_number
# 주문일자 order_date
# 상품 개수 product_number
# 할인가격 discount_price
class Order:    
	def __init__(self,order_number, order_date, product_number, discount_price):
		self.order_number = order_number
		self.order_date = order_date
		self.product_number = product_number
		self.discount_price = discount_price

	def setOrderNumber(self, order_number):
		self.order_number = order_number

	def setOrderDate(self, order_date):
		self.order_date = order_date

	def setProductNumber(self, product_number):
		self.product_number = product_number

	def setDiscountPrice(self, discount_price):
		self.discount_price = discount_price

	def getOrderNumber(self):
		return self.order_number

	def getOrderDate(self):
		return self.order_date

	def getProductNumber(self):
		return self.product_number

	def getDiscountPrice(self):
		return self.discount_price