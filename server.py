from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import app, User
from flask import jsonify, request
from crud.user_crud import get_all_users, get_user, create_user, update_user, destroy_user

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flasql'
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

# Get/Post routes
@app.route('/users', methods=['GET', 'POST'])
def user_index_create():
    if request.method == 'GET':
        return get_all_users()
    if request.method == 'POST':
        return create_user(name=request.form['name'], email=request.form['email'])

# Get, put, and delete routes
@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def user_show_put_delete(id):
    if request.method == 'GET':
        return get_user(id)
    if request.method == 'PUT':
        return update_user(id, name=request.form[name], email=request.form[email])
    if request.method == 'DELETE':
        return destroy_user(id)





