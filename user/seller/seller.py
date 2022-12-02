import pymysql
import pandas as pd
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from user.user import User

class Seller(User):
    def __init__(self, identifier="", password="", phone_number="", name="", business_name="", email_address="", seller_account="",
                 telephone_number="", business_address="", teleselling_registration="", buisiness_registration=""):
        super().__init__(identifier, password, phone_number, name)
        self.__business_name = business_name
        self.__email_address = email_address
        self.__seller_account = seller_account
        self.__telephone_number = telephone_number
        self.__business_address = business_address
        self.__teleselling_registration = teleselling_registration
        self.__buisiness_registration = buisiness_registration

        self.conn = None  # DB 접속
        self.cur = None  # DB 커서

    def __dbInit(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def dbInsert(self):
        self.__dbInit()
        self.cur.execute("""INSERT INTO seller
                                   VALUES('%s', '%s', '%s', '%s', '%s',
                                          '%s', '%s', '%s', '%s', '%s', '%s');
                                   """
                                   % (self.identifier, self.password, self.phone_number, self.name,
                                      self.__business_address, self.__email_address, self.__seller_account,
                                      self.__telephone_number, self.__business_address, self.__teleselling_registration,
                                       self.__buisiness_registration))
        self.conn.commit()
        self.cur.close()

    def dbRetrieve(self, identifier):
        self.__dbInit()
        rs = self.cur.execute("""select * from seller where identifier='%s'
                                   """ % (identifier))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values

        self.__identifier = rs.item(0)
        self.__password = rs.item(1)
        self.__phone_number = rs.item(2)
        self.__name = rs.item(3)
        self.__business_name = rs.item(4)
        self.__email_address = rs.item(5)
        self.__seller_account = rs.item(6)
        self.__telephone_number = rs.item(7)
        self.__business_address = rs.item(8)
        self.__teleselling_registration = rs.item(9)
        self.__buisiness_registration = rs.item(10)

    def set_business_name(self, business_name):
        self.__business_name = business_name

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def set_seller_account(self, seller_account):
        self.__seller_account = seller_account

    def set_telephone_number(self, telephone_number):
        self.__telephone_number = telephone_number

    def set_business_address(self, business_address):
        self.__business_address = business_address

    def set_teleselling_registration(self, teleselling_registration):
        self.__teleselling_registration = teleselling_registration

    def set_business_registration(self, business_registration):
        self.__business_registration = business_registration

    def get_business_name(self):
        return self.__business_name

    def get_email_address(self):
        return self.__email_address

    def get_seller_account(self):
        return self.__seller_account

    def get_telephone_number(self):
        return self.__telephone_number

    def get_business_address(self):
        return self.__business_address

    def get_business_registration(self):
        return self.__business_registration

    def get_item_number(self):
        self.__dbInit()
        rs = f"select count(*) from product where seller_id = '{self.__identifier}'"

        self.cur.execute(rs)
        rs = self.cur.fetchall()

        result = pd.DataFrame(result)
        self.conn.commit()
        self.conn.close()

        return result.item(0)

    def print(self):
        print(self.__identifier)
        print(self.__password)
        print(self.__phone_number)
        print(self.__name)
        print(self.__business_name)
        print(self.__email_address)
        print(self.__seller_account)
        print(self.__telephone_number)
        print(self.__business_address)
        print(self.__teleselling_registration)
        print(self.__business_registration)


class IndividualSeller(Seller):
    def __init__(self, identifier, password, phone_number, name, business_name, email_address, seller_account, telephone_number, business_address, teleselling_registration):
        super().__init__(identifier, password, phone_number, name, business_name, email_address,
                         seller_account, telephone_number, business_address, teleselling_registration)


class CorporateSeller(Seller):
    def __init__(self, identifier, password, phone_number, name, business_name, email_address, seller_account, telephone_number, business_address, teleselling_registration, business_registration):
        super().__init__(identifier, password, phone_number, name, business_name, email_address,
                         seller_account, telephone_number, business_address, teleselling_registration)
        self.__business_registration = business_registration

seller = Seller('2345', 'aaaaa', '01011111111', 'hongs', 'cop','asd@sf.sdf',
                'afds','01012341234','home','home somewhere','cop somewhere')
seller.dbInsert()