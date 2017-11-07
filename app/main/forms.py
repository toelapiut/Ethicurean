from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
     bio=TextAreaField('Tell us about you',validators=[Required()])
     submit=SubmitField('submit')

class Bloger(FlaskForm):
    title=StringField('Blog Title',validators=[Required()])
    blog=TextAreaField('Type in your Story',validators=[Required()])
    submit=SubmitField('submit')

class Comments(FlaskForm):
    comments=TextAreaField('Your Idea??',validators=[Required()])
    submit=SubmitField('submit')