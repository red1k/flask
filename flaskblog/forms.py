from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        # raise error when username is already taken
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken, change it bitch!')

    def validate_email(self, email):
        # raise error when email is already taken
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is taken, change it bitch!')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
