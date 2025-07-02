import pickle
import json
import numpy as np
import pandas as pd 

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

__brand = None
__fuel = None
__transmission = None
__owner = None
__seller = None
__data_columns = None
__model = None

def estimated_price(brand, fuel, transmission, owner, seller, year, km, mileage, engine_cc, max_bhp, seats):

    brand_index = __data_columns.index(brand.lower())
    fuel_index = __data_columns.index(fuel.lower())
    transmission_index = __data_columns.index(transmission.lower())
    owner_index = __data_columns.index(owner.lower())
    seller_index = __data_columns.index(seller.lower())

    a = np.zeros(len(__data_columns))
    a[0] = year
    a[1] = km 
    a[2] = mileage
    a[3] = engine_cc
    a[4] = max_bhp
    a[5] = seats

    # if a[brand_index] >= 0:
    #     a[brand_index] = 1
    # if a[fuel_index] >= 0:
    #     a[fuel_index] = 1
    # if a[transmission_index] >= 0:
    #     a[transmission_index] = 1
    # if a[owner_index] >= 0:
    #     a[owner_index] = 1
    # if a[seller_index]  >= 0:
    #     a[seller_index] = 1

    if brand_index >= 0:
        a[brand_index] = 1
    if fuel_index >= 0:
        a[fuel_index] = 1
    if transmission_index >= 0:
        a[transmission_index] = 1
    if owner_index >= 0:
        a[owner_index] = 1
    if seller_index >= 0:
        a[seller_index] = 1

    return round(__model.predict([a])[0], 2)

def get_brand_names():
    return __brand

def get_fuel():
    return __fuel

def get_transmission():
    return __transmission

def get_owner():
    return __owner

def get_seller():
    return __seller

def load_saved_artifacts():
    print("Loading Saved Artifacts...")
    global __data_columns
    global __brand
    global __fuel
    global __transmission
    global __owner
    global __seller
    global __model

    import os

    base_path = os.path.dirname(__file__)  # this gets the path of the util.py file
    columns_path = os.path.join(base_path, "Artifacts", "Columns.json")
    model_path = os.path.join(base_path, "Artifacts", "Old_Car.pickle")

    with open(columns_path, 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __brand = __data_columns[20:]
        __fuel = __data_columns[6:10]
        __transmission = __data_columns[13:15]
        __owner = __data_columns[15:20]
        __seller = __data_columns[10:13]

    with open(model_path, 'rb') as f:
        __model = pickle.load(f)


    # with open(r"C:\Users\iamha\OneDrive\Documents\OldCar\Server\Artifacts\Columns.json", 'r') as f:
    #     __data_columns = json.load(f)['data_columns']
    #     __brand = __data_columns[20:]
    #     __fuel = __data_columns[6:10]
    #     __transmission = __data_columns[13:15]
    #     __owner = __data_columns[15:20]
    #     __seller = __data_columns[10:13]

    # with open(r"C:\Users\iamha\OneDrive\Documents\OldCar\Server\Artifacts\Old_Car.pickle", 'rb') as f:
    #     __model = pickle.load(f)
    # print("Loading Saved Artifacts... Completed")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_brand_names())
    print(get_fuel())
    print(get_transmission())
    print(get_owner())
    print(get_seller())
    print(estimated_price(brand='Renault', fuel='Petrol', transmission='Automatic', owner='First', seller='Dealer' ,year=2019, km=45000, mileage=60, engine_cc=1300, max_bhp=60, seats=5))
    print(estimated_price(brand='Mitsubishi', fuel='Diesel', transmission='Manual', owner='Second', seller='Dealer' ,year=2017, km=45000, mileage=60, engine_cc=1300, max_bhp=60, seats=5))