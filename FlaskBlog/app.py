from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Jyoti',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date': 'Jan 01, 2000'
    },
{
        'author': 'Sagar',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date': 'Jan 02, 2000'
    },
    {
        'author': 'Chowrasia',
        'title': 'Blog post 3',
        'content': 'Third post content',
        'date': 'Jan 03, 2000'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts) #'Home page'


@app.route('/about')
def about():
    return render_template('about.html', title='about') #'This is about Page'


@app.route('/hello')
def hello():
    # name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'
    return '<h3>Hello World! Welcome to Flask World..</h3>'


if __name__ == '__main__':
    app.run(debug=True)
