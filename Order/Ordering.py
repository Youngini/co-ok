# 주문번호 order_number
# 주문일자 order_date
# 상품 개수 product_number
# 할인가격 discount_price

import pymysql
import pandas as pd
from datetime import datetime
from Order.BuyGroup import BuyGroup
from Afterservice.Exchange import Exchange
from Afterservice.Return import Return


class Ordering:
    def __init__(self, identifier="", order_date=datetime.today(), product_number=0, paid_price=0, group_id="", consumer_id=""):
        self.__identifier = identifier
        self.__order_date = order_date
        self.__product_number = product_number
        self.__paid_price = paid_price
        self.__group_id = group_id
        self._consumer_id = consumer_id

        self.conn = None
        self.cur = None

    def __dbInit(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def dbInsert(self):
        self.__dbInit()
        self.cur.execute("""INSERT INTO ordering
                                   VALUES('%s', '%s', %d, %d, '%s', '%s');
                                   """
                         % (self.__identifier, self.__order_date, int(self.__product_number),
                            int(self.__paid_price), self.__group_id, self._consumer_id))
        self.conn.commit()
        self.cur.close()

    def dbRetrieve(self, identifier):
        self.__dbInit()
        rs = self.cur.execute("""select * from ordering where identifier='%s';
                                   """ % (identifier))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values

        self.__identifier = rs.item(0)
        self.__order_date = rs.item(1)
        self.__product_number = rs.item(2)
        self.__paid_price = rs.item(3)
        self.__group_id = rs.item(4)
        self.__consumer_id = rs.item(5)

    def make_order(self, group_id, consumer_id):
        self.__dbInit()
        order_number = self.__get_consumer_number()
        buygroup = BuyGroup()
        buygroup.dbRetrieve(self.__group_id)

        limit_number = buygroup.get_limit_number()

        if order_number > limit_number:
            print("order_number over limit")

    def __get_consumer_number(self):
        self.__dbInit()
        self.cur.execute("select count(*) from ordering where group_id = '%s'" %
                         (self.__group_id))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values

        return rs.item(0)
    
    def make_exchange(self):
        exchange = Exchange("", self.__order_date, self.__identifier)
        
        return exchange
    
    def make_returning(self):
        returning = Return("", self.__order_date, self.__identifier)
        
        return returning
	
    def set_order_number(self, order_number):
        self.__order_number = order_number

    def set_order_date(self, order_date):
        self.__order_date = order_date

    def set_product_number(self, product_number):
        self.__product_number = product_number

    def set_discount_price(self, discount_price):
        self.__discount_price = discount_price

    def get_order_number(self):
        return self.__order_number

    def get_order_date(self):
        return self.__order_date

    def get_product_number(self):
        return self.__product_number

    def get_discount_price(self):
        return self.__discount_price

    def print(self):
        print(self.__identifier)
        print(self.__order_date)
        print(self.__product_number)
        print(self.__paid_price)
        print(self.__group_id)
        print(self.__consumer_id)
        
    @classmethod
    def make_identifier(cls):
        return "od" + datetime.now().strftime('%y%m%d%H%M%S%f')



#order = Ordering('6789', '2022-12-03', '1234', 30, '4567', '3456')
#order.make_order('4567', '3456')
