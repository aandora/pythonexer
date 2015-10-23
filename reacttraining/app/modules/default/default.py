from flask import Blueprint
from flask import render_template
from flask import session
from flask import redirect
from flask import request
from flask import g
from flask import flash
from flask import url_for

mod = Blueprint('default', __name__)

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

# Routing list for React examples

@mod.route('/')
def one():
    return render_template('default/one.html')

@mod.route('/two')
def two():
    return render_template('default/two.html')

@mod.route('/three')
def three():
    return render_template('default/three.html')

@mod.route('/four')
def four():
    return render_template('default/four.html')

@mod.route('/five')
def five():
    return render_template('default/five.html')

@mod.route('/six')
def six():
    return render_template('default/six.html')

@mod.route('/seven')
def seven():
    return render_template('default/seven.html')

@mod.route('/eight')
def eight():
    return render_template('default/eight.html')

#=================

@mod.route('/shopping')
def shopping():
    return render_template('default/shopping.html');

