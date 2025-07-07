# main.py - Streamlit app
import streamlit as st
import pandas as pd
from utils import load_model, predict_heart_disease, predict_diabetes

# Load models
heart_model = load_model("models/heart_model.pkl")
diabetes_model = load_model("models/diabetes_model.pkl")

st.set_page_config(page_title="AI Health Assistant", layout="centered")
st.title("🧠 AI Health Assistant")
st.markdown("Use AI to predict diseases based on medical inputs.")

menu = ["Heart Disease", "Diabetes"]
choice = st.sidebar.selectbox("Choose a Module", menu)

if choice == "Heart Disease":
    st.header("❤️ Heart Disease Risk Prediction")

    with st.expander("📋 Patient Basic Info"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age (years)", 20, 80, 45)
            sex = st.radio("Sex", ["Male", "Female"])
            fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
        with col2:
            trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
            chol = st.number_input("Cholesterol (mg/dl)", 100, 400, 200)
            thalach = st.number_input("Max Heart Rate Achieved", 70, 220, 150)

    with st.expander("🫀 Heart-Related Factors"):
        cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal", "Asymptomatic"])
        restecg = st.selectbox("Resting ECG Results", ["Normal", "Abnormal", "Hypertrophy"])
        exang = st.radio("Exercise-induced Angina", ["Yes", "No"])
        oldpeak = st.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0)
        slope = st.selectbox("Slope of ST Segment", ["Upsloping", "Flat", "Downsloping"])
        ca = st.slider("Major Vessels Colored by Fluoroscopy", 0, 4, 0)
        thal = st.selectbox("Thalassemia Type", ["Normal", "Fixed Defect", "Reversible Defect", "Unknown"])

    # Encode categorical inputs
    sex = 1 if sex == "Male" else 0
    fbs = 1 if fbs == "Yes" else 0
    cp = ["Typical Angina", "Atypical Angina", "Non-anginal", "Asymptomatic"].index(cp)
    restecg = ["Normal", "Abnormal", "Hypertrophy"].index(restecg)
    exang = 1 if exang == "Yes" else 0
    slope = ["Upsloping", "Flat", "Downsloping"].index(slope)
    thal = ["Normal", "Fixed Defect", "Reversible Defect", "Unknown"].index(thal)

    if st.button("🧠 Predict Heart Disease"):
        data = [[age, sex, cp, trestbps, chol, fbs, restecg,
                 thalach, exang, oldpeak, slope, ca, thal]]
        prediction = predict_heart_disease(heart_model, data)
        st.success(f"Prediction: {'❤️ Disease Detected' if prediction == 1 else '✅ No Disease'}")

elif choice == "Diabetes":
    st.header("🩺 Diabetes Risk Prediction")

    with st.expander("📋 Patient Data"):
        col1, col2 = st.columns(2)
        with col1:
            pregnancies = st.slider("Number of Pregnancies", 0, 15, 1)
            glucose = st.slider("Glucose Level", 50, 200, 110)
            bp = st.slider("Blood Pressure (mm Hg)", 40, 130, 70)
            skin = st.slider("Skin Thickness (mm)", 0, 99, 20)
        with col2:
            insulin = st.slider("Insulin (mu U/ml)", 0, 900, 80)
            bmi = st.slider("BMI (kg/m²)", 10.0, 60.0, 25.0)
            dpf = st.slider("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
            age = st.slider("Age (years)", 18, 90, 35)

    if st.button("🧠 Predict Diabetes"):
        data = [[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]]
        prediction = predict_diabetes(diabetes_model, data)
        st.success(f"Prediction: {'🩸 Diabetic' if prediction == 1 else '✅ Non-Diabetic'}")
