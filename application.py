from flask import Flask,request,jsonify,render_template
import matplotlib.pyplot as pyplot
import numpy as numpy
import pandas as pd
import pickle

application = Flask(__name__)
app = application

model = pickle.load(open("models/linreg.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        Temperature = int(request.form["Temperature"])
        RH = int(request.form["RH"])
        Ws = int(request.form["Ws"])
        Rain = float(request.form["Rain"])
        FFMC = float(request.form["FFMC"])
        DMC = float(request.form["DMC"])
        ISI = float(request.form["ISI"])
        Classes = int(request.form["Classes"])
        Region = int(request.form["Region"])

        features = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
        scaled_features = scaler.transform(features)
        FWI = model.predict(scaled_features)
        print("features",features)
        print("Scaled Features",scaled_features)
        return render_template("form.html", FWI=FWI[0])

    return render_template("form.html")
    

if __name__=="__main__":
    app.run(debug=True)    