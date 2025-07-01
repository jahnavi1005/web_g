import pickle
import streamlit as st

# Load model (relative path, must be in same directory)
diabetes_model = pickle.load(open('diabetes_model(2).sav', 'rb'))

st.title('Diabetes Prediction using Machine Learning')

cols = st.columns(3)
labels = [
    'Pregnancies', 'Glucose Level', 'Blood Pressure', 'Skin Thickness',
    'Insulin Level', 'BMI', 'Diabetes Pedigree Function', 'Age'
]

inputs = []
for i, label in enumerate(labels):
    with cols[i % 3]:
        val = st.text_input(label)
        inputs.append(val)

if st.button('Predict Diabetes'):
    try:
        data = [float(x) for x in inputs]
        result = diabetes_model.predict([data])
        diagnosis = "✅ The person is diabetic" if result[0] == 1 else "✅ The person is not diabetic"
        st.success(diagnosis)
    except:
        st.error("❌ Please enter valid numeric values.")
