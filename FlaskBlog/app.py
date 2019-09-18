from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Home page'


@app.route('/hello')
def hello():
    # name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'
    return '<h3>Hello World! Welcome to Flask World..</h3>'


@app.route('/about')
def about():
    return 'This is about Page'


if __name__ == '__main__':
    app.run(debug=True)
