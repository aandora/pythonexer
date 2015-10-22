from flask import Flask
from flask import g

from modules import default
from modules import users

from pymongo import MongoClient

app = Flask(__name__)

def get_main_db():
    client = MongoClient('mongodb://localhost:27017/')
    maindb = client.postsdb
    return maindb

@app.before_request
def before_request():
    mainDb = get_main_db()
    g.usersdb = users.UserDB(conn=mainDb.users)
    
@app.teardown_request
def teardown_request(exception):
    postdb = getattr(g, 'postdb', None)
    if postdb is not None:
        postdb.close()
    userdb = getattr(g, 'userdb', None)
    if userdb is not None:
        userdb.close()

app.register_blueprint(default.mod)