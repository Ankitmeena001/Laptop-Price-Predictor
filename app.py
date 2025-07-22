import streamlit as st
import pandas as pd
import joblib

# Load model and any encoders or scalers
model = joblib.load('df.pkl')  # Replace with your actual model filename

# Title
st.title("💻 Laptop Price Predictor")
st.write("Fill in the specs below to predict laptop price.")

# User input fields
company = st.selectbox("Brand", ['Apple', 'Dell', 'HP', 'Lenovo', 'Acer', 'Asus', 'MSI', 'Other'])
type_name = st.selectbox("Laptop Type", ['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible', 'Netbook', 'Workstation'])
ram = st.selectbox("RAM (in GB)", [4, 8, 16, 32, 64])
weight = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, step=0.1)
touchscreen = st.selectbox("Touchscreen", ['No', 'Yes'])
ips = st.selectbox("IPS Display", ['No', 'Yes'])
screen_size = st.number_input("Screen Size (inches)", min_value=10.0, max_value=18.0, step=0.1)
resolution = st.selectbox("Screen Resolution", ['1920x1080', '1366x768', '3200x1800', '3840x2160', '1600x900'])

cpu = st.selectbox("CPU", ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'AMD Ryzen 5', 'AMD Ryzen 7', 'Other'])

hdd = st.number_input("HDD (in GB)", min_value=0, max_value=2000, step=128)
ssd = st.number_input("SSD (in GB)", min_value=0, max_value=2000, step=128)
gpu = st.selectbox("GPU Brand", ['Intel', 'Nvidia', 'AMD', 'Other'])
os = st.selectbox("Operating System", ['Windows', 'Mac', 'Linux', 'Others'])

# Convert 'Yes'/'No' to 1/0
touchscreen = 1 if touchscreen == 'Yes' else 0
ips = 1 if ips == 'Yes' else 0

# Convert resolution to PPI
x_res, y_res = map(int, resolution.split('x'))
ppi = ((x_res**2 + y_res**2) ** 0.5) / screen_size

# Construct input DataFrame
input_df = pd.DataFrame([[company, type_name, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]],
                        columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'IPS', 'PPI', 'Cpu', 'HDD', 'SSD', 'Gpu', 'OpSys'])

st.write("Input dataframe:", input_df)
st.write("Type of pipe:", type(pipe))
# Prediction
if st.button("Predict Price 💸"):
    prediction = pipe.predict(input_df)[0]
    st.success(f"Predicted Laptop Price: ₹{int(prediction):,}")
