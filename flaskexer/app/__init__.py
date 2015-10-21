from flask import Flask
from flask import g

from modules.math import math
from modules import math_two
from modules import default
from modules import posts

from pymongo import MongoClient

app = Flask(__name__)

def get_main_collection():
    client = MongoClient('mongodb://localhost:27017/')
    collect = client.postsdb.posts
    return collect

def get_user_collection():
    client = MongoClient('mongodb://localhost:27017/')
    collect = client.postsdb.users
    return collect

@app.before_request
def before_request():
    postConn = get_main_collection()
    userConn = get_user_collection()
    g.postsdb = posts.PostDB(conn=postConn)
    g.usersdb = posts.UserDB(conn=userConn)

@app.teardown_request
def teardown_request(exception):
    postdb = getattr(g, 'postdb', None)
    if postdb is not None:
        postdb.close()

app.register_blueprint(math.mod, url_prefix="/math")
app.register_blueprint(math_two.mod_two)
app.register_blueprint(default.mod)
app.register_blueprint(posts.mod, url_prefix="/posts")