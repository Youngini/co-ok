import pymysql
import pandas as pd


class Coupon:
    def __init__(self, name="", discount=0, experation_date="", consumer_id=""):
        self.__name = name
        self.__discount = discount
        self.__experation_date = experation_date  # 질문
        self.__consumer_id = consumer_id

        self.conn = None  # DB 접속
        self.cur = None  # DB 커서

    def __dbInit(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def dbInsert(self):
        self.__dbInit()
        self.cur.execute("""INSERT INTO coupon 
                                   VALUES('%s', '%d', '%s', '%s');
                                   """
                         % (self.__name, self.__discount, self.__experation_date, self.__consumer_id))

        self.conn.commit()
        self.cur.close()

    def dbRetrieve(self, name):
        self.__dbInit()
        rs = self.cur.execute(
            "select * from coupon where name = '%s'" % (name))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values

        self.__name = rs.item(0)
        self.__discount = rs.item(1)
        self.__experation_date = rs.item(2)
        self.__consumer_id = rs.item(3)

    def set_name(self, name):
        self.__name = name

    def set_discount(self, discount):
        self.__discount = discount

    def set_experation_date(self, experation_date):
        self.__experation_date = experation_date

    def set_consumer(self, consumer_id):
        self.__consumer_id = consumer_id

    def get_name(self):
        return self.__name

    def get_discount(self):
        return self.__discount

    def get_experation_date(self):
        return self.__experation_date

    def get_consumer_id(self):
        return self.__consumer_id

    def print(self):
        print(self.__name)
        print(self.__discount)
        print(self.__experation_date)
        print(self.__consumer_id)
