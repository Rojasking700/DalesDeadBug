from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email
from datetime import date

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
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField()


class CreateAPlan(FlaskForm):

        service_name = StringField('Service Name')
        service_date = StringField('Date')
        price = IntegerField('Price')
        description = TextAreaField('Description')
        url = StringField('Img URL')
        sale = BooleanField('Leave empty if service is not on sale')
        submit = SubmitField()

