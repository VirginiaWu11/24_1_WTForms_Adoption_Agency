from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField,  SelectField
from wtforms.validators import InputRequired, Optional, NumberRange,URL

class PetForm(FlaskForm):
    """WTForm to add/edit pets"""
    name = StringField("Pet name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat','cat'),('dog','dog'),('porcupine','porcupine')] , validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(),URL()])
    age = IntegerField("Age", validators=[Optional(),NumberRange(min=0,max=30)])
    notes = StringField("Notes", validators=[Optional()])


