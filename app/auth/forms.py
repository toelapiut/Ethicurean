from ..models import User
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo

class RegistrationForm(FlaskForm):
    email=StringField('Your Email Address',validators=[Required(),Email()])
    username=StringField('Enter your username',Validators=[Required()])
    password=PasswordField('Password',validators=[Required(),
    EqualTo('password_confirm',message='password must match')])
    password_confirm=PasswordField('Confirm Password',validators=[Required()])
    Submit=SubmitField('Sign Up')

    def validators_email(self,data_field):
        if user.query.filter_by(email=data_field.data).first():
            raise ValidationError('An Account has been created by that email')

    def validators_username(self,data_field):
        if User.query.filter_by(username=data_field).first():
            raise ValidationError("The username is Taken")


class LoginForm(FlaskForm):
    email=StringField('Your Email Address',valdators=[Required(),Email()])
    password=PasswordField('Password',validators=[Required()])
    remember=BooleanField('Remember')
    submit=SubmitField('Log In')
