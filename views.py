import json 
import pickle
import numpy as np
import os
from flask import current_app as app

locations = None
data_columns = None
model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index =  data_columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts")
    global data_columns
    global locations

    filename = os.path.join(app.static_folder, 'data', 'columns.json')
    
    
    with open(filename, "r") as f:
        data_columns = json.load(f)['data_columns']
        locations = data_columns[3:] 
    
    global model
    if model is None:
        filename = os.path.join(app.static_folder, 'data', 'house_price_prediction.pkl')
        
        with open(filename,"rb") as f:
         model = pickle.load(f)
    print("loading saved articles")


def get_location_names():
    return locations


def get_data_columns():
    return data_columns

if __name__ == "__main__":
    load_saved_artifacts()
    
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print("-----")
    print(get_estimated_price('7th Phase JP Nagar',2225, 3, 3))