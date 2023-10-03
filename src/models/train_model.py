import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

# Directory paths
data_directory = "data/processed/"
models_directory = "models/"

# Ensure models directory exists
if not os.path.exists(models_directory):
    os.makedirs(models_directory)

# List all processed data files
files = [f for f in os.listdir(data_directory) if f.endswith('.csv')]

for file in files:
    # Load data
    data_path = os.path.join(data_directory, file)
    data = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')
    
    # Split data
    X = data.drop('Close', axis=1)
    y = data['Close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    # Train model (using Random Forest as an example)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save model
    ticker_symbol = file.split('.')[0]  # Assuming file name is the ticker symbol
    model_path = os.path.join(models_directory, f"{ticker_symbol}_model.pkl")
    joblib.dump(model, model_path)

print("All models trained and saved!")
