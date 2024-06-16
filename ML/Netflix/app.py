from flask import Flask , render_template , request
import  pandas as pd
import numpy as np
import sklearn 
import pickle

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('/index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    Open = float(request.form["open"])
    High = float(request.form["high"])
    Low = float(request.form["low"])
    Adj_Close = float(request.form["adj_close"])
    Volume = float(request.form["volume"])
    Year = float(request.form["year"])
    Month = float(request.form["month"])
    Day = float(request.form["day"])

    feature_list = [[Open, High, Low, Adj_Close, Volume, Year, Month, Day]]
    prediction = model.predict(feature_list)
    return render_template('/index.html' , output = prediction[0])


if __name__ == '__main__':
    app.run(debug = True)