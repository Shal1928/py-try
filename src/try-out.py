from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return '{} User-value %s'.format(username) % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post-value %d' % post_id

@app.route('/path/<path:subpath>')
def path(subpath):
    # show the subpath after /path/
    return 'Subpath-value %s' % subpath

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('path'))
#     print(url_for('path', next='/'))
#     print(url_for('profile', username='John Doe'))