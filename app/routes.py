from app import app, db, Mail, Message
from flask import render_template, request, flash, redirect, url_for
from app.forms import UserInfoForm, LoginForm
from app.models import User, Plans
from flask_login import login_user, logout_user, login_required,current_user
from werkzeug.security import check_password_hash

ddb = "Dale's Dead Bugs | "

@app.route('/')
@app.route('/index')
def index():
    title = ddb + 'HOME'

    return render_template('index.html', title=title)

# @app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    title = ddb + "register"
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
        # msg.body = 'Thank you for signing up for the most glorious death of your bugs. I hope you enjoy your new carnage!'
        msg.html = "<p>Thanks you so much for signing up for the Dale's Dead Bugs service. Where we do buggin right! We may, or may not, be in Liberia!</p>"

        # Mail.send(msg)  error occurs saying that send needs a postional argument dont know why

        flash("It may be a crack in your internet, or the Chinese are making their move!", "success")
        return redirect(url_for('index'))
    return render_template('register.html', title=title, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    title = "Kekambas Blog | LOGIN"
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user is None or not check_password_hash(user.password, password):
            flash("Incorrect Email/Password. Please try again", 'danger')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        flash("You have successfully logged in!", 'success')
        next_page = request.args.get('next')
        if next_page:
            return redirect(url_for(next_page.lstrip('/')))
        return redirect(url_for('index'))

    return render_template('login.html', title=title, form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You have succesfully logged out", 'primary')
    return redirect(url_for('index'))

@app.route('/login', methods=['GET','POST'])
def login():
    title = ddb + 'login'
    
    form = LoginForm()
    
    if request.method == 'POST' and form.validate():

        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user is None or not check_password_hash(user.password, password):
            flask("Incorrect Username or Password. Please try again")
            return redirect(url_for('index'))

        login_user(user,remember=form.remember_me.data)
        flash(f"Welcome back {username}!")
        next_page = request.args.get('next')
        if next_page:
            return redirect(url_for(next_page.lstrip('/')))

        return redirect(url_for('index'))

    return render_template('login.html',title=title, form=form)

@app.route('/myinfo')
@login_required
def myinfo():
    title = ddb + 'My Info'
    return render_template('myinfo.html', title = title)


@app.route('/shoppingCart', methods=["GET", "POST"])
@login_required
def shoppingCart():
    title = ddb + 'My Cart'
    return render_template('shoppingCart.html',title=title)

