# 주문번호 order_number
# 주문일자 order_date
# 상품 개수 product_number
# 할인가격 discount_price

import pymysql
import pandas as pd
from datetime import datetime


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
		self.cur.execute("""INSERT INTO Ordering
                                   VALUES('%s', '%s', '%d', '%d', '%s', '%s');
                                   """
                                   % (self.__identifier, self.__order_date, self.__product_number,
									self.__paid_price, self.__group_id, self._consumer_id))
		self.conn.commit()
		self.cur.close()

	def dbRetrieve(self, group_id, consumer_id):
		self.__dbInit()
		rs = self.cur.execute("""select * from Ordering where group_id='%s', consumer_id='%s';
                                   """ % (group_id, consumer_id))
		rs = self.cur.fetchall()
		rs = pd.DataFrame(rs).values

		self.__identifier = rs.item(0)
		self.__order_date = rs.item(1)
		self.__product_number = rs.item(2)
		self.__paid_price = rs.item(3)
		self.__group_id = rs.item(4)
		self.__consumer_id = rs.item(5)

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