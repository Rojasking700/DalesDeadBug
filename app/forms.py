from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email


class UserInfoForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    phone = StringField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    zipcode = StringField('ZipCode', validators=[DataRequired()])
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField()

