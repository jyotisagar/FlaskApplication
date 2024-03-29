from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '27f7637817cf42cc3f0e54e42fbbbe04'

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'a@a.com' and form.password.data == 'a':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
