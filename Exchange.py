# 사유 reason
# 결함사진 faulty_img
# 주문일자 order_date

class Exchange:
    def __init__(self, reason, faulty_img, order_date):
        self.reason = reason
        self.faulty_img = faulty_img
        self.order_date = order_date

    def set_reason(self, reason):
        self.reason = reason

    def set_faulty_img(self, faulty_img):
        self.faulty_img = faulty_img

    def set_order_date(self):
        self.order_date = order_date

    def get_reason(self):
        return self.reason

    def get_faulty_img(self):
        return self.faulty_img

    def get_order_date(self):
        return self.order_date
    

