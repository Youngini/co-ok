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
from datetime import datetime

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
        
        user = None
        
    if type(user) is Consumer:
        return render_template('main_customer.html')
    if type(user) is CorporateSeller:
        return render_template('main_seller.html')
    
    return render_template('main.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/consumer', methods=['POST', 'GET'])
def consumer():
    global user
    
    if request.method == 'POST':
        identifier = request.form['identifier']
        reason = request.form['reason']
        
        order = Ordering().dbRetrieve('identifier')
        
        if 'refund' in request.form:
            application = order.make_returning()
        else:
            application = order.make_exchange()
            
        application.request_reason(reason)
        
    user.dbRetrieve(user.get_identifier())
    
    rs = user.get_ordering_list()
    
    return render_template('mypage_consumer.html', rs = rs)

@app.route('/seller', methods=['POST', 'GET'])
def seller():
    global user
    if request.method == 'POST':
        name = request.form['name']
        cost = request.form['cost']
        rate = request.form['rate']
        min_num = request.form['min']
        max_num = request.form['max']
        deadline = request.form['deadline']
        category = request.form['category']
        
        
        product = Product(Product.make_identifier(), name, int(cost), int(rate), int(min_num), int(max_num), deadline, category, user.get_identifier())
        
    user.dbRetrieve(user.get_identifier())
    
    rs = user.get_item_list()
    
    item_nums = user.get_item_number()
        
    return render_template('mypage_seller.html', name = user.get_business_name(), rs = rs, item_nums = item_nums)

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
        
        conn.commit()
        cur.close()
        
        if type(user) is Consumer:
            return render_template('search_customer.html', products = rs)
        if type(user) is CorporateSeller:
            return render_template('search_seller.html', products = rs)
    
    return render_template('main.html')   

@app.route('/groups', methods=['POST', 'GET'])
def groups():
    conn = pymysql.connect(
            host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
    cur = conn.cursor(pymysql.cursors.DictCursor)
    
    if request.method == 'POST':
        identifier = request.form['listvalue']
        
        product = Product(identifier)
        product.dbRetrieve(identifier)
        
        grrs = product.get_group_list()
        
        cur.execute("""select buygroup.identifier, count(*) as cnt from ordering, buygroup where ordering.group_id = buygroup.identifier and buygroup.product_id = '%s' group by buygroup.identifier
                                   """ % (identifier))
        
        grcnt = cur.fetchall()
        
    return render_template('group_buy.html', lens = len(grrs), grrs = grrs, grcnt = grcnt, identifier = identifier)

@app.route('/participate', methods=['POST', 'GET'])
def participate():
     if request.method == 'POST':
        if request.method == 'POST':
            conn = pymysql.connect(
                host='localhost', user='root', password='Rlatotquf45!', db='cook', charset='utf8')
            cur = conn.cursor(pymysql.cursors.DictCursor)

            identifier = request.form['listvalue']
            if 'name' in request.form:
                name = request.form['name']
                personnel = int(request.form['personnel'])

                buygroup = BuyGroup(BuyGroup.make_identifier(), name, personnel, identifier)

                buygroup.dbInsert()

                group_id = buygroup.get_identifier()
            else:
                group_id = request.form['group_id']

            cur.execute("""select * from product where identifier = '%s'
                                       """ % (identifier))
            pdrs = cur.fetchall()

            cur.execute("""select * from product, seller where seller.identifier = product.seller_id and product.identifier = '%s'
                                       """ % (identifier))
            slrs = cur.fetchall()

            cur.execute("""select * from buygroup where identifier = '%s'
                                       """ % (group_id))

            grrs = cur.fetchall()

            cur.execute("""select count(*) as cnt from ordering where group_id = '%s' group by group_id
                                       """ % (group_id))

            grcnt = cur.fetchall()

            if len(grcnt) == 0:
                grcnt = 0
            else:
                grcnt = grcnt[0]['cnt']

            cur.execute("""select * from consumer where identifier = '%s'
                                       """ % (user.get_identifier()))

            usrs = cur.fetchall()
        
        return render_template('participate.html', slrs = slrs, pdrs = pdrs, grrs = grrs, grcnt = grcnt, usrs = usrs)
        
@app.route('/done', methods=['POST', 'GET'])
def done():
    if request.method == 'POST':
        identifier = request.form['identifier']
        personnel = request.form['personnel']
        
        buygroup = BuyGroup("identifier")
            
        buygroup.dbRetrieve(identifier)
        
        buygroup.make_ordering(personnel, user.get_identifier())
        
    return render_template('done.html')
    
if __name__ == '__main__':
	app.run(host=sys.argv[1], port=int(sys.argv[2]))
    