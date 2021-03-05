from app import app, db
from flask import render_template, request, flash, redirect, url_for
from app.forms import UserInfoForm
from app.models import User, Plans
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

@app.route('/')
@app.route('/index')
def index():
    title = "Dales Dead Bug "

    return render_template('index.html', title=title)

# @app.route('/')

# @app.route('/shoppingCart', methods=["GET", "POST"])
# @login_required
# def shoppingCart():
    
#     return render_template('shoppingCart.html')