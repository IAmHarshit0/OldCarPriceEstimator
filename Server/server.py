from flask import Flask, request, jsonify
from . import util

app = Flask(__name__)

@app.route('/get_brand_names')
def get_brand_names():
    response = jsonify({
        'brand': util.get_brand_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

@app.route('/get_fuel')
def get_fuel():
    response = jsonify({
        'fuel': util.get_fuel()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

@app.route('/get_transmission')
def get_transmission():
    response = jsonify({
        'transmission': util.get_transmission()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

@app.route('/get_owner')
def get_owners():
    response = jsonify({
        'owner': util.get_owner()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

@app.route('/get_seller')
def get_seller():
    response = jsonify({
        'seller': util.get_seller()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

@app.route('/predict_car_price', methods=["POST"])
def predict_car_price():
    brand = request.form['brand']
    fuel = request.form['fuel']
    transmission = request.form['transmission']
    owner = request.form['owner']
    seller = request.form['seller']
# year, km, mileage, engine_cc, max_bhp, seats
    year = int(request.form['year'])
    km = float(request.form['km'])
    mileage = float(request.form['mileage'])
    engine_cc = float(request.form['engine_cc'])
    max_bhp = float(request.form['max_bhp'])
    seat = int(request.form['seats'])

    response = jsonify({
        'estimate_price': util.estimated_price(brand, fuel, transmission, owner, seller, year, km, mileage, engine_cc, max_bhp, seat)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Old Car Price Prediction")
    util.load_saved_artifacts()
    app.run()