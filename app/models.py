from app import login, db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# User Registration to be used for the form


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False, unique=False)
    phone = db.Column(db.String(150), nullable=False, unique=False)
    address = db.Column(db.String(150), nullable=False, unique=False)
    city = db.Column(db.String(150), nullable=False, unique=False)
    zipcode = db.Column(db.String(150), nullable=False, unique=False)
    # Ignore this during user registration
    Admin = db.Column(db.Boolean, default=False, nullable=False)
    cart = db.relationship('Cart', backref='customer')

    def __init__(self, username, email, password, phone, address, city, zipcode, Admin=False):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.phone = phone
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.Admin = Admin


class Plans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(150), nullable=False, unique=True)
    service_date = db.Column(db.String(150), nullable=False, unique=True)
    price = db.Column(db.Integer)
    description = db.Column(db.String(256), nullable=False, unique=False)
    url = db.Column(db.String(150), nullable=False, unique=False)
    sale = db.Column(db.Boolean)
    cart = db.relationship('Cart', backref='plan')

    def __init__(self, service_name, service_date, price, description, url, sale=False):
        self.service_name = service_name
        self.service_date = service_date
        self.price = price
        self.description = description
        self.url = url
        self.sale = sale
        

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(
        db.Integer, db.ForeignKey('plans.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, service_id, user_id):
        self.service_id = service_id
        self.user_id = user_id