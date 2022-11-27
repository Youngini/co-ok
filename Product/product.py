# 상품명 product_name
# 원가 cost
# 인당 할인율 discount_per_person
# 공구최소정원 min_group_num
# 공구최대정원 max_group_num
# 모임모집기한 apply_deadline
# 상품사진 product_pict
# 카테고리 category

class Product:
    def __init__(self, product_name, cost, discount_per_person, min_group_num, max_group_num, apply_deadline, product_pict, category):
        self.product_name = product_name
        self.cost = cost
        self.discount_per_person = discount_per_person
        self.min_group_num = min_group_num
        self.max_group_num = max_group_num
        self.apply_deadline = apply_deadline
        self.product_pict = product_pict
        self.category = category

    def setProduct_name(self, product_name):
        self.product_name = product_name

    def setCost(self, cost):
        self.cost = cost

    def setDiscount_per_person(self, discount_per_person):
        self.discount_per_person = discount_per_person

    def setMin_group_num(self, min_group_num):
        self.min_group_num = min_group_num

    def setMax_group_num(self, max_group_num):
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
