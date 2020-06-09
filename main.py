import requests
from flask import Flask, request, render_template
from pprint import pprint as pp 
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
    data = []
    error = None
    return render_template("weather.html", data=data, error=error)

@app.route("/result", methods=['GET', 'POST'])
def result():
    data = []
    error = None
    city_name = request.form.get('city_name')
    resp = query_api(city_name)
    if resp.get('cod') == 200:
        data.append(resp)
    else:
        error = "Could not get weather data :("
    return render_template("result.html", data=data, error=error)


if __name__ == "__main__":
    app.run(debug=True)

