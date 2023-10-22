import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('receipt_forecast_model.h5')

month_dict = {
    "January" : 1, "February":2 , "March":3 , "April":4, "May":5, "June":6, 
    "July":7, "August":8, "September":9, "October":10, "November":11, "December":12
}

def get_key(dictionary, target_value):
    return [key for key, value in dictionary.items() if value == target_value][0]


st.set_option('deprecation.showPyplotGlobalUse', False)

st.write("""
# Fetch Rewards: Monthly Receipt Count Forecaster
*Monthly Receipt Counts in the year 2021*
""")

# Load the data
data_daily = pd.read_csv("data_daily.csv")
data_daily['# Date'] = pd.to_datetime(data_daily['# Date'])
data_monthly = data_daily.groupby(data_daily['# Date'].dt.to_period("M"))['Receipt_Count'].sum().reset_index()
data_monthly.columns = ['Month', 'Receipt_Count']

# Convert 'Month' column to string for visualization purposes
data_monthly['Month'] = data_monthly['Month'].astype(str)

max_val = data_monthly['Receipt_Count'].max()
min_val = data_monthly['Receipt_Count'].min()
data_normalized = (data_monthly['Receipt_Count'] - min_val) / (max_val - min_val)

# Initialize the forecast with the last sequence from the training data
forecast = data_normalized[-3:].tolist()
# Create columns for side-by-side layout
col1, col2 = st.columns(2)

# In the first column, display the plot
with col1:
    # Create the plot
    plt.figure(figsize=(6, 6))
    plt.plot(data_monthly['Month'], data_monthly['Receipt_Count'], marker='o', linestyle='-')
    plt.title('Monthly Receipt Counts for 2021')
    plt.xlabel('Month')
    plt.ylabel('Receipt Count')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot()

# In the second column, display the data_monthly table
with col2:
    st.write(data_monthly)


with st.sidebar:
    st.title("2022 Monthly Receipt Count Forecaster: ")
    st.markdown("---")
    st.write("*How it works:*")
    st.write("when you select a Month in 2022, the forecaster will predict all the Receipt counts from January to the selected month")
    st.write("*Note:* By default January 2022 is selected and its prediction is given")
    st.markdown("---")
    month = st.selectbox("Select Month in 2022 to forecast:", ["January", "February", "March", "April", "May", "June", 
                                           "July", "August", "September", "October", "November", "December"])
    # Predict next 12 months
    for _ in range(month_dict[month]):
        next_seq = model.predict(np.array([forecast[-3:]]))[0][0]
        forecast.append(next_seq)

    # Extract only the forecasted 12 months
    forecasted_values = forecast[-month_dict[month]:]

    # Denormalize the forecasted data
    forecast_denorm = np.array(forecasted_values) * (max_val - min_val) + min_val

    for i, value in enumerate(forecast_denorm):
        st.write("{}'s receipt count = {:.0f}".format(get_key(month_dict, i+1), value))
