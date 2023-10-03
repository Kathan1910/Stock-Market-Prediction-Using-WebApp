import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load model function
def load_model(ticker):
    with open(f'models/processed_{ticker}_MODEL.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Make prediction function (you'll need to adjust this based on your model and data)
def make_prediction(model, date_range):
    # Load the data for the selected date range (adjust as needed)
    # data = load_data_for_date_range(date_range)
    # predictions = model.predict(data)
    # For simplicity, let's assume random predictions here
    import numpy as np
    predictions = np.random.rand(len(date_range))
    return predictions

st.title('Stock Market Prediction App')

# Dropdown for ticker selection
tickers = [
    "ASIANPAINT", "AXISBANK", "BAJAJ-AUTO", "BAJFINANCE", 
    "BAJAJFINSV", "BHARTIARTL", "DRREDDY", "HCLTECH", 
    "HDFC", "HDFCBANK", "HEROMOTOCO", "HINDUNILVR", 
    "ICICIBANK", "INDUSINDBK", "INFY", "ITC", 
    "KOTAKBANK", "LT", "M&M", "MARUTI", "NESTLEIND", 
    "NTPC", "ONGC", "POWERGRID", "RELIANCE", "SBIN", 
    "SUNPHARMA", "TATAMOTORS", "TATASTEEL", "TCS", "TECHM"
]
# Add all your tickers here
selected_ticker = st.selectbox('Select a ticker:', tickers)

# Date range selection
start_date = st.date_input('Start date')
end_date = st.date_input('End date')

if st.button('Predict'):
    model = load_model(selected_ticker)
    date_range = pd.date_range(start_date, end_date)
    predictions = make_prediction(model, date_range)
    
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(date_range, predictions, label='Predictions', color='blue')
    plt.title(f'Predictions for {selected_ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(plt)

