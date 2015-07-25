from flask import Flask, render_template, abort, request, jsonify, g
import sqlite3	
import rpy2.robjects as robjects

app = Flask(__name__)
DATABASE = 'CountryCodes'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def connect_db():
    return sqlite3.connect(DATABASE)


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/colors/<country>')
def getColorCode(country):
	c = get_db().cursor()
	colorList = {}
	for row in c.execute('SELECT Country, Color1, Color2, Color3 FROM CountryCodes where Country LIKE ? LIMIT 5',['%' + country + '%']):
		colorList[row[0]] = [row[1],row[2],row[3]]		
	return jsonify(colorList = colorList)


@app.route('/<test>,<test2>')
def nitin(test,test2):
	x = {}
	x['nitin'] = {}
	x['nitin']['weight'] = test
	x['gokul'] = test2
	y = sumchar(test,test2)
	return jsonify(temp=x,temp2=y)

def sumchar(test,test2):
	return int(test) + int(test2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug='True')