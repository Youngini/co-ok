# 사유 reason
# 결함사진 faulty_img
# 주문일자 order_date

import pymysql
import pandas as pd
from datetime import datetime

class Return:
    def __init__(self, reason="", order_date=datetime.today(), order_id=""):
        self.__reason = reason
        # self.faulty_img = faulty_img
        self.__order_date = order_date
        self.__order_id = order_id

        self.conn = None  # DB 접속
        self.cur = None  # DB 커서

    def __dbInit(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def dbInsert(self):
        self.__dbInit()
        self.cur.execute("""INSERT INTO returning
                                   VALUES('%s', '%s', '%s');
                                   """
                                   % (self.__order_date, self.__reason, self.__order_id))
        self.conn.commit()
        self.cur.close()

    def dbRetrieve(self, order_id):
        self.__dbInit()
        rs = self.cur.execute("""select * from returning where order_id='%s'
                                   """ % (order_id))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values

        self.__reason = rs.item(0)
        # self.faulty_img = faulty_img
        self.__order_date = rs.item(1)
        self.__order_id = rs.item(2)

    def set_reason(self, reason):
        self.__reason = reason

    # def set_faulty_img(self, faulty_img):
    #     self.__faulty_img = faulty_img

    def set_order_date(self, order_date):
        self.__order_date = order_date

    def get_reason(self):
        return self.__reason

    # def get_faulty_img(self):
    #     return self.__faulty_img

    def get_order_date(self):
        return self.__order_date
    
    def print(self):  
        print(self.__order_id)
        print(self.__reason)
        print(self.__order_date)
