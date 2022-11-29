from flask import Flask, render_template
from user.seller.seller import Individual_seller
import sys
import pymysql


app = Flask(__name__)

@app.route('/')
@app.route('/main')
def home():
    return render_template('home.html') #insert home html file path here

if __name__ == '__main__':
    s = Individual_seller("a", "a", "a", "a", "a", "a", "a", "a", "a", "a")
    s.get_item_number()
	#app.run(host='0.0.0.0', port=int(sys.argv[1]))