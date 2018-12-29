from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretKeyLol'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Ayush\\Desktop\\vlift_flow\\database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manger = LoginManager()
login_manger = init_app(app)
login_manager.login_view = 'login'



class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(30), unique = True)
	password = db.Column(db.String(80))

class UserLogin(FlaskForm):
	username = StringField('username', validators = [InputRequired(), Length(min =4, max=30)])
	password = PasswordField('password', validators= [InputRequired(), Length(min = 5, max = 80)])
	remember = BooleanField('Remember Me?')

class Signup(FlaskForm):
	username = StringField('username', validators = [InputRequired(), Length(min =4, max=30)])
	password = PasswordField('password', validators= [InputRequired(), Length(min = 5, max = 80)])

@app.route('/')
def index():
	
	return(render_template('index.html'))

@app.route('/userLogin', methods = ['POST','GET'])
def userLogin():
	form = UserLogin()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password,form.password.data):
				return redirect('/services')

		return render_template('services.html')


	return(render_template('userLogin.html', form=form))

@app.route('/signup', methods = ['POST','GET'])
def signup():
	form = Signup()

	if form.validate_on_submit():
		new_user = User()
		new_user.username = form.username.data
		# print(new_user.username)
		hashed_password = generate_password_hash(form.password.data, method = 'sha256'
		new_user.password = hashed_password

		# print(User)
		# print(username)
		# new_user = User(username=form.data.username, password=form.data.password)
		db.session.add(new_user)
		db.session.commit()
		return 'New User Created!'
		# return render_template('services.html')

	return(render_template('signup.html', form=form))

@app.route('/agentLogin', methods = ['POST','GET'])
def agentLogin():
	return(render_template('userLogin.html'))

# @login_srequired
@app.route('/services', methods = ['POST','GET'])
def services():
	return(render_template('services.html'))

if __name__ == "__main__":
	app.run(debug=True)