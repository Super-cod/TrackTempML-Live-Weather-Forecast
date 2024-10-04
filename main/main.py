import numpy as np
import serial
import time
import pandas as pd
from precipitation_model import PrecipitationModel
from wind_speed_model import WindSpeedModel
from visibility_model import VisibilityModel
from app_temp import app_temp
from presure import pressure

def get_sensor_data():
    ser = serial.Serial('COM3', 9600)

    sensor_data = []
    serial_inputs = 0

    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line.startswith("Data: [") and line.endswith("]"):
                data_str = line[line.find("[") + 1: line.rfind("]")]
                data_str = data_str.strip()

                try:
                    temperature, humidity = map(float, data_str.split(","))
                except ValueError:
                    continue

                print(f"Recorded - Temperature: {temperature:.2f} °C, Humidity: {humidity:.2f} %")

                if len(sensor_data) < 20:
                    sensor_data.append([temperature, humidity])
                else:
                    sensor_data.pop(0)
                    sensor_data.append([temperature, humidity])

                serial_inputs += 1
                if serial_inputs >= 20:
                    break

    except KeyboardInterrupt:
        pass

    finally:
        ser.close()

    avg_temperature = sum(data[0] for data in sensor_data) / len(sensor_data)
    avg_humidity = sum(data[1] for data in sensor_data) / len(sensor_data)

    return avg_temperature, avg_humidity, sensor_data

def main():
    precip_model = PrecipitationModel()
    wind_model = WindSpeedModel()
    visibility_model = VisibilityModel()
    app_model=app_temp()
    pressure_model=pressure()

    avg_temperature, avg_humidity, sensor_data = get_sensor_data()


    precip_prediction = precip_model.predict(avg_temperature, avg_humidity)
    wind_prediction = wind_model.predict(avg_temperature, avg_humidity)
    visibility_prediction = visibility_model.predict(avg_temperature, avg_humidity)
    app_predict=app_model.predict(avg_temperature, avg_humidity)
    pressure_predict=pressure_model.predict(avg_temperature, avg_humidity)

    df_sensor_data = pd.DataFrame(sensor_data, columns=['Temperature (°C)', 'Humidity (%)'])

    print("\nRecorded Temperature and Humidity Data:")
    print(df_sensor_data)

    print(f"\nAverage Temperature: {avg_temperature:.2f} °C")
    print(f"Average Humidity: {avg_humidity:.2f} %")
    print(f"\nPredicted Precipitation Type: {precip_prediction}")
    print(f"Predicted Wind Speed: {wind_prediction:.2f} km/h")
    print(f"Predicted Visibility: {visibility_prediction:.2f} km")
    print(f"Apparent Temperature (C): {app_predict:.2f} °C")
    print(f"Pressure (millibars): {pressure_predict:.2f} millibars\n")
    

if __name__ == "__main__":
    main()
