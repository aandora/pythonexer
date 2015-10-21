from datetime import datetime
from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import g
from flask import request
from flask import url_for
from flask import sessions

mod = Blueprint('default', __name__)

@mod.route('/')
def index():
	if 'username' in sessions:
		redirect('/posts')
	else:
    	current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    	return render_template('default/index.html', server_time=current_time)

@mod.route('/login', methods=['GET'])
def login_page():
    return render_template('default/login.html')

@mod.route('/signup', methods=['GET'])
def signup_page():
	return render_template('default/signup.html')

@mod.route('/login', methods=['POST'])
def login_submit():
	u = request.form['username']
	p = request.form['password']
    return redirect('/')

@mod.route('/signup', methods=['POST'])
def signup_submit():
	u = request.form['username']
	p = request.form['password']
	if g.usersdb.doesUserExist(u):
		return redirect('/signup')
	else:
		g.usersdb.createUser(u, p)
		sessions['username'] = u
    	return redirect('/')