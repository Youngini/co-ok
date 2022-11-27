# 상품명 product_name
# 원가 cost
# 인당 할인율 discount_per_person
# 공구최소정원 min_group_num
# 공구최대정원 max_group_num
# 모임모집기한 apply_deadline
# 상품사진 product_pict
# 카테고리 category

from datetime import date, timedelta
#import Evaluation

class Product:
	#seller = seller()
	def __init__(self, product_name="", cost=1, discount_per_person=0, min_group_num=10,max_group_num=10, apply_deadline=date.today(), product_pict="", category=""):
		self.__product_name = product_name
		self.__cost = cost
		self.__discount_per_person = discount_per_person
		self.__min_group_num = min_group_num
		self.__max_group_num = max_group_num
		self.__apply_deadline = apply_deadline
		self.__product_pict = product_pict
		self.__category = category

	def setProduct_name(self, product_name):
		self.product_name = product_name

	def setCost(self, cost):
		if cost >= 1 and cost <= 999999999:
			self.cost = cost

	def setDiscount_per_person(self, discount_per_person):
		self.discount_per_person = discount_per_person

	def setMin_group_num(self, min_group_num):
		if min_group_num >= 10:
			self.min_group_num = min_group_num
	
	def setMax_group_num(self, max_group_num):
		if max_group_num <= 500:
			self.max_group_num = max_group_num

	def setApply_deadline(self, apply_deadline):
		self.apply_deadline = apply_deadline

	def setProduct_pict(self, product_pict):
		self.product_pict = product_pict
	
	def setCategory(self, category):
		self.category = category
	
	def getProduct_name(self):
		return self.product_name

	def getCost(self):
		return self.cost

	def getDiscount_per_person(self):
		return self.discount_per_person

	def getMin_group_num(self):
		return self.min_group_num

	def getMax_group_num(self):
		return self.max_group_num

	def getApply_deadline(self):
		return self.apply_deadline

	def getProduct_pict(self):
		return self.product_pict

	def getCategory(self):
		return self.category

    # def __getDiscounted(self):
	# def setDetailed_info(self, )
	# def getMaxprice(self)
	# def getMinprice(self)
	# def getGroup()
	# 최소가격이 원가의 50%이하일때 판매자한테 경고
	# 할인공식:(100-인당할인률)/100 ** 구매인원 