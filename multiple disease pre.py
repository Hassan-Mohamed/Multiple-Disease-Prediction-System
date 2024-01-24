# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:53:51 2022
@author: haska
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Function to validate and convert input data
def validate_input(input_value, data_type):
    if data_type == 'int':
        return int(input_value) if input_value else None
    elif data_type == 'float':
        return float(input_value) if input_value else None
    return input_value

# loading the saved models
diabetes_model = pickle.load(open('C:/Users/haska/Desktop/Multiple Disease Prediction System/saved models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/haska/Desktop/Multiple Disease Prediction System/saved models/heart_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction'],
                           icons=['activity', 'heart'], default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.header('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    if st.button('Diabetes Test Result'):
        Glucose = validate_input(Glucose, 'float')
        DiabetesPedigreeFunction = validate_input(DiabetesPedigreeFunction, 'float')
        if Glucose and DiabetesPedigreeFunction:
            if Glucose > 130 and DiabetesPedigreeFunction > 3:
                st.success('The person is diabetic')
            else:
                Pregnancies = validate_input(Pregnancies, 'int')
                BloodPressure = validate_input(BloodPressure, 'float')
                SkinThickness = validate_input(SkinThickness, 'float')
                Insulin = validate_input(Insulin, 'float')
                BMI = validate_input(BMI, 'float')
                Age = validate_input(Age, 'int')
                try:
                    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
                    diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
                    st.success(diab_diagnosis)
                except Exception as e:
                    st.error(f"Error in prediction: {e}")
        else:
            st.error("Please enter Glucose Level and Diabetes Pedigree Function.")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.header('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.selectbox('Sex', ['', '0', '1'])
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['', '0', '1'])
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.selectbox('Exercise Induced Angina', ['', '0', '1'])
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    if st.button('Heart Disease Test Result'):
        trestbps = validate_input(trestbps, 'float')
        if trestbps:
            if trestbps < 90 or trestbps > 120:
                st.success('The person is having heart disease')
            else:
                age = validate_input(age, 'float')
                sex = validate_input(sex, 'int')
                cp = validate_input(cp, 'int')
                chol = validate_input(chol, 'float')
                fbs = validate_input(fbs, 'int')
                restecg = validate_input(restecg, 'int')
                thalach = validate_input(thalach, 'float')
                exang = validate_input(exang, 'int')
                oldpeak = validate_input(oldpeak, 'float')
                slope = validate_input(slope, 'int')
                ca = validate_input(ca, 'int')
                thal = validate_input(thal, 'int')
                try:
                    heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
                    heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
                    st.success(heart_diagnosis)
                except Exception as e:
                    st.error(f"Error in prediction: {e}")
        else:
            st.error("Please enter Resting Blood Pressure.")










