# 상품점수 score
# 상세평가 detailed_eval

# .dbInit() 으로 mysql연결, 커서생성
# .dbInsert() 으로 현재 객체 멤버변수 정보 mysql에 등록
# .dbRetrieve(product_id, consumer_id) 으로 mysql에서 identifier에 해당하는 정보 멤버변수에 할당

import pymysql
import pandas as pd
from datetime import datetime


class Evaluation:
    def __init__(self, score=5, detailed_eval="", product_id="", consumer_id=""):
        self.__score = score
        self.__detailed_eval = detailed_eval
        self.__product_id = product_id
        self.__consumer_id = consumer_id

        self.conn = None  # DB 접속
        self.cur = None  # DB 커서
        self.rs = None  # 쿼리 실행 결과

    def __dbInit(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def dbInsert(self):
        self.__dbInit()
        self.rs = self.cur.execute("""INSERT INTO evaluation
                                   VALUES('%d', '%s', '%s', '%s');
                                   """
                                   % (self.__score, self.__detailed_eval, self.__product_id, self.__consumer_id,))
        self.conn.commit()
        self.cur.close()

    def dbRetrieve(self, product_id, consumer_id):
        self.__dbInit()
        self.rs = self.cur.execute("""select * from evaluation where product_id='%s' and consumer_id='%s'
                                   """ % (product_id, consumer_id))
        rs = self.cur.fetchall()
        rs = pd.DataFrame(rs).values

        self.__score = rs.item(0)
        self.__detailed_eval = rs.item(1)
        self.__product_id = rs.item(2)
        self.__consumer_id = rs.item(3)

    def setScore(self, score):
        self.score = score

    def setDetailed_eval(self, detailed_eval):
        self.detailed_eval = detailed_eval

    def getScore(self):
        return self.score

    def getDetailed_eval(self):
        return self.detailed_eval

    def print(self):
        print(self.__score)
        print(self.__detailed_eval)
        print(self.__product_id)
        print(self.__consumer_id)
    
eva = Evaluation()
eva.dbRetrieve('1234','66668')
eva.print()