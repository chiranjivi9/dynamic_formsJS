from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class fireput(Form):
    champs = StringField('Data here')
    emails = StringField('emails')
