import pandas as pd
import pymysql

class MoneyTransfer:
    def __init__(self,account="",bank="",password="",consumer_id=""):
        self.__account = account
        self.__bank = bank
        self.__password = password
        self.__consumer_id = consumer_id

        self.conn = None
        self.cur = None

    def __dbInit(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def dbInsert(self):
        self.__dbInit()
        self.cur.execute("""INSERT INTO moneytransfer 
                                   VALUES('%s', '%s', '%s', '%s');
                                   """
                              % (self.__account, self.__bank, self.__password, self.__consumer_id))
        
        self.conn.commit()
        self.cur.close()

    def dbRetrieve(self, account):
        self.__dbInit()
        rs = self.cur.execute(
            "select * from moneytransfer where account = '%s'" % (account))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values

        self.__account = rs.item(0)
        self.__bank = rs.item(1)
        self.__password = rs.item(2)
        self.__consumer_id = rs.item(3)

    def set_account(self,account):
        self.__account = account

    def set_bank(self,bank):
        self.__bank = bank
    
    def set_password(self,password):
        self.__password = password

    def set_consumer_id(self, consumer_id):
        self.__consumer_id = consumer_id

    def get_account(self):
        return self.__account
    
    def get_bank(self):
        return self.__bank
    
    def get_password(self):
        return self.__password
    
    def get_consumer_id(self):
        return self.__consumer_id

    def print(self):
        print(self.__account)
        print(self.__bank)
        print(self.__password)
        print(self.__consumer_id)