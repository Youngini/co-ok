from user.user import User
from user.location import Location
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
                              % (self.__identifier, self.__password, self.__phone_number, self.__name,
                                 self.__location, self.__nick_name))
        self.conn.commit()
        self.cur.close()

    def dbRetrieve(self, identifier):
        self.__dbInit()
        rs = self.cur.execute(
            "select * from consumer where identifier = '%s'" % (identifier))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values
        
        if len(rs) == 0:
            return False
        
        self.__identifier = rs.item(0)
        self.__password = rs.item(1)
        self.__phone_number = rs.item(2)
        self.__name = rs.item(3)
        self.__location = rs.item(4)
        self.__nick_name = rs.item(5)
        
        return True
        
    def dbLogin(self, identifier, password):
        self.__dbInit()
        rs = self.cur.execute(
            "select * from consumer where identifier = '%s'" % (identifier))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values
        
        if len(rs) == 0:
            return False
        if rs.item(1) != password:
            return False
        if rs.item(1) == password:
            self.dbRetrieve(identifier)
            return True

    def set_location(self, location):
        self.__location = location

    def set_nick_name(self, nick_name):
        self.__nick_name = nick_name

    def get_location(self):
        return self.__location

    def get_nick_name(self):
        return self.__nick_name

    def print(self):
        print(self.__identifier)
        print(self.__password)
        print(self.__phone_number)
        print(self.__name)
        print(self.__location)
        print(self.__nick_name)