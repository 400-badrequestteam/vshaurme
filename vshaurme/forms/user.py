from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_babel import lazy_gettext
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, HiddenField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, Regexp
from vshaurme.vshaurme_validators.validate_password import is_password_valid
from vshaurme.vshaurme_validators.validate_username_for_obscene import is_username_obscene

from vshaurme.models import User


class EditProfileForm(FlaskForm):
    name = StringField(lazy_gettext('Name'), validators=[DataRequired(), Length(1, 30)])
    username = StringField(lazy_gettext('Username'), validators=[DataRequired(), Length(1, 20),
                                                   Regexp('^[a-zA-Z0-9]*$',
                                                          message='{} a-z, A-Z {} 0-9.'.format(
                                                              lazy_gettext('The username should contain only'),
                                                              lazy_gettext('and'))),
                                                          is_username_obscene])
    website = StringField(lazy_gettext('Website'), validators=[Optional(), Length(0, 255)])
    location = StringField(lazy_gettext('City'), validators=[Optional(), Length(0, 50)])
    bio = TextAreaField(lazy_gettext('Bio'), validators=[Optional(), Length(0, 120)])
    submit = SubmitField(lazy_gettext('Apply'))

    def validate_username(self, field):
        if field.data != current_user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError(lazy_gettext('The username is already in use.'))


class UploadAvatarForm(FlaskForm):
    image = FileField(lazy_gettext('Upload'), validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], '{} .jpg {} .png.'.format(
            lazy_gettext('The file format should be'),
            lazy_gettext('or')))
    ])
    submit = SubmitField(lazy_gettext('Upload'))


class CropAvatarForm(FlaskForm):
    x = HiddenField()
    y = HiddenField()
    w = HiddenField()
    h = HiddenField()
    submit = SubmitField(lazy_gettext('Crop and Update'))


class ChangeEmailForm(FlaskForm):
    email = StringField(lazy_gettext('New Email'), validators=[DataRequired(), Length(1, 254), Email()])
    submit = SubmitField(lazy_gettext('Change'))

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError(lazy_gettext('The email is already in use.'))


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(lazy_gettext('Old Password'), validators=[DataRequired()])
    password = PasswordField(lazy_gettext('New Password'), validators=[
        DataRequired(), is_password_valid, EqualTo('password2')])
    password2 = PasswordField(lazy_gettext('Confirm Password'), validators=[DataRequired()])
    submit = SubmitField(lazy_gettext('Change'))


class NotificationSettingForm(FlaskForm):
    receive_comment_notification = BooleanField(lazy_gettext('New comment'))
    receive_follow_notification = BooleanField(lazy_gettext('New follower'))
    receive_collect_notification = BooleanField(lazy_gettext('New collector'))
    submit = SubmitField(lazy_gettext('Apply'))


class PrivacySettingForm(FlaskForm):
    public_collections = BooleanField(lazy_gettext('Public my collection'))
    submit = SubmitField(lazy_gettext('Apply'))


class DeleteAccountForm(FlaskForm):
    username = StringField(lazy_gettext('Username'), validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField(lazy_gettext('Delete'))

    def validate_username(self, field):
        if field.data != current_user.username:
            raise ValidationError(lazy_gettext('Wrong username.'))
