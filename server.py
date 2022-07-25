from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    return 'This is my blog'


@app.route('/blog/dogs')
def blog_dogs():
    return 'These are my dogs'
