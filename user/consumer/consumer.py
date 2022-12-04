import sys, os
#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from user.user import User
from user.location import Location
from Order.BuyGroup import BuyGroup
from Product.product import Product
from Order.Ordering import Ordering
import pymysql
import pandas as pd

class Consumer(User):
    def __init__(self, identifier="", password="", phone_number="", name="", location=Location(), nick_name=""):
        super().__init__(identifier, password, phone_number, name)
        self.__location = location  # location 객체
        self.__nick_name = nick_name

        self.conn = None  # DB 접속
        self.cur = None  # DB 커서

    def __dbInit(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def dbInsert(self):
        self.__dbInit()
        self.cur.execute("""INSERT INTO consumer 
                                   VALUES('%s', '%s', '%s', '%s', '%s', '%s');
                                   """
                              % (self.identifier, self.password, self.phone_number, self.name,
                                 self.__location, self.__nick_name))
        self.conn.commit()
        self.cur.close()

    def dbRetrieve(self, identifier):
        self.__dbInit()
        rs = self.cur.execute(
            "select * from consumer where identifier = '%s'" % (identifier))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values

        self.identifier = rs.item(0)
        self.password = rs.item(1)
        self.phone_number = rs.item(2)
        self.name = rs.item(3)
        self.__location = rs.item(4)
        self.__nick_name = rs.item(5)
        
    def dbLogin(self, identifier, password):
        self.__dbInit()
        rs = self.cur.execute("""select * from consumer where identifier='%s'
                                   """ % (identifier))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values
		
        if len(rs) > 0 and rs.item(1) == password:
            self.dbRetrieve(identifier)
            return True
        else:
            return False

    def set_location(self, location):
        self.__location = location

    def set_nick_name(self, nick_name):
        self.__nick_name = nick_name

    def get_location(self):
        return self.__location

    def get_nick_name(self):
        return self.__nick_name

    def print(self):
        print(self.identifier)
        print(self.password)
        print(self.phone_number)
        print(self.name)
        print(self.__location)
        print(self.__nick_name)

# consumer = Consumer('3456','bbbbb','01022222222','consumer','somewhere','monekey')
# consumer.dbInsert()

#pro = Product()
#pro.dbRetrieve('1234')
#pro.get_group_list()