from flask import Flask, jsonify, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Security Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///secure_app.db'
app.config['JWT_SECRET_KEY'] = (
    'super-secret-key-change-this'  # In production, use environment variables!
)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


# User Model (Secure Data Storage)
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password_hash = db.Column(db.String(120), nullable=False)


with app.app_context():
  db.create_all()


# Home Route
@app.route('/')
def home():
  return jsonify(
      {
          'message': 'Welcome to Project 5: Secure Web Application API',
          'status': 'Online',
      }
  )


# Route 1: User Registration (Secure Hashing + SQL Injection Prevention)
@app.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  username = data.get('username')
  password = data.get('password')

  if not username or not password:
    return jsonify({'error': 'Missing username or password'}), 400

  existing_user = User.query.filter_by(username=username).first()
  if existing_user:
    return jsonify({'error': 'Username already exists'}), 409

  # Hash password securely using Bcrypt
  hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

  # SQLAlchemy ORM automatically prevents SQL Injection
  new_user = User(username=username, password_hash=hashed_password)
  db.session.add(new_user)
  db.session.commit()

  return jsonify({'message': f'User {username} registered successfully!'}), 201


# Route 2: User Login (Authentication & Token Generation)
@app.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  username = data.get('username')
  password = data.get('password')

  user = User.query.filter_by(username=username).first()

  if user and bcrypt.check_password_hash(user.password_hash, password):
    # Generate JWT token for authorization
    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200

  return jsonify({'error': 'Invalid credentials'}), 401


# Route 3: Protected Dashboard (Requires Valid JWT Authorization)
@app.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
  current_user = get_jwt_identity()
  return jsonify({
      'message': f'Welcome to the secure dashboard, {current_user}!',
      'status': 'Authorized',
  })


if __name__ == '__main__':
  app.run(debug=True, port=5000)