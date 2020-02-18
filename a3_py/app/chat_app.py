from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bro'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'eyo'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)
