import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class PrecipitationModel:
    def __init__(self):
        self.model = RandomForestClassifier(random_state=42)
        self.train_model()

    def train_model(self):
        data = pd.read_csv(r"data\Book1.csv")
        columns_to_keep = ["Temperature (C)", "Humidity", "Precip Type"]
        filtered_data = data[columns_to_keep].dropna(subset=["Precip Type"])
        filtered_data["Precip Type"] = filtered_data["Precip Type"].replace({"rain": 0, "snow": 1})

        X = filtered_data.drop("Precip Type", axis=1)
        y = filtered_data["Precip Type"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    def predict(self, temperature, humidity):
        input_data = [[temperature, humidity]]
        prediction = self.model.predict(input_data)
        return "Rain" if prediction[0] == 0 else "Snow"
