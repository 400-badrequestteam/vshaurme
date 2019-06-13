from flask_wtf import FlaskForm
from flask_babel import lazy_gettext
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp
from vshaurme.vshaurme_validators.validate_password import is_password_valid
from vshaurme.vshaurme_validators.validate_username_for_obscene import is_username_obscene

from vshaurme.models import User


class LoginForm(FlaskForm):
    email = StringField(lazy_gettext('Email'), validators=[DataRequired(), Length(1, 254), Email()])
    password = PasswordField(lazy_gettext('Password'), validators=[DataRequired()])
    remember_me = BooleanField(lazy_gettext('Remember me'))
    submit = SubmitField(lazy_gettext('Log in'))


class RegisterForm(FlaskForm):
    name = StringField(lazy_gettext('Name'), validators=[DataRequired(), Length(1, 30)])
    email = StringField(lazy_gettext('Email'), validators=[DataRequired(), Length(1, 254), Email()])
    username = StringField(lazy_gettext('Username'), validators=[DataRequired(), is_username_obscene, Length(1, 20),
                                                   Regexp('^[a-zA-Z0-9]*$',
                                                          message=lazy_gettext('The username should contain only a-z, A-Z and 0-9.')),
                                                          ])
    password = PasswordField(lazy_gettext('Password'), validators=[
        DataRequired(), is_password_valid, EqualTo('password2')])
    password2 = PasswordField(lazy_gettext('Confirm password'), validators=[DataRequired()])
    submit = SubmitField(lazy_gettext('Register'))

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError(lazy_gettext('The email is already in use.'))

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(lazy_gettext('The username is already in use.'))


class ForgetPasswordForm(FlaskForm):
    email = StringField(lazy_gettext('Email'), validators=[DataRequired(), Length(1, 254), Email()])
    submit = SubmitField(lazy_gettext('Remind'))


class ResetPasswordForm(FlaskForm):
    email = StringField(lazy_gettext('Email'), validators=[DataRequired(), Length(1, 254), Email()])
    password = PasswordField(lazy_gettext('Password'), validators=[
        DataRequired(), is_password_valid, EqualTo('password2')])
    password2 = PasswordField(lazy_gettext('Confirm password'), validators=[DataRequired()])
    submit = SubmitField(lazy_gettext('Reset'))
