from flask import Flask, url_for, request, render_template, flash, redirect

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/ok')
def hello2():
    flash('You were successfully logged in')
    return redirect(url_for('hello'))

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "login POST"
        # return do_the_login()
    else:
        return "login NOT POST"
        # return show_the_login_form()

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'