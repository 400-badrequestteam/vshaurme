from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp
from vshaurme.vshaurme_validators.validate_password import is_password_valid
from vshaurme.vshaurme_validators.validate_username_for_obscene import is_username_obscene

from vshaurme.models import User


class LoginForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Length(1, 254), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember me'))
    submit = SubmitField(_l('Log in'))


class RegisterForm(FlaskForm):
    name = StringField(_l('Name'), validators=[DataRequired(), Length(1, 30)])
    email = StringField(_l('Email'), validators=[DataRequired(), Length(1, 254), Email()])
    username = StringField(_l('Username'), validators=[DataRequired(), is_username_obscene, Length(1, 20),
                                                   Regexp('^[a-zA-Z0-9]*$',
                                                          message=_l('The username should contain only a-z, A-Z and 0-9.')),
                                                          ])
    password = PasswordField(_l('Password'), validators=[
        DataRequired(), is_password_valid, EqualTo('password2')])
    password2 = PasswordField(_l('Confirm password'), validators=[DataRequired()])
    submit = SubmitField(_l('Register'))

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError(_l('The email is already in use.'))

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(_l('The username is already in use.'))


class ForgetPasswordForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Length(1, 254), Email()])
    submit = SubmitField(_l('Remind'))


class ResetPasswordForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Length(1, 254), Email()])
    password = PasswordField(_l('Password'), validators=[
        DataRequired(), is_password_valid, EqualTo('password2')])
    password2 = PasswordField(_l('Confirm password'), validators=[DataRequired()])
    submit = SubmitField(_l('Reset'))
