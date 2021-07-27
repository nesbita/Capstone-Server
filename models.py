from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flasql'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)

    products = db.relationship('Products', backref='user', lazy=True)

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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))

    def __repr__(self):
        return f'Products("id={self.id}")'
