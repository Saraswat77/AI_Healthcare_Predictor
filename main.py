# main.py - Streamlit app
import streamlit as st
import pandas as pd
from utils import load_model, predict_heart_disease, predict_diabetes

# Load models
heart_model = load_model("heart_model.pkl")
diabetes_model = load_model("diabetes_model.pkl")

st.set_page_config(page_title="AI Health Assistant", layout="centered")
st.title("🧠 AI Health Assistant")
st.markdown("Use AI to predict diseases.")

menu = ["Heart Disease", "Diabetes","Saraswat" ]            #streamlit run app/main.py
choice = st.sidebar.selectbox("Choose Module", menu)

if choice == "Heart Disease":
    st.header("❤️ Heart Disease Prediction")
    age = st.slider("Age", 20, 80, 45)
    sex = st.selectbox("Sex", [0, 1])
    cp = st.slider("Chest Pain Type (cp)", 0, 3, 1)
    trestbps = st.slider("Resting Blood Pressure", 80, 200, 120)
    chol = st.slider("Cholesterol", 100, 400, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120?", [0, 1])
    restecg = st.selectbox("Resting ECG", [0, 1, 2])
    thalach = st.slider("Max Heart Rate Achieved", 70, 200, 150)
    exang = st.selectbox("Exercise-induced Angina", [0, 1])
    oldpeak = st.slider("ST depression", 0.0, 6.0, 1.0)
    slope = st.selectbox("Slope", [0, 1, 2])
    ca = st.slider("Number of Major Vessels", 0, 4, 0)
    thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

    if st.button("Predict Heart Disease"):
        data = [[age, sex, cp, trestbps, chol, fbs, restecg,
                 thalach, exang, oldpeak, slope, ca, thal]]
        prediction = predict_heart_disease(heart_model, data)
        st.success(f"Prediction: {'Disease' if prediction == 1 else 'No Disease'}")

elif choice == "Diabetes":
    st.header("🩺 Diabetes Prediction")
    pregnancies = st.slider("Pregnancies", 0, 15, 1)
    glucose = st.slider("Glucose Level", 50, 200, 110)
    bp = st.slider("Blood Pressure", 40, 130, 70)
    skin = st.slider("Skin Thickness", 0, 99, 20)
    insulin = st.slider("Insulin", 0, 900, 80)
    bmi = st.slider("BMI", 10.0, 60.0, 25.0)
    dpf = st.slider("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
    age = st.slider("Age", 18, 90, 35)

    if st.button("Predict Diabetes"):
        data = [[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]]
        prediction = predict_diabetes(diabetes_model, data)
        st.success(f"Prediction: {'Diabetic' if prediction == 1 else 'Non-Diabetic'}")

