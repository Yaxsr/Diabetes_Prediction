import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul web
st.title('Data Mining Prediksi Diabetes')

# Membagi kolom
col1, col2 = st.columns(2)
with col1:
    Pregnancies = st.text_input('Input nilai Pregnancies')
    BloodPressure = st.text_input('Input nilai Blood Pressure')
    Insulin = st.text_input('Input nilai Insulin')
    DiabetesPedigreeFunction = st.text_input('Input nilai Diabetes Pedigree Function')

with col2:
    Glucose = st.text_input('Input nilai Glucose')
    SkinThickness = st.text_input('Input nilai Skin Thickness')
    BMI = st.text_input('Input nilai BMI')
    Age = st.text_input('Input nilai Age')

# Code untuk prediksi
diab_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    if diab_prediction[0] == 1:
        diab_diagnosis = 'Pasien terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena Diabetes'

st.success(diab_diagnosis)
