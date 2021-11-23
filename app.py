from flask import Flask, render_template, jsonify, request
from markupsafe import escape

import sqlite3
import json

import RPi.GPIO as gpio
import time

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(18, gpio.OUT)

@app.route("/")
def index():
	gpio.output(18,gpio.HIGH)
	time.sleep(1)
	gpio.output(18,gpio.LOW)
	return render_template('index.html')

@app.route("/led/<state>")
def actuate(state):
	if state == 'on':
		gpio.output(18,gpio.HIGH)
	if state == 'off':
		gpio.output(18,gpio.LOW)
	return('',204)

@app.route('/db')
def dbRead():
	connection = sqlite3.connect('pi-api.db')
	cursor = connection.cursor()
	read = cursor.execute('SELECT username FROM users').fetchall()
	return jsonify(username=read)

@app.route('/users')
def users():
	return render_template('users.html')

@app.route('/users/newuser', methods = ['POST'])
def newUser():
	resDict = json.loads(request.data)
	connection = sqlite3.connect('pi-api.db')
	cursor = connection.cursor()
	cursor.execute("INSERT INTO users (username, password) VALUES ('%s', '%s')" % (resDict['username'], resDict['password']))
	connection.commit()
	cursor.close()

	return 'added user'

@app.route('/db/changepassword/<newPassword>')
def changePassword(newPassword):
	connection = sqlite3.connect('pi-api.db')
	cursor = connection.cursor()
	cursor.execute("UPDATE users SET password = '%s' WHERE id = 1" % newPassword)
	connection.commit()
	cursor.close()

	return('Recorded update successfully')