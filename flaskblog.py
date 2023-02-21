from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'


posts = [
    {
        'author': 'Cory Taylor',
        'title': 'Blog1',
        'content': 'Some Content'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog2',
        'content': 'Some Content'
    },
    {
        'author': 'Johny Doe',
        'title': 'Blog3',
        'content': 'Some Content'
    },

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', Posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data} !', 'success')
        return redirect( url_for('home') )
    return render_template('register.html', title='Register', Form = form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    """if form.validate_on_submit():"""

    return render_template('login.html', title='Login', Form = form)


if __name__ == "__main__":
    app.run(port=3000, debug=True)

