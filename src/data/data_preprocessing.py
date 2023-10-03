import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
import numpy as np

def preprocess_data(df):
    # Handling Missing Values
    all_dates = pd.date_range(start=df.index.min(), end=df.index.max(), freq='B')
    df = df.reindex(all_dates)
    df.fillna(method='ffill', inplace=True)
    
    # Detecting and Handling Outliers
    rolling_mean = df['Close'].rolling(window=20).mean()
    rolling_std = df['Close'].rolling(window=20).std()
    upper_bound = rolling_mean + (2 * rolling_std)
    lower_bound = rolling_mean - (2 * rolling_std)
    df['Close'] = np.where((df['Close'] > upper_bound) | (df['Close'] < lower_bound), rolling_mean, df['Close'])
    
    # Standardization
    scaler = StandardScaler()
    df['Close_standardized'] = scaler.fit_transform(df[['Close']])
    
    # Log Transformation
    df['Close_log'] = np.log1p(df['Close'])
    
    # Date Features
    df['Day_of_Week'] = df.index.dayofweek
    df['Month'] = df.index.month
    df['Quarter'] = df.index.quarter
    df['Year'] = df.index.year
    
    # Normalize the index to remove time and timezone components
    df.index = df.index.normalize().tz_localize(None)


    return df

if __name__ == "__main__":
    input_directory = "data/raw/SENSEX/"
    output_directory = "data/processed/"
    
    for filename in os.listdir(input_directory):
        if filename.endswith(".csv"):
            input_filepath = os.path.join(input_directory, filename)
            output_filepath = os.path.join(output_directory, f"processed_{filename}")
            
            data = pd.read_csv(input_filepath, parse_dates=['Date'], index_col='Date')
            processed_data = preprocess_data(data)
            processed_data.reset_index(inplace=True)
            processed_data.rename(columns={"index": "Date"}, inplace=True)
            processed_data.to_csv(output_filepath)
