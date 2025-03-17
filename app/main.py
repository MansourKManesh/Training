from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# تنظیمات اتصال به MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:A1Alaki@498@localhost/myflaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# مقداردهی اولیه به دیتابیس
from app.models import db, User
db.init_app(app)

@app.route('/')
def home():
    return "اتصال Flask به MySQL موفقیت‌آمیز بود!"

if __name__ == '__main__':
    app.run(debug=True)
