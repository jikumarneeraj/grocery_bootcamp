from app import app
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(32),unique=True,nullable=False)
    passhash=db.Column(db.String(128), nullable=False)
    name=db.Column(db.String(32), nullable=True)
    is_admin=db.Column(db.Boolean, nullable=False, default=False)

class Category(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(32), unique=True)
    product=db.relationship('Product',backref='category',lazy=True)

class Product(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(32), unique=False)
    unit=db.Column(db.String(32), nullable=False)
    price_per_unit=db.Column(db.Float, nullable=False)
    category_id=db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    man_date=db.Column(db.Date, nullable=False)
    cart=db.relationship('Cart',backref='product',lazy=True)
    order=db.relationship('Order', backref='product', lazy=True)

class Cart(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id=db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity=db.Column(db.Integer, nullable=False)

class Transaction(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    datetime=db.Column(db.DateTime, nullable=False)
    order=db.relationship('Order', backref='transaction', lazy=True)
    
class Order(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    transaction_id=db.Column(db.Integer, db.ForeignKey('transaction.id'), nullable=False)
    product_id=db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity=db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()