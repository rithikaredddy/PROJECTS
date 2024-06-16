from flask import Flask,request ,render_template
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template("/index.html")

@app.route('/predict',methods=['GET','POST'])
def predict():
    N = int(request.form["Nitrogen"])
    P = int(request.form["Phosphorus"])
    K = int(request.form["Potassium"])
    T = int(request.form["Temparature"])
    H = int(request.form["Humidity"])
    PH = int(request.form["Ph"])
    R = int(request.form["Rainfall"])

    feature_list = [[N,P,K,T,H,PH,R]]
    prediction = model.predict(feature_list)
    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = f"{crop} is the best crop to be cultivated right there"

    else:
        result = "Sorry , we could not determine the best crop to be cultivated with the provided data..."

    return render_template('/index.html',result = result)


if __name__ == '__main__':
    app.run(debug=True)