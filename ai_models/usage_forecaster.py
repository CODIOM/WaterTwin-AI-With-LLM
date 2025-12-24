import joblib
from sklearn.linear_model import LinearRegression
import numpy as np
import os

def train_consumption_model():
    """
    Trains a Linear Regression model to forecast water consumption based on 
    environmental temperature. This forms the predictive capability of the Digital Twin.
    """
    # Sample Data: [Air Temperature (°C)], [Water Consumption (Liters)]
    # Logic: As temperature rises, consumption increases due to factors like garden irrigation.
    X = np.array([[10], [15], [20], [25], [30], [35], [40]]).reshape(-1, 1)
    y = np.array([150, 180, 250, 350, 500, 700, 950])
    
    # Initialize the Linear Regression algorithm
    model = LinearRegression()
    
    # Fit the model to the training data to learn the relationship (weight and bias)
    model.fit(X, y)
    
    # Ensure the 'models' directory exists to prevent FileNotFoundError
    if not os.path.exists('models'):
        os.makedirs('models')
    
    # Persist the trained model using joblib for deployment in the Streamlit app
    joblib.dump(model, 'models/usage_forecaster.joblib')
    
    print("AI Consumption Model has been trained and saved to the 'models/' folder.")

if __name__ == "__main__":
    train_consumption_model()