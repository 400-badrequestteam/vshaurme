from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Optional, Length
from flask_babel import lazy_gettext


class DescriptionForm(FlaskForm):
    description = TextAreaField(lazy_gettext('Description'), validators=[Optional(), Length(0, 500)])
    submit = SubmitField(lazy_gettext('Add'))


class TagForm(FlaskForm):
    tag = StringField(lazy_gettext('Add Tag (use space to separate)'), validators=[Optional(), Length(0, 64)])
    submit = SubmitField(lazy_gettext('Add'))


class CommentForm(FlaskForm):
    body = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField(lazy_gettext('Add'))
