from flask import jsonify, redirect 
from models import db, User

# Get all users
def get_all_users():
    all_users = User.query.all()
    results = [user.as_dict() for user in all_users] 
    return jsonify(results)

# Get user by id
def get_user(id):
    user = User.query.get(id)
    if user:
      return jsonify(user.as_dict())
    else:
      raise Exception('Error getting user at {}'.format(id))

# Create new user
def create_user(name, email):
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.as_dict())

# Update user
def update_user(id, name, email):
    user = User.query.get(id)
    if user:
        user.name = name or user.name
        user.email = email or user.email
        db.session.commit()
        return jsonify(user.as_dict())
    else:
        raise Exception('No User at id {}'.format(id))

# Delete user 
def destroy_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect('/users')
    else:
        raise Exception('No User at id {}'.format(id))