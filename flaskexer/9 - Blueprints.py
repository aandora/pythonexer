from flask import request, render_template
from flask import session
from flask import redirect
from functools import wraps
import logging
# from flask import url_for 

from app import app

app.config.from_object('config.Config')

# Setup Logging
formatter = logging.Formatter(app.config.get('LOG_FORMAT'))
fh = logging.FileHandler(filename=app.config.get('LOG_FILE'))
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
app.logger.addHandler(fh)

app.secret_key = 'This is an unspeakable secret.'

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            return func(*args, **kwargs)
        else:
            return redirect('error')
    return wrapper

@app.route("/login", methods=['POST'])
def login():
    session['username'] = 'Ali'
    return 'User is now logged in.'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/error')
def error():
    return 'User is not logged in!'

@app.route("/")
def Welcome():
    return 'Welcome!'

@app.route("/<username>")
@login_required
def welcome_user(username):
    return 'Welcome ' + username + '!'

@app.route('/with_int/<int:number>')
@login_required
def show_number(number):
    return 'We\'re counting with number '+ str(number) +'!'

@app.route('/methods', methods=['GET', 'POST'])
@login_required
def methods():
    if request.method == 'POST':
        return 'In here via POST request.'
    else:
        return 'In here via GET request.'

@app.route('/log_sample')
def log_sample():
    app.logger.info('Sample log entry!')
    return 'Log sample printed out!'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def application_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    # with app.test_request_context():
    #     print url_for('welcome_user', username='Sarah Connor')
    app.run(debug=True)