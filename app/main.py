from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# تنظیمات اتصال به MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://flaskuser:A1Alaki%40498@localhost/myflaskdb"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# مقداردهی اولیه به دیتابیس
from app.models import db, User
db.init_app(app)

@app.route('/')
def home():
    return "اتصال Flask به MySQL موفقیت‌آمیز بود!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "کاربر با موفقیت اضافه شد!"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return jsonify(users_list)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "❌ کاربر پیدا نشد!"}), 404

    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    
    db.session.commit()
    return jsonify({"message": "✅ اطلاعات کاربر با موفقیت به‌روزرسانی شد!"})
