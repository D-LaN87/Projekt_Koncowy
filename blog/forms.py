# blog/forms.py

from werkzeug.routing import ValidationError
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, PasswordField
from wtforms.validators import DataRequired
from config import Config


def validate_username(field):
    if field.data != Config.ADMIN_USERNAME:
        raise ValidationError("Invalid username")
    return field.data


def validate_password(field):
    if field.data != Config.ADMIN_PASSWORD:
        raise ValidationError("Invalid password")
    return field.data


class LoginForm(FlaskForm):

   username = StringField('Username', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])


class EntryForm(FlaskForm):
   title = StringField('Title', validators=[DataRequired()])
   body = TextAreaField('Content', validators=[DataRequired()])
   is_published = BooleanField('Is Published?')