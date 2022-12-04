from flask import Flask, render_template, request
from user.seller.seller import IndividualSeller, CorporateSeller
from user.consumer.consumer import Consumer
from user.consumer.coupon import Coupon
from user.consumer.payment.card import Card
from user.consumer.payment.moneyTransfer import MoneyTransfer
from Product.product import Product
from Product.Evaluation.evaluation import Evaluation
from Order.Ordering import Ordering
from Order.BuyGroup import BuyGroup
from Order.Return import Return
from Order.Exchange import Exchange
import sys
import pymysql
import pandas as pd

app = Flask(__name__)

global user
user = None

@app.route('/', methods=['POST', 'GET'])
def home():
    global user
    if request.method == 'POST':
        identifier = request.form['id']
        password = request.form['pw']
        
        user = Consumer()
        if user.dbLogin(identifier, password):
            return render_template('main_customer.html')
        
        user = CorporateSeller()
        if user.dbLogin(identifier, password):
            return render_template('main_seller.html')
        
    if type(user) is Consumer:
        return render_template('main_customer.html')
    if type(user) is CorporateSeller:
        return render_template('main_seller.html')
    
    return render_template('main.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/consumer')
def consumer():
    user
    return render_template('mypage_consumer.html')

@app.route('/seller')
def seller():
    return render_template('mypage_seller.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
    global user
    if request.method == 'POST':
        searching = request.form['searching']
        conn = pymysql.connect(
            host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
        cur = conn.cursor(pymysql.cursors.DictCursor)
        rs = cur.execute("""select * from product where name like '%%%s%%'
                                   """ % (searching))
        rs = cur.fetchall()
        
        print(rs)
        
        if type(user) is Consumer:
            return render_template('search_customer.html', products = rs)
        if type(user) is CorporateSeller:
            return render_template('search_seller.html', products = rs)
    
    return render_template('main.html')   

if __name__ == '__main__':
	app.run(host=sys.argv[1], port=int(sys.argv[2]))
    