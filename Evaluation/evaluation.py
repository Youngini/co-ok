#상품점수 score
#상세평가 detailed_eval
#import Product
#from datetime import date, timedelta

class Evaluation:
    #prod = Product()

    def __init__(self, score, detailed_eval):
        self.__score = score
        self.__detailed_eval = detailed_eval

    def setScore(self, score):
        self.score = score

    def setDetailed_eval(self, detailed_eval):
        self.detailed_eval = detailed_eval

    def getScore(self):
        return self.score

    def getDetailed_eval(self):
        return self.detailed_eval

    