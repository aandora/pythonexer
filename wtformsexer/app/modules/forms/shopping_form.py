from wtforms import Form
from wtforms import DecimalField

class ShoppingForm(Form):

	prodductfields = {}
	
	def __init__(self, products):
		super(Form, self).__init__()
		self.products = products
		for key in self.products.keys():
			prodductfields[key] = DecimalField(key+' '+str(products[key]), [validators.NumberRange(min=0.0)], places=2, rounding=None)
