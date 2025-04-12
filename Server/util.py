import json
import pickle
import numpy as np
import pandas as pd

__locations = None
__columns = None
__model = None

def get_prediction(location,sqrft,bhk,bath):
    try:
        loc_index = __columns.index(location.lower())
    except:
        loc_index =  -1

    x = np.zeros(len(__columns))
    x[0] = sqrft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    print("Input vector:", x)
    return round(__model.predict(pd.DataFrame([x],columns=__columns))[0],2)


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading the artifacts...Start")
    global __locations
    global __columns
    with open("./artifacts/columns.json",'r') as f:
        __columns = json.load(f)["columns"]
        __locations = __columns[3:]
    global __model
    with open("./artifacts/bengaluru_home_price_model.pkl",'rb') as f:
        __model = pickle.load(f)
        print("loading saved artifacts..... done!!!!")




if __name__ == "__main__":
    load_saved_artifacts()
    get_prediction()
    print(get_location_names())
    print(get_prediction("Ambedkar Nagar",1000,2,2))
    print(get_prediction("Ambedkar Nagar", 1000, 3, 3))