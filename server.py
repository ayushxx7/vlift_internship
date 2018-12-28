from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return(render_template('index.html'))

@app.route('/userLogin')
def userLogin():
	return(render_template('userLogin.html'))

@app.route('/agentLogin')
def agentLogin():
	return(render_template('userLogin.html'))


if __name__ == "__main__":
	app.run(debug=True)