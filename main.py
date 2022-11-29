from flask import Flask, render_template
from user.seller.seller import IndividualSeller, CoporateSeller
from user.consumer.consumer import Consumer
from user.consumer.coupon import Coupon
from user.consumer.payment.card import Card
from user.consumer.payment.moneyTransfer import MoneyTransfer
import sys
import pymysql

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html') #insert home html file path here

if __name__ == '__main__':
	app.run(host=sys.argv[1], port=int(sys.argv[2]))