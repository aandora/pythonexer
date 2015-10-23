from flask import Blueprint
from flask import jsonify
from flask import request

mod = Blueprint('api', __name__)

sample_data = [
        {'author':'Ali', 'post':'Lorem ipsum'},
        {'author':'Ruth', 'post':'Dolor sit amet'},
        {'author':'Andrew', 'post':'Consectetur Adipiscing Elit'},
    ]

@mod.route('/getsampledata', methods=['GET','POST'])
def get_sample_data():
    print request.form.keys()
    if request.method=='POST':
        sample_data.append({
            'author':request.form['author'], 
            'post':request.form['post'], 
        })
    return jsonify(posts=sample_data)

#====================

product_list = [{'name': 'Apple', 'price': 1.25}]
cart_list = []
total = 0;

def get_sum():
    total = 0
    for item in cart_list:
        total += item['subtotal']
    return total

@mod.route('/add_product', methods=['POST'])
def add_product():
    product_list.append({
        'name': request.form['item_name'], 
        'price': request.form['item_price']
    })
    return jsonify(items=product_list)

@mod.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    price = request.form['item_price']
    qty = request.form['item_qty']
    subttl = float(price)*int(qty)
    cart_list.append({
        'name':request.form['item_name'],
        'price':price,
        'quantity':qty,
        'subtotal':subttl
    });
    total = get_sum();
    return jsonify(items=cart_list, total=get_sum())

@mod.route('/display_orders', methods=['GET'])
def display_orders():
    return jsonify(items=cart_list, total=get_sum())

@mod.route('/get_products', methods=['GET'])
def get_products():
    return jsonify(items=product_list)



