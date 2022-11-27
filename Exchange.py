# 사유 reason
# 결함사진 faulty_img
# 주문일자 order_date

class Exchange:
    def __init__(self, reason, faulty_img, order_date):
        self.reason = reason
        self.faulty_img = faulty_img
        self.order_date = order_date

    def setReason(self, reason):
        self.reason = reason

    def setFaultyImg(self, faulty_img):
        self.faulty_img = faulty_img

    def setOrderDate(self):
        self.order_date = order_date

    def getReason(self):
        return self.reason

    def getFaultyImg(self):
        return self.faulty_img

    def getOrderDate(self):
        return self.order_date
    

