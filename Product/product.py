#!/usr/bin/python3

# 상품명 product_name
# 원가 cost
# 인당 할인율 discount_per_person
# 공구최소정원 min_group_num
# 공구최대정원 max_group_num
# 모임모집기한 apply_deadline
# 상품사진 product_pict
# 카테고리 category

# .dbInsert() 으로 현재 객체 멤버변수 정보 mysql에 등록
# .dbRetrieve(identifier) 으로 mysql에서 identifier에 해당하는 정보 멤버변수에 할당

import pymysql
import pandas as pd
from datetime import datetime

class Product:
    # product id는 어떻게?
    def __init__(self, identifier="", product_name="", cost=1, discount_per_person=0, min_group_num=10,
                 max_group_num=10, apply_deadline=str(datetime.today()), product_pict="", category="", seller_id=""):

        self.__identifier = identifier
        self.__product_name = product_name
        self.__cost = cost
        self.__discount_per_person = discount_per_person
        self.__min_group_num = min_group_num
        self.__max_group_num = max_group_num
        self.__apply_deadline = apply_deadline
        #self.__product_pict = product_pict
        self.__category = category
        self.__seller_id = seller_id

        self.conn = None  # DB 접속
        self.cur = None  # DB 커서

    def __dbInit(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def dbInsert(self):
        self.__dbInit()
        # PRODUCT_ID, SELLER_ID, product_pict 어떻게?
        self.cur.execute("""INSERT INTO product 
                                   VALUES('%s', '%s', '%d', '%d', '%d',
                                          '%d', '%s', '%s', '%s');
                                   """
                                   % (self.__identifier, self.__product_name, self.__cost, self.__discount_per_person,
                                      self.__min_group_num, self.__max_group_num, self.__apply_deadline,
                                      self.__category, self.__seller_id))
        self.conn.commit()
        self.cur.close()

    def dbRetrieve(self, identifier):
        self.__dbInit()
        self.rs = self.cur.execute("select * from product where identifier = '%s'" % (identifier))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values

        self.__identifier = rs.item(0)
        self.__product_name = rs.item(1)
        self.__cost = rs.item(2)
        self.__discount_per_person = rs.item(3)
        self.__min_group_num = rs.item(4)
        self.__max_group_num = rs.item(5)
        self.__apply_deadline = rs.item(6)
        #self.__product_pict = product_pict
        self.__category = rs.item(7)
        self.__seller_id = rs.item(8)

    def setIdentifier(self, identifier):
        self.__identifier = identifier

    def setProduct_name(self, product_name):
        self.__product_name = product_name

    def setCost(self, cost):
        if cost >= 1 and cost <= 999999999:
            self.__cost = cost

    def setDiscount_per_person(self, discount_per_person):
        self.__discount_per_person = discount_per_person

    def setMin_group_num(self, min_group_num):
        if min_group_num >= 10:
            self.__min_group_num = min_group_num

    def setMax_group_num(self, max_group_num):
        if max_group_num <= 500:
            self.__max_group_num = max_group_num

    def setApply_deadline(self, apply_deadline):
        self.__apply_deadline = apply_deadline

    def setProduct_pict(self, product_pict):
        self.__product_pict = product_pict

    def setCategory(self, category):
        self.__category = category

    def setSeller_id(self, seller_id):
        self.__seller_id = seller_id

    def getIdentifier(self):
        return self.__identifier

    def getProduct_name(self):
        return self.__product_name

    def getCost(self):
        return self.__cost

    def getDiscount_per_person(self):
        return self.__discount_per_person

    def getMin_group_num(self):
        return self.__min_group_num

    def getMax_group_num(self):
        return self.__max_group_num

    def getApply_deadline(self):
        return self.__apply_deadline

    def getProduct_pict(self):
        return self.__product_pict

    def getCategory(self):
        return self.__category

    def getSeller_id(self):
        return self.__seller_id
    
    def print(self):
        print(self.__identifier)
        print(self.__product_name)
        print(self.__cost)
        print(self.__discount_per_person)
        print(self.__min_group_num)
        print(self.__max_group_num)
        print(self.__apply_deadline)
        print(self.__category)
        print(self.__seller_id)
        #  def getDiscounted(self):
        # def setDetailed_info(self, )
        # def getMaxprice(self)
        # def getMinprice(self)
        # def getGroup()
        # 최소가격이 원가의 50%이하일때 판매자한테 경고
        # 할인공식:(100-인당할인률)/100 ** 구매인ㅇ

pro = Product()
pro.dbRetrieve('1234')
pro.print()
