from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")

def index():
	return render_template('index.html')

@app.route("/location_route", methods=["POST"])

def location_route():
	form_data = request.form
	print (form_data["location"])
	return "All OK"

@app.route("/location/<name>", methods=["GET"])

def location(name):
  return render_template('location.html', location=name)

app.run(debug=True)