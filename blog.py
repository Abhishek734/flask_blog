from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '33714b7a88d47e355a4bbfe78a247c27'
posts = [
    {
    'author':'Abhishek',
    'title': 'Blog 1',
    'content':' first post content',
    'date_posted': 'April 20, 2019'
    },
    {
    'author':'Vikash',
    'title': 'Blog 2',
    'content': 'Second post content',
    'date_posted': 'April 22, 2019'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged In', 'success')
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful, please check username and password", 'danger')
    return render_template('login.html', title='Login', form=form)


# set FLASK_APP=1_blog.py

if __name__ == '__main__':
	app.run(debug=True)
