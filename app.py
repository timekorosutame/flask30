from flask import Flask, render_template, url_for, request, redirect, session, flash
from functools import wraps
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# шоб юзати сесії
app.secret_key = 'my secret_key'
# база даних
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

db = SQLAlchemy(app)
from models import *




# декоратор для провірки на logged_in в session
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('u need to login first')
			return redirect(url_for('login'))
	return wrap


@app.route('/')
@login_required
def home():
	posts = db.session.query(BlogPost).all()
	return render_template('index.html', posts = posts)


@app.route('/welcome')
def welcome():
	return render_template('welcome.html')


@app.route('/login', methods = ['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'invalid credentuals please, try again'
		else:
			session['logged_in'] = True
			flash('u logged in')
			return redirect(url_for('home'))

	return render_template('login.html', error = error)

# міняю місцями logged_in користувача на None
@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('u logged out')
	return redirect(url_for('welcome'))


if __name__ == '__main__':
	app.run(debug = True)

