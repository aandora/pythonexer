from datetime import datetime
from flask import Blueprint
from flask import render_template
from flask import session
from flask import redirect
from flask import request
from flask import g
from flask import flash
from ..forms import reg_form
from ..forms import inventory_form
from ..forms import shopping_form
from ..models import user as UserRef
from functools import wraps

mod = Blueprint('default', __name__)

productlist = {}

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect('/login')
        else:
            return func(*args, **kwargs)
    return wrapper 

@mod.route('/')
def index():
    if 'username' not in session:
        return redirect('/login')
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('default/index.html', server_time=current_time)

@mod.route('/login', methods=['GET'])
def login_page():
    if 'username' in session:
        return redirect('/')
    return render_template('default/login.html')

@mod.route('/login', methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']
    if g.usersdb.getUserWithPassword(username, password).count() > 0:
        session['username'] = username
        return redirect('/')
    else:
        flash('Invalid username and password.', 'signin_failure')
        return redirect('/login') 

@mod.route('/logout', methods=['GET'])
def logout_submit():
    session.pop('username', None)
    session.clear()
    return redirect('/')

@mod.route('/register', methods=['GET', 'POST'])
def register():
    form = reg_form.RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = UserRef.User(form.username.data, form.email.data,
                    form.password.data)
        g.usersdb.createUserUsingUser(user)
        session['username'] = form.username.data
        return redirect('/')
    return render_template('default/signup.html', form=form)

@mod.route('/shopping', methods=['GET', 'POST'])
def shopping():
    def redirect_to_home(**kwargs):
        return render_template('default/shopping.html', **kwargs)

    inventoryform = inventory_form.InventoryForm(request.form)
    productform = shopping_form.ShoppingForm(productlist)
    
    if request.method == 'POST':
        if request.form['btn'] == 'Add Item':
            if inventoryform.validate():
                productlist[inventoryform.itemname.data] = inventoryform.price.data
                return redirect_to_home(inventoryform = inventoryform, products=productlist, productform=productform)
            else:
                return redirect_to_home(inventoryform = inventoryform, products=productlist, productform=productform)
        else:
            return redirect_to_home(inventoryform = inventoryform, products=productlist, productform=productform)
    else:
        return redirect_to_home(inventoryform = inventoryform, products=productlist, productform=productform)
