# 모임명 name
# 모임정원 limit_number
# 상품id product_id
# 할인 가격 discount_price

import pymysql
import pandas as pd


class BuyGroup:
    def __init__(self, identifier="", name="", limit_number=30, product_id="", dicounted_price=0):
        self.__identifier = identifier
        self.__name = name
        self.__limit_number = limit_number
        self.__product_id = product_id
        self.__dicounted_price = dicounted_price

        self.conn = None  # DB 접속
        self.cur = None  # DB 커서
        self.rs = None  # 쿼리 실행 결과

    def __dbInit(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def dbInsert(self):
        self.__dbInit()
        self.rs = self.cur.execute("""INSERT INTO buygroup
                                   VALUES('%s', '%s', '%d', '%s', '%d');
                                   """
                                   % (self.__identifier, self.__name, self.__limit_number, self.__product_id, self.__dicounted_price))
        self.conn.commit()
        self.cur.close()

    def dbRetrieve(self, identifier):
        self.__dbInit()
        self.rs = self.cur.execute("""select * from buygroup where identifier='%s'
                                   """ % (identifier))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values

        self.__identifier = rs.item(0)
        self.__name = rs.item(1)
        self.__limit_number = rs.item(2)
        self.__product_id = rs.item(3)
        self.__dicounted_price = rs.item(4)

    def print(self):
        print(self.__identifier)
        print(self.__name)
        print(self.__limit_number)
        print(self.__product_id)
        print(self.__dicounted_price)

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
