from flask import Flask
app = Flask(__name__)

from markupsafe import escape

@app.route('/')
def root():
    return 'Flask server is running' 

@app.route('/user/<username>')
def show_user(username):
    return 'Username is %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'post id  is %d' % post_id

@app.route('/path/<path:subpath>')
def show_path(subpath):
    return '<h1>sub path</h1> is %s' % escape(subpath)
