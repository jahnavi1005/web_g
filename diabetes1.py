import pickle
import streamlit as st

# Load the model from the same directory
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Streamlit App Title
st.title('Diabetes Prediction using Machine Learning')

# Input Fields Layout
cols = st.columns(3)
labels = [
    'Pregnancies', 'Glucose Level', 'Blood Pressure', 'Skin Thickness',
    'Insulin Level', 'BMI', 'Diabetes Pedigree Function', 'Age'
]

# User Inputs
inputs = []
for i, label in enumerate(labels):
    with cols[i % 3]:
        value = st.text_input(label)
        inputs.append(value)

# Predict Button
if st.button('Predict Diabetes'):
    try:
        # Convert input strings to float
        input_data = [float(i) for i in inputs]
        
        # Make Prediction
        prediction = diabetes_model.predict([input_data])
        
        # Display Result
        result = '✅ The person is diabetic' if prediction[0] == 1 else '✅ The person is not diabetic'
        st.success(result)
    
    except ValueError:
        st.error("❌ Please enter valid numeric values in all fields.")
