import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Import matplotlib for plotting
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

class VisibilityModel:
    def __init__(self):
        self.model = RandomForestRegressor(random_state=42)
        self.train_model()

    def train_model(self):
        data = pd.read_csv(r"data\Book1.csv")
        columns_to_keep = ["Temperature (C)", "Humidity", "Visibility (km)"]
        filtered_data = data[columns_to_keep].dropna(subset=["Visibility (km)"])
        filtered_data["Visibility (km)"] = filtered_data["Visibility (km)"].round()

        X = filtered_data.drop("Visibility (km)", axis=1)
        y = filtered_data["Visibility (km)"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

       
        self.plot_results(X_train, y_train)

    def plot_results(self, X, y):
        plt.figure(figsize=(10, 6))
        
      
        plt.scatter(X["Temperature (C)"], y, color='blue', label='Actual Visibility', alpha=0.5)

   
        temperature_range = np.linspace(X["Temperature (C)"].min(), X["Temperature (C)"].max(), 100)
        humidity_avg = X["Humidity"].mean()
        
     
        visibility_pred = self.model.predict(np.column_stack((temperature_range, [humidity_avg] * len(temperature_range))))

        
        plt.plot(temperature_range, visibility_pred, color='red', label='Predicted Visibility', linewidth=2)

        plt.title('Visibility Prediction')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Visibility (km)')
        plt.grid(True)
        plt.show()

    def predict(self, temperature, humidity):
        input_data = [[temperature, humidity]]
        return self.model.predict(input_data)[0]
