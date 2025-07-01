import pickle
import streamlit as st

# Load the saved diabetes model using full path (Windows)
model_path = r"C:\Users\jahna\Downloads\diabetes_model (2).sav"
diabetes_model = pickle.load(open(model_path, 'rb'))

# Page Title
st.title('Diabetes Prediction using ML')

# Input layout
cols = st.columns(3)
labels = ['Pregnancies', 'Glucose Level', 'Blood Pressure', 'Skin Thickness', 'Insulin Level', 'BMI',
          'Diabetes Pedigree Function', 'Age']

inputs = []
for i, label in enumerate(labels):
    with cols[i % 3]:
        value = st.text_input(label)
        inputs.append(value)

# Predict Button
if st.button('Predict Diabetes'):
    try:
        input_data = [float(i) for i in inputs]
        prediction = diabetes_model.predict([input_data])
        diagnosis = 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'
        st.success(diagnosis)
    except ValueError:
        st.error('Please enter valid numeric values')
