from flask import Flask,request,jsonify,render_template
from .views import *


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('page.html')

@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': views.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET','POST'])

def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': views.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)
    return response


@app.route('/predict', methods=['GET','POST'])
def predict():
    location = request.form['location']
    print(type(location))
    total_sqft = float(request.form['total_sqft'])
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    
    # first loading the saved artifacts
    views.load_saved_artifacts()

    response = views.get_estimated_price(location,total_sqft,bhk,bath)
    return render_template("page.html",prediction_text="The House price prediction is {}".format(response))

if __name__ == "__main__":
    print("Starting python flask server")
    views.load_saved_artifacts()
    app.run()