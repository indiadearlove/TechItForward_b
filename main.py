from flask import Flask, render_template, request
from data import DATA_FILE

app = Flask("MyApp")

@app.route("/")

def index():
	return render_template('index.html')

@app.route("/location_route", methods=["POST"])

def location_route():
	form_data = request.form
	print (form_data["location"])
	return "All OK"

@app.route("/location", methods=['POST'])

def location():
	if request.form["location"]:
	  return render_template('location.html', location=request.form["location"], data=DATA_FILE)
	else:
	  return 'Hey'

app.run(debug=True)