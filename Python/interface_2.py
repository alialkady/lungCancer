# app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Function to load models
@st.cache(allow_output_mutation=True)
def load_models():
    logistic_model = joblib.load('models/logistic_regression.pkl')
    random_forest_model = joblib.load('models/random_forest.pkl')
    svm_model = joblib.load('models/svm.pkl')
    return logistic_model, random_forest_model, svm_model

# Load models
logistic_model, random_forest_model, svm_model = load_models()

# Define top 10 features
top_features = [
    'coughing_of_blood',
    'alcohol_use',
    'passive_smoker',
    'obesity',
    'smoking',
    'balanced_diet',
    'chest_pain',
    'fatigue',
    'air_pollution',
    'genetic_risk'
]

# Preprocess function
def preprocess_input(user_input):
    input_data = pd.DataFrame([user_input])

    input_df = input_data[top_features]

    return input_df

# Main function
def main():
    st.title("Cancer Level Prediction App")
    st.write("""
    ### Predict the cancer level of a patient based on their medical features.
    """)

    # Sidebar for model selection
    st.sidebar.header("Model Selection")
    model_choice = st.sidebar.selectbox("Choose your model", ("Logistic Regression", "Random Forest", "SVM"))

    # User inputs
    st.header("Input Patient Features")

    # Create input widgets for each feature
    user_input = {}
    
    # Feature: coughing_of_blood (Assuming binary: 0 - No, 1 - Yes)
    user_input['coughing_of_blood'] = st.selectbox(
        'Coughing of Blood',
        options=[0, 1],
        format_func=lambda x: 'No' if x == 0 else 'Yes'
    )

    # Feature: alcohol_use (Assuming scale 1-10)
    user_input['alcohol_use'] = st.slider(
        'Alcohol Use (1-10)',
        min_value=1,
        max_value=10,
        value=5
    )

    # Feature: passive_smoker (Assuming binary: 0 - No, 1 - Yes)
    user_input['passive_smoker'] = st.selectbox(
        'Passive Smoker',
        options=[0, 1],
        format_func=lambda x: 'No' if x == 0 else 'Yes'
    )

    # Feature: obesity (Assuming binary: 0 - No, 1 - Yes)
    user_input['obesity'] = st.selectbox(
        'Obesity',
        options=[0, 1],
        format_func=lambda x: 'No' if x == 0 else 'Yes'
    )

    # Feature: smoking (Assuming binary: 0 - No, 1 - Yes)
    user_input['smoking'] = st.selectbox(
        'Smoking',
        options=[0, 1],
        format_func=lambda x: 'No' if x == 0 else 'Yes'
    )

    # Feature: balanced_diet (Assuming scale 1-7)
    user_input['balanced_diet'] = st.slider(
        'Balanced Diet (1-7)',
        min_value=1,
        max_value=7,
        value=4
    )

    # Feature: chest_pain (Assuming scale 1-10)
    user_input['chest_pain'] = st.slider(
        'Chest Pain (1-10)',
        min_value=1,
        max_value=10,
        value=5
    )

    # Feature: fatigue (Assuming scale 1-10)
    user_input['fatigue'] = st.slider(
        'Fatigue (1-10)',
        min_value=1,
        max_value=10,
        value=5
    )

    # Feature: air_pollution (Assuming scale 1-7)
    user_input['air_pollution'] = st.slider(
        'Air Pollution (1-7)',
        min_value=1,
        max_value=7,
        value=4
    )

    # Feature: genetic_risk (Assuming scale 1-7)
    user_input['genetic_risk'] = st.slider(
        'Genetic Risk (1-7)',
        min_value=1,
        max_value=7,
        value=4
    )

    # Prediction button
    if st.button("Predict"):
        input_df = preprocess_input(user_input)

        # Check if preprocessing was successful
        if input_df is not None:
            # Select model
            if model_choice == "Logistic Regression":
                model = logistic_model
            elif model_choice == "Random Forest":
                model = random_forest_model
            elif model_choice == "SVM":
                model = svm_model
            else:
                st.error("Invalid model selected.")
                return

            # Make prediction
            prediction = model.predict(input_df)[0]
            prediction_proba = model.predict_proba(input_df)[0]

            # Map prediction to level
            level_mapping = {0: 'Low', 1: 'Medium', 2: 'High'}
            predicted_level = level_mapping.get(prediction, "Unknown")

            # Survival percentage
            survival_ranges = {
                'Low': '70% - 90%',
                'Medium': '50% - 70%',
                'High': '30% - 50%'
            }
            survival_percentage = survival_ranges.get(predicted_level, "N/A")

            # Display results
            st.subheader("Prediction Results")
            st.write(f"**Predicted Cancer Level:** {predicted_level}")
            st.write(f"**Estimated Survival Percentage:** {survival_percentage}")

            # Optional: Show probabilities
            st.subheader("Prediction Probabilities")
            prob_df = pd.DataFrame({
                'Level': ['Low', 'Medium', 'High'],
                'Probability (%)': np.round(prediction_proba * 100, 2)
            })
            st.write(prob_df)

            # Visualize probabilities
            st.subheader("Probability Distribution")
            st.bar_chart(prob_df.set_index('Level'))
        else:
            st.error("Error in preprocessing the input data.")

if __name__ == '__main__':
    main()
