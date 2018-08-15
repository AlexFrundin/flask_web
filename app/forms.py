from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField,SubmitField,PasswordField, SelectField
from wtforms.validators import IPAddress, DataRequired, EqualTo, ValidationError
from .models import User, Pet, Types
from flask import flash

class LoginForm(FlaskForm):
    name = StringField('login', validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    remember = BooleanField('запомнить меня')
    submit = SubmitField("Вход")

class RegistrationForm(FlaskForm):
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Ok')
    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

class PetForm(FlaskForm):

    all = tuple([item.type for item in Types.query.all()])
    print(all)
    name = StringField('name pet', validators=[DataRequired()])
    type = SelectField('type pet', choices=[(name,name) for name in all])
    submit = SubmitField('ok')
