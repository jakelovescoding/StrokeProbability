import streamlit as st
import torch
from predict import predict

def divide_arrays(array1, array2):
    result = []
    for i in range(len(array1)):
        result.append(array1[i] / array2[i])
    return result


st.set_page_config(
    page_title="Stroke Probability 🧠"
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.write("""
         # Stroke Probability 🧠
         """
         )
gender = st.selectbox('Gender',('Male', 'Female', 'Other'))
age = st.number_input(label='Age',value=10,step=1)
hypertension = st.checkbox(label='hypertension')
heart_disease = st.checkbox(label='heart_disease')
ever_married = st.checkbox(label='ever_married')
work = st.selectbox('Work',('children', 'Govt_jov', 'Never_worked','Private','Self-employed'))
residence = st.selectbox('Residence',('Rural', 'Urban'))
glucose = st.number_input(label='Glucose level',min_value=1,max_value=500,value=100,step=1)
weight = st.number_input(label='Weight (lbs)',min_value=1,max_value=300,value=140,step=1)
height = st.number_input(label='Height (in)',min_value=1,max_value=84,value=60,step=1)
bmi = weight/pow(height,2) * 703

smoking = st.selectbox('Smoking',('formerly smoked', 'never smoked', 'smokes', 'Unknown'))

gender_map = {'Male': 0,'Female': 1,'Other': 2}
ever_married_map = {'No': 0,'Yes': 1}
work_type_map = {'children': 0,'Govt_jov': 1,'Never_worked': 2,'Private': 3,'Self-employed': 4}
residence_type_map = {'Rural': 0,'Urban': 1}
smoking_status_map = {'formerly smoked': 0, 'never smoked': 1, 'smokes': 2, 'Unknown': 3}
data = []

if st.button("Predict!"):
    data.append(gender_map[gender])
    data.append(age)
    data.append(1 if hypertension else 0)
    data.append(1 if heart_disease else 0)
    data.append(1 if ever_married else 0)
    data.append(work_type_map[work])
    data.append(residence_type_map[residence])
    data.append(glucose)
    data.append(bmi)
    data.append(smoking_status_map[smoking])
    normalize_data = divide_arrays(data,[1, 82.0, 1, 1, 1, 4.0, 1, 271.74, 61.6, 2])
    st.success("The probablity that you will have a stroke is "+str(int(round(predict(normalize_data).item(),2)*100))+"%     👍")
    

#st.text("Please upload an image file") text
#st.success("what") green text box
html_link = """
    Made by Shreyam Bhattacharya, Akhil Byju, Jake Jin, Srinandha Murugesan
    """
st.markdown(html_link, unsafe_allow_html=True)