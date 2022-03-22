from wtforms.validators import DataRequired, Email
from flask import Flask
from wtforms import SubmitField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField,TextAreaField, IntegerField,DecimalField,SelectField
from werkzeug.utils import secure_filename

class PropForm(FlaskForm):
    ptitle = StringField("Property Title", validators=[DataRequired()],name = "Property Title")
    desc = TextAreaField("Description", validators=[DataRequired()],name="Description")
    rooms = IntegerField("Number of Rooms", validators=[DataRequired()],name="Number of Rooms")
    brooms = IntegerField("Number of Bathrooms", validators=[DataRequired()],name="Number of Bathrooms")
    price = DecimalField("Price", validators=[DataRequired()],name="Price",places = 2)
    ptypes = ["House","Mansion","Apartment","Open lot","Commercial"]
    ptype = SelectField("Type", validators=[DataRequired()],name = "Poperty type",choices=ptypes)
    locat = StringField("Location", validators=[DataRequired()],name = "Location")
    photo = FileField(validators=[FileRequired(), FileAllowed(['png', 'jpg','jpeg'], "wrong format!")])
    submit = SubmitField('Upload')