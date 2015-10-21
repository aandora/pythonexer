from flask import Blueprint
from flask import render_template
from flask import session
from flask import redirect
from flask import request
from flask import g
from flask import flash
from flask import url_for
from functools import wraps

mod = Blueprint('default', __name__)

number_list = range(1,6)

itemlist = {'Ball': 0, 'Pen': 0, 'Glass': 0, 'Car': 0}
itemprice = {'Ball': 1.0, 'Pen': 2.0, 'Glass': 3.0, 'Car': 4.0}
itemsubtotal = {'Ball': 0, 'Pen': 0, 'Glass': 0, 'Car': 0}

class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

person_list = [Person('Ruth', 24, 'F'), Person('Pat', 25, 'M'), Person('Andrew', 22, 'M'), Person('Mieden', 25, 'M')]

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
    return render_template('default/index.html')

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

@mod.route('/signup', methods=['GET'])
def signup_page():
    if 'username' in session:
        return redirect('/')
    return render_template('default/signup.html')

@mod.route('/signup', methods=['POST'])
def signup_submit():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    if password != confirm_password:
        flash('Password did not match.', 'signup_failure')
        return redirect(url_for('.signup_page'))
    elif g.usersdb.getUser(username).count() > 0:
        flash('Username already exists.', 'signup_failure')
        return redirect(url_for('.signup_page'))
    session['username'] = username
    g.usersdb.createUser(username, password)
    return redirect('/')

@mod.route('/element')
def element():
    return render_template('default/index.html')

@mod.route('/for_block')
def for_block():
    return render_template('default/for_block.html', numbers=number_list)

@mod.route('/if_block')
def if_block():
    return render_template('default/if_block.html', numbers=number_list)

@mod.route('/object_element')
def object_element():
    return render_template('default/object_element.html', person_list=person_list)

@mod.route('/macros_ref')
def macros_ref():
    return render_template('default/macros_ref.html', person_list=person_list)

@mod.route('/exercise')
def exercise():
    with request:
        newitem = request.args.get('item')
        if newitem is None:
            for key in itemlist.keys():
                itemlist[key] = 0
                itemsubtotal[key] = 0
            return render_template('default/exer.html', items=itemlist, prices=itemprice, subtotals=itemsubtotal)
        else:
            itemlist[newitem] += 1
            itemsubtotal[newitem] += itemprice[newitem]
            return render_template('default/exer.html', items=itemlist, prices=itemprice, subtotals=itemsubtotal)
