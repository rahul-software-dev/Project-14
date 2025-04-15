from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

@app.route('/')
def home():
    return "Flask app is connected to PostgreSQL!"

@app.route('/user', methods=['POST'])
def create_user():
    username = request.json.get('username')
    email = request.json.get('email')
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created!"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username, "email": u.email} for u in users])

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    user = User.query.filter_by(username=username).first()
    if user:
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token)
    return jsonify({"message": "Invalid username"}), 401

if __name__ == "__main__":
    app.run(debug=True)