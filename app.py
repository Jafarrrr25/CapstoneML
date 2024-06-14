from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

app = Flask(__name__)

# Load the model
model = load_model('credit_risk_model.h5')

# Initialize the scaler
scaler = StandardScaler()

# Define the columns to be normalized
columns_to_normalize = ['duration', 'amount', 'installment_rate', 'present_residence', 'age', 'number_credits', 'people_liable']

# Ensure the StandardScaler is fitted before running the app
# Load your original data to fit the scaler
original_data_path = "convert_numeric.csv"
if os.path.exists(original_data_path):
    original_data = pd.read_csv(original_data_path, delimiter=",")
    X = original_data.drop('credit_risk', axis=1)
    scaler.fit(X[columns_to_normalize])
else:
    raise FileNotFoundError(f"Data file {original_data_path} not found.")

@app.route('/')
def home():
    return "Credit Risk Model API"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Convert the data to DataFrame
        input_data = pd.DataFrame(data, index=[0])
        
        # Check if all required columns are present
        required_columns = set(columns_to_normalize)
        if not required_columns.issubset(input_data.columns):
            missing_columns = required_columns - set(input_data.columns)
            return jsonify({'error': f'Missing columns: {missing_columns}'}), 400
        
        # Normalize the input data
        input_data[columns_to_normalize] = scaler.transform(input_data[columns_to_normalize])
        
        # Reshape the input data for the model
        input_data_reshaped = input_data.values.reshape(input_data.shape[0], input_data.shape[1], 1)
        
        # Predict using the loaded model
        prediction = model.predict(input_data_reshaped)
        
        # Convert prediction to class
        predicted_class = (prediction > 0.5).astype(int).flatten()
        
        # Return the prediction as JSON
        return jsonify({'prediction': predicted_class.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=8080)
