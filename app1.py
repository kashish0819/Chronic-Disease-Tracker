import streamlit as st
import joblib
import numpy as np

model = joblib.load("disease_model.pkl")

st.title("Chronic Disease Progression Prediction System")

age = st.number_input("Age", 40, 100, 60)
gender = st.selectbox("Gender", ["Male", "Female"])

disease = st.selectbox(
    "Disease",
    ["Diabetes", "Parkinson's", "Alzheimer's"]
)

medical = st.selectbox(
    "Medical History",
    ["Heart Disease", "Hypertension", "Asthma", "Stroke"]
)

lifestyle = st.selectbox(
    "Lifestyle",
    ["Active", "Sedentary", "Non-Smoker", "Occasional Drinker"]
)

biomarker = st.number_input("Biomarker Score", 0.0, 100.0, 20.0)
dose = st.number_input("Medication Dose", 0.5, 2.0, 1.0)
heart = st.number_input("Heart Rate", 60, 100, 80)

# Encoding
gender = 1 if gender == "Male" else 0

disease_map = {
    "Diabetes": 0,
    "Parkinson's": 1,
    "Alzheimer's": 2
}

medical_map = {
    "Heart Disease": 0,
    "Hypertension": 1,
    "Asthma": 2,
    "Stroke": 3
}

lifestyle_map = {
    "Active": 0,
    "Sedentary": 1,
    "Non-Smoker": 2,
    "Occasional Drinker": 3
}

if st.button("Predict Disease Stage"):

    data = np.array([[
        age,
        gender,
        disease_map[disease],
        medical_map[medical],
        lifestyle_map[lifestyle],
        biomarker,
        dose,
        heart
    ]])

    prediction = model.predict(data)[0]

    if prediction == 0:
        st.success("Early Stage")
    elif prediction == 1:
        st.warning("Mid Stage")
    else:
        st.error("Late Stage")