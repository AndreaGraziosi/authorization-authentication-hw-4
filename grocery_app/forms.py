from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import ItemCategory, GroceryStore, GroceryItem

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

  
    title = StringField("Store Title", validators=[DataRequired(), Length(min=3, max=80)])
    address = StringField("Store Address", validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField('Submit')
    

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=80)])
    price = FloatField("Price", validators=[DataRequired()])
    category = SelectField('Categoty', choices=ItemCategory.choices())
    photo_url = StringField('Photo URL', validators=[DataRequired(), Length(min=3, max=80)])
    store = QuerySelectField ('Store', query_factory=lambda: GroceryStore.query, allow_blank=False)
    submit = SubmitField('Submit')
    
