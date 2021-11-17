from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(18, gpio.OUT)

@app.route("/")
def index():
	gpio.output(18,gpio.HIGH)
	return render_template('index.html')

@app.route("/escape/<var>")
def passVariable(var):
	return f'you passed: {escape(var)}'
@app.route("/hello")
def hello():
	return "<h1>Hello from my rasberry pi!</h1><p>Let's Gooo!</P>"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=True)