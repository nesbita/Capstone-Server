from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flasql'
db = SQLAlchemy(app)

'''
association_table = Table('association', Base.metadata,
    Column('left_id', ForeignKey('left.id')),
    Column('right_id', ForeignKey('right.id'))
)

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Child",
                    secondary=association_table)

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
'''
association_table = Table('association', db.Model.metadata,
    Column('users_id', ForeignKey('users.id'), primary_key=True),
    Column('products_id', ForeignKey('products.id'), primary_key=True)
)
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    products = relationship('Products',
                    secondary=association_table, back_populates='users')


    # products = db.relationship('Products', back_populates='user', lazy=True)
    # products = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))

    def __repr__(self):
        return f'User(id={self.id}, email="{self.email}", name="{self.name}")'
    
    # def as_dict(self):
    #     return {
    #         id: self.id,
    #         name: self.name,
    #         email: self.email,
    #     }
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    users = relationship('User',
                    secondary=association_table, back_populates='products')
    
    
    
    # user = db.relationship('User', back_populates='products', lazy='subquery')
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))

    def __repr__(self):
        return f'Products("id={self.id}", "name={self.name}", "price={self.price}", "description={self.description}", "img={self.img}")'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}