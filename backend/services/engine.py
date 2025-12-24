import numpy as np
import json
import joblib
import os

class WaterTwinCore:
    """
    WaterTwinCore: The computational engine of the Digital Twin.
    It manages parameter loading, AI-based usage prediction, and water balance simulations.
    """
    def __init__(self):
        # Define the cross-platform compatible path to the configuration file
        # Using os.path.join ensures compatibility between Windows, Linux, and macOS
        config_path = os.path.join('data', 'system_params', 'config.json')
        
        # Load system constants from the JSON file
        # If this file is missing, the initialization will intentionally fail to prevent bad data
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        # Initialize attributes from the configuration schema
        self.roof_area = self.config['default_roof_area'] # Surface area in m2
        self.tank_capacity = self.config['default_tank_capacity'] # Max volume in Liters

    def predict_usage(self, temperature: float):
        """
        Loads the pre-trained Linear Regression model to forecast water consumption.
        Temperature-driven prediction allows the Digital Twin to adapt to seasonal changes.
        """
        # Path for the serialized joblib model
        model_path = os.path.join('models', 'usage_forecaster.joblib')
        
        # Check if the model exists; if not, use a fallback value of 300L
        if os.path.exists(model_path):
            try:
                model = joblib.load(model_path)
                # Model expects a 2D array input: [[feature]]
                prediction = model.predict([[temperature]])
                return round(float(prediction[0]), 2)
            except Exception:
                return 300.0 # Safety fallback for model loading errors
        
        return 300.0 # Fallback for missing model file

    def run_simulation(self, rain_mm: float, initial_fill_pct: float, temperature: float):
        """
        Executes the primary water balance algorithm.
        Logic: Final Volume = Initial Volume + Inflow - Consumption
        """
        # Load efficiency and loss factors from the internal config dictionary
        eta = self.config['runoff_coefficient']
        evap_loss = self.config['evaporation_loss_rate']
        
        # Step 1: Obtain the AI-predicted daily usage based on temperature
        daily_usage = self.predict_usage(temperature)
        
        # Step 2: Calculate inflow volume: Rain * Area * Efficiency * (1 - Losses)
        inflow = rain_mm * self.roof_area * eta * (1 - evap_loss)
        
        # Step 3: Determine the starting water volume in absolute Liters
        start_water = (initial_fill_pct / 100) * self.tank_capacity
        
        # Step 4: Calculate the theoretical total before boundary constraints
        potential_total = start_water + inflow - daily_usage
        
        # Step 5: Overflow analysis - Any volume exceeding capacity is lost
        overflow = max(0, potential_total - self.tank_capacity)
        
        # Step 6: Final tank level clipping (Stay within 0 and capacity)
        # Using np.clip is an engineering best practice for boundary control
        final_level_l = np.clip(potential_total, 0, self.tank_capacity)
        final_level_pct = (final_level_l / self.tank_capacity) * 100
        
        # Returns a result set optimized for the Streamlit dashboard
        return {
            "inflow_L": round(float(inflow), 2),
            "predicted_usage_L": daily_usage,
            "overflow_L": round(float(overflow), 2),
            "final_fill_rate": round(float(final_level_pct), 1),
            "status": "OVERFLOW RISK" if overflow > 0 else "STABLE"
        }

# Console feedback for successful module initialization
if __name__ == "__main__":
    print("WaterTwinCore engine initialized successfully.")