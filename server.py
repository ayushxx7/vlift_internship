from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretKeyLol'


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

		return render_template('services.html')


	return(render_template('userLogin.html', form=form))

@app.route('/signup', methods = ['POST','GET'])
def signup():
	form = Signup()

	if form.validate_on_submit():
		return render_template('services.html')

	return(render_template('signup.html', form=form))

@app.route('/agentLogin', methods = ['POST','GET'])
def agentLogin():
	return(render_template('userLogin.html'))


if __name__ == "__main__":
	app.run(debug=True)