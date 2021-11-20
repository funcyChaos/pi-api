from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(18, gpio.OUT)

@app.route("/")
def index():
	gpio.output(18,gpio.HIGH)
	time.sleep(1)
	gpio.output(18,gpio.LOW)
	return render_template('index.html')

@app.route("/escape/<var>")
def passVariable(var):
	return f'you passed: {escape(var)}'

@app.route("/led/<state>")
def actuate(state):
	if state == 'on':
		gpio.output(18,gpio.HIGH)
	if state == 'off':
		gpio.output(18,gpio.LOW)
	return('',204)

@app.route("/hello")
def hello():
	return "<h1>Hello from my rasberry pi!</h1><p>Let's Gooo!</P>"