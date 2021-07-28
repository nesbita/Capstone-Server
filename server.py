from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import app, User, Products
from flask import jsonify, request
from crud.user_crud import get_all_users, get_user, create_user, update_user, destroy_user
from crud.products_crud import get_all_products, get_products, create_products, update_products, destroy_products

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flasql'
CORS(app)
db = SQLAlchemy(app)


@app.route('/')
def home():
  first_user = User.query.first()
  print(f'🎀 {first_user}')
  return jsonify(user=first_user.as_dict())

# def home():
#     first_user = []
#     return jsonify(user=first_user.as_dict() if first_user else 'No users!')
    
    # return '<h1>This is my home route.</h1>'

# Get/Post routes for users
@app.route('/users', methods=['GET', 'POST'])
def user_index_create():
    if request.method == 'GET':
        return get_all_users()
    if request.method == 'POST':
        return create_user(name=request.form['name'], email=request.form['email'])

# Get, put, and delete routes for users
@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def user_show_put_delete(id):
    if request.method == 'GET':
        return get_user(id)
    if request.method == 'PUT':
        return update_user(id, name=request.form[name], email=request.form[email])
    if request.method == 'DELETE':
        return destroy_user(id)

# Get/Post routes for products
@app.route('/products', methods=['GET', 'POST'])
def products_index_create():
    if request.method == 'GET':
        return get_all_products()
    if request.method == 'POST':
        return create_products(id)

# Get, put, and delete routes for products
@app.route('/products/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def products_show_put_delete(id):
    if request.method == 'GET':
        return get_products(id)
    if request.method == 'PUT':
        return update_products(id)
    if request.method == 'DELETE':
        return destroy_products(id)





