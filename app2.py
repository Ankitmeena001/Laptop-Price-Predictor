import streamlit as st
import pickle
import numpy as np
import pandas as pd

# -----------------------
# Load the trained model
# -----------------------
# Make sure 'pipe.pkl' is in the same folder as this app.py
pipe = pickle.load(open('pipe.pkl', 'rb'))

# -----------------------
# Streamlit UI
# -----------------------
st.set_page_config(page_title="💻 Laptop Price Predictor", page_icon="💸", layout="centered")

st.title("💻 Laptop Price Predictor")
st.write("Predict the price of a laptop based on its specifications.")

# -----------------------
# Input fields
# -----------------------
company = st.selectbox("Brand", ['Dell', 'HP', 'Apple', 'Asus', 'Acer', 'Lenovo', 'MSI', 'Other'])
type_ = st.selectbox("Type", ['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible', 'Workstation'])
ram = st.selectbox("RAM (in GB)", [4, 8, 16, 32, 64])
weight = st.number_input("Weight of the laptop (kg)", min_value=0.5, max_value=5.0, step=0.1)
touchscreen = st.selectbox("Touchscreen", ['No', 'Yes'])
ips = st.selectbox("IPS Display", ['No', 'Yes'])
screen_size = st.number_input("Screen Size (in inches)", min_value=10.0, max_value=20.0, step=0.1)
resolution = st.selectbox("Screen Resolution", ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])
cpu = st.selectbox("CPU Brand", ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Other Intel', 'AMD Processor'])
hdd = st.selectbox("HDD (in GB)", [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox("SSD (in GB)", [0, 128, 256, 512, 1024])
gpu = st.selectbox("GPU Brand", ['Intel', 'Nvidia', 'AMD'])
os = st.selectbox("Operating System", ['Windows', 'Mac', 'Others/No OS/Linux'])

# -----------------------
# Prediction
# -----------------------
if st.button("Predict Price 💰"):
    # Preprocess inputs
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2 + Y_res ** 2) ** 0.5) / screen_size

    # Convert to DataFrame or array depending on your model
    query = pd.DataFrame([[
        company, type_, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os
    ]], columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'Ips', 'Ppi', 'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'])

    # Predict
    predicted_price = int(np.exp(pipe.predict(query)[0]))  # if model trained on log(price)

    st.success(f"💸 Predicted Laptop Price: ₹{predicted_price:,}")

# -----------------------
# Footer
# -----------------------
st.caption("Made with ❤️ using Streamlit")








