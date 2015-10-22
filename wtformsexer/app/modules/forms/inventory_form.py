from wtforms import Form
from wtforms import TextField
from wtforms import DecimalField
from wtforms import validators

class InventoryForm(Form):
    itemname = TextField('Name', [validators.Length(min=2, max=25)])
    price = DecimalField('Price', [validators.NumberRange(min=0.0)], places=2, rounding=None)