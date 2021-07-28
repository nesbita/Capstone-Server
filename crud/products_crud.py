from flask import jsonify, redirect 
from models import db, Products

# Get all products
def get_all_products():
    all_products = Products.query.all()
    results = [products.as_dict() for products in all_products] 
    return jsonify(results)

# Get products by id
def get_products(id):
    products = Products.query.get(id)
    if products:
      return jsonify(products)
    else:
      raise Exception('Error getting products at {}'.format(id))

# Create new products
def create_products(id):
    new_products = Products(id=id)
    db.session.add(new_products)
    db.session.commit()
    return jsonify(new_products)

# Update products
def update_products(id):
    user = Products.query.get(id)
    if products:
        products.id = id or products.id
        db.session.commit()
        return jsonify(products)
    else:
        raise Exception('No Products at id {}'.format(id))

# Delete products
def destroy_products(id):
    products = Products.query.get(id)
    if products:
        db.session.delete(products)
        db.session.commit()
        return redirect('/products')
    else:
        raise Exception('No Products at id {}'.format(id))