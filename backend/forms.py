# Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length, DataRequired


class WordForm(FlaskForm):
    word = StringField(label='Word', validators=[DataRequired(), Length(min=1)])
