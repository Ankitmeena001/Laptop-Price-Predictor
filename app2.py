import streamlit as st
import pickle
import joblib
import numpy as np

# Load trained pipeline
with open('pipe.pkl', 'rb') as file:
    pipe = pickle.load("pipe.pkl")

# Load dataframe for dropdown options
with open('df.pkl', 'rb') as file:
    df = pickle.load(file)

st.title("💻 Laptop Price Predictor")

# Dropdowns
company = st.selectbox('Brand', df['Company'].unique())
type_ = st.selectbox('Type', df['TypeName'].unique())
ram = st.selectbox('RAM (in GB)', sorted(df['Ram'].unique()))
weight = st.number_input('Laptop Weight (kg)', min_value=0.5, max_value=5.0, step=0.1)

# Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
touchscreen = 1 if touchscreen == 'Yes' else 0

# IPS Panel
ips = st.selectbox('IPS Panel', ['No', 'Yes'])
ips = 1 if ips == 'Yes' else 0

# Screen size
screen_size = st.number_input('Screen Size (inches)', min_value=10.0, max_value=20.0, step=0.1)

# Resolution
resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

# CPU
cpu = st.selectbox('CPU', df['Cpu brand'].unique())

# HDD
hdd = st.selectbox('HDD (GB)', sorted(df['HDD'].unique()))

# SSD
ssd = st.selectbox('SSD (GB)', sorted(df['SSD'].unique()))

# GPU
gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())

# OS
os = st.selectbox('Operating System', df['os'].unique())

# Resolution to PPI function
def calculate_ppi(resolution, screen_size):
    x_res, y_res = map(int, resolution.split('x'))
    return ((x_res**2 + y_res**2) ** 0.5) / screen_size

# Predict button
if st.button('Predict Price'):
    ppi = calculate_ppi(resolution, screen_size)
    query = np.array([company, type_, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])
    query = query.reshape(1, 12)

    prediction = pipe.predict(query)[0]
    st.subheader(f"💰 Estimated Laptop Price: ₹ {np.exp(prediction):,.0f}")


