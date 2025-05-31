import streamlit as st
import pickle
import pandas as pd
import numpy as np


pipe=pickle.load(open('pipe.pkl','rb'))

st.markdown(
    """
    <style>
    .stApp {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<h1 style='color: white;'> Crop Yield Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown("""
This app predicts crop yield based on various parameters such as Rainfall, soil conditions, and other agricultural factors.
Fill in the information below to predict the expected yield for your crops.
""")

st.markdown(
    "<h3 style='color: white;'> Enter the Parameters for Prediction</h3>",
    unsafe_allow_html=True
)

Rf = st.number_input("Rain Fall (mm)",min_value=0)
fer = st.number_input("Fertilizer",min_value=0)
col1,col2,col3=st.columns(3)
with col1:
    Phos=st.number_input('Phosphorus (P)',min_value=0)
with col2:
    potas=st.number_input('Potassium (K)',min_value=0)
with col3:
    Nit=st.number_input('Nitrogen (N)',min_value=0)
    


if st.button("Predict Yield"):

    # Process the input data and make the prediction
    input_df= pd.DataFrame({'Rain Fall (mm)':[Rf],'Fertilizer':[fer],'Nitrogen (N)':[Nit],'Phosphorus (P)':[Phos],'Potassium (K)':[potas]})

    # This is where you'd implement the logic to display the prediction
    predicted_yield = pipe.predict(input_df)  # example model call

    st.subheader(f"Predicted Crop Yield: {predicted_yield[0]} tons/acers")
