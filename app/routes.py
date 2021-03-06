from app import app, db, Mail, Message
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
@app.route('/register', methods=['GET', 'POST'])
def register():
    title = "Dale's Dead Bugs Service | register"
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data 
        phone = form.phone.data
        address = form.address.data
        city = form.city.data
        zipcode = form.zipcode.data
        # admin = form.admin.data
        # print(username, email, password)

        # create new instance of User
        new_user = User(username, email, password, phone, address, city, zipcode)
        # add new instance to our database
        db.session.add(new_user)
        # commit database
        db.session.commit()

        # send email to new user
        msg = Message(f"Welcome, {username}", [email])
        msg.body = 'Thank you for signing up for the most glorious death of your bugs. I hope you enjoy your new carnage!'
        msg.html = "<p>Thanks you so much for signing up for the Dale's Dead Bugs service. Where we do buggin right! We may, or may not, be in Liberia!</p>"

        Mail.send(msg)

        flash("It may be a crack in your internet, or the Chinese are making their move!", "success")
        return redirect(url_for('index'))
    return render_template('register.html', title=title, form=form)



# @app.route('/shoppingCart', methods=["GET", "POST"])
# @login_required
# def shoppingCart():
    
#     return render_template('shoppingCart.html')