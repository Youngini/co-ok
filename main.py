from flask import Flask, render_template
import sys
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html') #insert home html file path here

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(sys.argv[1]))