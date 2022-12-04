# 모임명 name
# 모임정원 limit_number
# 상품id product_id
# 할인 가격 discount_price
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import pymysql
import pandas as pd
from datetime import datetime

class BuyGroup:
    def __init__(self, identifier="", name="", limit_number=30, product_id=""):
        self.__identifier = identifier
        self.__name = name
        self.__limit_number = limit_number
        self.__product_id = product_id
        self.__dicounted_price = self.make_discounted_price()

        self.conn = None  # DB 접속
        self.cur = None  # DB 커서

    def __dbInit(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def dbInsert(self):
        self.__dbInit()
        self.cur.execute("""INSERT INTO buygroup
                                   VALUES('%s', '%s', %d, '%s', %d);
                                   """
                                   % (self.__identifier, self.__name, self.__limit_number, self.__product_id, self.__dicounted_price))
        self.conn.commit()
        self.cur.close()

    def dbRetrieve(self, identifier):
        self.__dbInit()
        rs = self.cur.execute("""select * from buygroup where identifier='%s'
                                   """ % (identifier))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values

        self.__identifier = rs.item(0)
        self.__name = rs.item(1)
        self.__limit_number = rs.item(2)
        self.__product_id = rs.item(3)
        self.__dicounted_price = rs.item(4)

    def make_discounted_price(self):
        self.__dbInit()
        self.cur.execute("select cost, discount_per_person from product where identifier='%s'" % 
                        (self.__product_id))
        rs = self.cur.fetchall()
        rs=pd.DataFrame(rs).values

        origin_price = rs.item(0)
        discount_rate = rs.item(1) * 0.01
        group_member_number = self.__limit_number

        discounted_cost = origin_price * ((100-discount_rate)/100)**int(group_member_number) ## 이 부분 맞는지 확인 부탁드립니다

        print(discounted_cost)

        return int(discounted_cost)

    def print(self):
        print(self.__identifier)
        print(self.__name)
        print(self.__limit_number)
        print(self.__product_id)
        print(self.__dicounted_price)

    def set_identifier(self, identifier):
        self.__identifier = identifier

    def set_name(self, name):
        self.__name = name

    def set_limit_number(self, limit_number):
        self.__limit_number = limit_number

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_discounted_price(self, discounted_price):
        self.__dicounted_price = discounted_price

    def get_identifier(self):
        return self.__identifier

    def get_name(self):
        return self.__name

    def get_limit_number(self):
        return self.__limit_number

    def get_product_id(self):
        return self.__product_id

    def get_discounted_price(self):
        return self.__dicounted_price
    
    @classmethod
    def make_identifier(cls):
        return "gr" + datetime.now().strftime('%y%m%d%H%M%S%f')
    
#buygroup = BuyGroup('4567', 'group1',45,'1234',20)
#buygroup = BuyGroup('5678','group2',46,'1234')
#buygroup.dbInsert()
#buygroup.dbRetrieve('5678')
#buygroup.print()
# buygroup = BuyGroup()
# buygroup.dbRetrieve('4567')