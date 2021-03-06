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


# @app.route('/shoppingCart', methods=["GET", "POST"])
# @login_required
# def shoppingCart():
#     ### Pull information about what has been added to the cart


#     ### Confirm shopping cart purchase of plan


#     ### Create a modello for paying for the plan.  This is a sham popup.
#         return
#     return render_template('shoppingCart.html', title="DDB | Cart")