import numpy as np
import pickle
import pandas as pd
import streamlit as sl
from PIL import Image

pickle_in = open("kidney_model.pkl", "rb")
model = pickle.load(pickle_in)

def welcome():
    return "Welcome"

def predict_kidney_disease(age, bp, sg, al, su, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc):
    prediction = model.predict([[age, bp, sg, al, su, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc]])
    if prediction == 1.0:
        prediction = 'Chronic'
    else:
        prediction = 'Healthy'
    print(prediction)

    return prediction

def main():
    sl.title("Kidney Disease Classifier")
    html_temp = """
    <div style="background-color:LightGreen; padding:10px;">
    <h2 style="color:white; text-align:center;"> Streamlit Kidney Disease Classifier App </h2>
    <h6 style="color:white; text-align:left;"> Create by : Arasy Bazwir </h6>
    </div>
    """

    sl.markdown(html_temp, unsafe_allow_html=True)
    age = sl.text_input("Age", "Type Here")
    bp = sl.text_input("Blood Pressure", "Type Here")
    sg = sl.text_input("Specific Gravity", "Type Here")
    al = sl.text_input("Albumin", "Type Here")
    su = sl.text_input("Sugar", "Type Here")
    bgr = sl.text_input("Blood Glucose Random", "Type Here")
    bu = sl.text_input("Blood Urea", "Type Here")
    sc = sl.text_input("Serum Creatinine", "Type Here")
    sod = sl.text_input("Sodium", "Type Here")
    pot = sl.text_input("Potasium", "Type Here")
    hemo = sl.text_input("Hemogoblin", "Type Here")
    pcv = sl.text_input("Packed Cell Volume", "Type Here")
    wc = sl.text_input("White Blood Cell Count", "Type Here")
    rc = sl.text_input("Red Blood Cell Count", "Type Here")

    result = ""

    if sl.button("Predict"):
        result = predict_kidney_disease(age, bp, sg, al, su, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc)
    sl.success("The Kidney is {}".format(result))
    
    if sl.button("About"):
        sl.text("if you are interested with this app")
        sl.text("you can reach me : arasy1703@gmail.com")

if __name__ == "__main__":
    main()