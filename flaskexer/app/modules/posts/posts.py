from flask import Blueprint
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

mod = Blueprint('posts', __name__)

@mod.route('/')
def post_list():
    posts = g.postsdb.getPosts('a')
    return render_template('posts/post.html', posts=posts)

@mod.route('/', methods=['POST'])
def create_post():
    new_post = request.form['new_post']
    g.postsdb.createPost('a', new_post)
    flash('New post created!', 'create_post_success')
    return redirect(url_for('.post_list'))