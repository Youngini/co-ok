import pandas as pd
import pymysql

class Card:
    def __init__(self,identifier="",name="",password="",cvc="", consumer_id=""):
        self.__identifier = identifier
        self.__name = name
        self.__password = password
        self.__cvc= cvc
        self.__consumer_id = consumer_id

        self.conn = None
        self.cur = None
        
    def __dbInit(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def dbInsert(self):
        self.__dbInit()
        self.cur.execute("""INSERT INTO card 
                                   VALUES('%s', '%s', '%s', '%s', '%s');
                                   """
                              % (self.__identifier, self.__name, self.__password, self.__cvc, self.__consumer_id))
        
        self.conn.commit()
        self.cur.close()

    def dbRetrieve(self, identifier):
        self.__dbInit()
        rs = self.cur.execute(
            "select * from card where identifier = '%s'" % (identifier))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values

        self.__identifier = rs.item(0)
        self.__name = rs.item(1)
        self.__password = rs.item(2)
        self.__cvc = rs.item(3)
        self.__consumer_id = rs.item(4)

    def set_identifier(self,identifier):
        self.__identifier = identifier
    
    def set_name(self,name):
        self.__name = name

    def set_password(self,password):
        self.__password = password
    
    def set_cvc(self,cvc):
        self.__cvc = cvc
    
    def set_consumer_id(self, consumer_id):
        self.__consumer_id = consumer_id

    def get_identifier(self):
        return self.__identifier
    
    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password
    
    def get_cvc(self):
        return self.__cvc

    def get_consumer_id(self):
        return self.__consumer_id

    def print(self):
        print(self.__identifier)
        print(self.__name)
        print(self.__password)
        print(self.__cvc)
        print(self.__consumer_id)
