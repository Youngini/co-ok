#!/usr/bin/python3

# 상품명 product_name
# 원가 cost
# 인당 할인율 discount_per_person
# 공구최소정원 min_group_num
# 공구최대정원 max_group_num
# 모임모집기한 apply_deadline
# 상품사진 product_pict
# 카테고리 category

import sys
import pymysql
import pandas as pd
from datetime import date, timedelta


class Product:
    # product id는 어떻게?
    def __init__(self, identifier="", product_name="", cost=1, discount_per_person=0, min_group_num=10,
                 max_group_num=10, apply_deadline=str(date.today()), product_pict="", category="", seller_id=""):

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
        self.rs = None  # 쿼리 실행 결과

    def dbInit(self):
        self.conn = pymysql.connect(
            host='localhost', user='', password='', db='cook', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

<<<<<<< HEAD
    def dbUpdate(self):
        self.dbInit()
=======
    def dbInsert(self):
        self.__dbInit()
>>>>>>> 9c61274ebd0d46a86f7c2f1c53c205611dab657d
        # PRODUCT_ID, SELLER_ID, product_pict 어떻게?
        self.rs = self.cur.execute("""INSERT INTO product 
                                   VALUES('%s', '%s', '%d', '%d', '%d',
                                          '%d', '%s', '%s', '%s');
                                   """
                                   % (self.__identifier, self.__product_name, self.__cost, self.__discount_per_person,
                                      self.__min_group_num, self.__max_group_num, self.__apply_deadline,
                                      self.__category, self.__seller_id))
        self.conn.commit()
        self.cur.close()

<<<<<<< HEAD
    def dbPrintOne(self, identifier):
        self.dbInit()
        self.cur.execute(
            "SELECT * FROM product WHERE identifier = '%s';" % (identifier))
=======
    def dbRetrieve(self, identifier):
        self.__dbInit()
        self.rs = self.cur.execute("select * from product where identifier = '%s'" % (identifier))
>>>>>>> 9c61274ebd0d46a86f7c2f1c53c205611dab657d
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs)
        print(rs)

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

        #  def getDiscounted(self):
        # def setDetailed_info(self, )
        # def getMaxprice(self)
        # def getMinprice(self)
        # def getGroup()
        # 최소가격이 원가의 50%이하일때 판매자한테 경고
        # 할인공식:(100-인당할인률)/100 ** 구매인ㅇ


# identifier = input("product id: ")
# pname = input("pname: ")
# cost = int(input("cost: "))
# dpp = int(input("discount_per_person: "))
# mingn = int(input("mingn: "))
# maxgn = int(input("maxgn: "))
# ad = input("apply_deadline: ")
# pict = input("product_pict: ")
# cate = input("category: ")
# seller_id = input("seller_id: ")

Pro = Product()
Pro.dbInit()
# Pro.dbUpdate()
Pro.dbPrintOne('1234')
