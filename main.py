from flask import Flask, render_template, request
from user.seller.seller import IndividualSeller, CorporateSeller
from user.consumer.consumer import Consumer
from user.consumer.coupon import Coupon
from user.consumer.payment.card import Card
from user.consumer.payment.moneyTransfer import MoneyTransfer
import sys
import pymysql

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        identifier = request.form['id']
        password = request.form['pw']
        
        c = Consumer()
        print(c.dbLogin(identifier, password))
        
        return render_template('main.html')
    else:
        return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
	app.run(host=sys.argv[1], port=int(sys.argv[2]))