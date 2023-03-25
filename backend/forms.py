# Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import Length, DataRequired,NumberRange


class WordForm(FlaskForm):
    word = StringField(label='Word', validators=[DataRequired(), Length(min=1)])


class LivesForm(FlaskForm):
    lives = IntegerField(label='Lives', validators=[DataRequired(), NumberRange(min=1)])
