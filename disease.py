
#------------- import libraries and dependencies  ---------------------


import streamlit as st 
import numpy as np 
import pickle
from streamlit_option_menu import option_menu


#------------- Setting the page conf ---------------------
st.set_page_config(
    layout="wide",
    page_title="Disease Prediction",
    page_icon=":heart",
 
    initial_sidebar_state="expanded",

)





#------------- LOADING THE SAVED MODELS ---------------------
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))
parkinsons_model = pickle.load(open("parkinsons_model.sav", "rb"))
heart_model = pickle.load(open("heart_disease_model.sav", "rb"))



#------------- SIDEBAR FOR NAVIGATION ---------------------
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System",
                            ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                            default_index = 0,
                            orientation="vertical",
                            icons=['activity', 'heart', 'person']

                            )


#------------- Diabetes prediction page ---------------------
if selected == "Diabetes Prediction":

    # page title 
    st.title("Diabetes Prediction using ML")
    st.divider()
    col1, col2, col3 = st.columns(3, gap='small')

    # getting user input
    with col1:
        pregnancies = st.text_input("Number of Pregnancies", key="pregnancies")    

    with col2:
        glucose = st.text_input("Glucose Level", key="glucose")
    
    with col3:
        bloodpressure = st.text_input("Blood Pressure value", key="bp")
    
    with col1:
        skin_thickness = st.text_input("Skin Thickness value", key="st")

    with col2:
        insulin = st.text_input("Insulin Level", key="insulin")
    with col3:
        bmi = st.text_input("BMI Level", key="bmi")

    with col1:
        DiabetesPadigreeFunction = st.text_input("Diabetes Padigree Function value", key="dpf")
    with col2:
        age = st.text_input("Age of the Person", key="age")


    # code for prediction 
    diabetes_dignosis = ""

    # creating a button for prediction 
    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict([[pregnancies, glucose, bloodpressure, skin_thickness,insulin, bmi, DiabetesPadigreeFunction, age]])

        if diab_prediction[0] == 1:
            diabetes_dignosis = "The Person is Diabetic"
            st.warning(diabetes_dignosis)
        else:
            diabetes_dignosis = "The Person is Not Diabetic"
            st.success(diabetes_dignosis)


#------------- Heart Disease prediction page ---------------------
if selected == "Heart Disease Prediction":
    # page title 
    st.title("Heart Disease Prediction using ML")
 
    st.divider()

    
    
    col1, col2, col3, col4 = st.columns(4, gap='small')

    with col1:
        age = st.number_input("Age", key="age")
    with col2:
        sex = st.number_input("Sex", key="sex")
    with col3:
        cp = st.number_input("Chest Pain Type")
    with col4:
        trestbps = st.number_input("Resting Blood Pressure")
    with col1:
        chol = st.number_input("Serum cholestoral in mg/dl")
    with col2:
        fbs = st.number_input("Fasting Blood Sugar")
    with col3:
        restecg = st.number_input("Resting Electrodiographic ")
    with col4:
        thalach = st.number_input("Maximum hear rate achieved")
    with col1:
        exang = st.number_input("Exercice Induced Angina")
    with col2:
        oldpeak =  st.number_input("Old Peak")
    with col3:
        slope = st.number_input("Slope")
    with col4:
        ca =st.number_input("Number of major vessels")   
    with col1:
        thal = st.number_input("Reversable Defect")
    

     # code for prediction 

    heart_dignosis = ""
    if st.button("Heart Disease Prediction"):
        heart_prediction = heart_model.predict([[age,sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])            

        if (heart_prediction[0]== 0):
            heart_dignosis = 'The Person does not have a Heart Disease'
            st.success(heart_dignosis)
        else:
            heart_dignosis = 'The Person has Heart Disease'    
            st.warning(heart_dignosis)

#------------- Parkinsons prediction page ---------------------
if selected == "Parkinsons Prediction":
    # page title 
    st.title("Parksinsons Prediction using ML")

    # user input

    st.subheader("Coming soon..... ")
    st.divider()
   




hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)