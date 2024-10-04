import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

class WindSpeedModel:
    def __init__(self):
        self.model = RandomForestRegressor(random_state=42)
        self.train_model()

    def train_model(self):
        data = pd.read_csv(r"data\Book1.csv")
        columns_to_keep = ["Temperature (C)", "Humidity", "Wind Speed (km/h)"]
        filtered_data = data[columns_to_keep].dropna(subset=["Wind Speed (km/h)"])
        filtered_data["Wind Speed (km/h)"] = filtered_data["Wind Speed (km/h)"].round()

        X = filtered_data.drop("Wind Speed (km/h)", axis=1)
        y = filtered_data["Wind Speed (km/h)"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    def predict(self, temperature, humidity):
        input_data = [[temperature, humidity]]
        return self.model.predict(input_data)[0]
