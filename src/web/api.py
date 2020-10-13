import sqlite3
import json
from flask import Flask, escape, render_template, current_app, g

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, OpenQL'

@app.route('/hello')
def hello():
	return 'hello'

@app.route('/object/')
@app.route('/object/<id>')
def object(id):
	dict = {"code":id}
	print(dict)
	return render_template('hello.html', id=json.dumps(dict))

@app.route('/result')
def result():
	return {'username': 'abc', 'age' : 17 }

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

def get_db():
	if 'db' not in g:
		pass

	return g.db 

def close_db():
	db = g.pop('db', None)

	if db is not None:
		db.close()

