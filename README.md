# TrackTempML: Live Weather Forecast

## Project Overview

TrackTempML is a machine learning-based weather forecasting system that uses real-time sensor data to predict various weather parameters. The system combines Arduino-based hardware sensors with scikit-learn machine learning models to provide accurate local weather predictions.

## Features

- Real-time temperature and humidity readings using DHT11 sensor
- Machine learning models trained on a dataset of approximately 50,000 entries
- Predictions for:
  - Precipitation Type (e.g., Rain)
  - Wind Speed
  - Visibility
  - Apparent Temperature
  - Atmospheric Pressure
- Customizable hyperparameters for model optimization

## Hardware Requirements

- Arduino board
- DHT11 temperature and humidity sensor
- Necessary wiring and connections

## Software Requirements

- Python 3.x
- Arduino IDE
- Required Python libraries (specified in requirements.txt)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Super-cod/TrackTempML-Live-Weather-Forecast.git
   cd TrackTempML-Live-Weather-Forecast
   ```

2. Install required Python libraries:
   ```
   pip install -r requirements.txt
   ```

3. Upload the Arduino sketch to your Arduino board using the Arduino IDE.

4. Connect the DHT11 sensor to your Arduino board according to the pin configuration in the Arduino sketch.

## Usage

1. Verify serial input from the sensor:
   ```
   python prediction_port.py
   ```
   This will check if the sensor data is being received correctly.

2. Train the models:
   Run all the model training files to load and process the dataset. This step may take some time depending on your system's performance.

3. Start the main prediction script:
   ```
   python main.py
   ```
   The script will initialize the models (which may take a moment) and then start taking live readings from the sensor to predict weather parameters.

<img src="./data/output%20image/Screenshot%202024-10-05%20020719.png" alt="OUTPUT" width="450" height="390">


## Customization

You can adjust the hyperparameters in the model training files to potentially increase the accuracy of the predictions. Experiment with different settings to find the optimal configuration for your specific use case.

## Dataset

The models are trained on a dataset of approximately 50,000 weather records. The dataset is included in the project as a data file. To use the dataset:

1. Locate the data file in the project directory (usually named something like `weather_data.csv` or `dataset.csv`).
2. Ensure that your model training scripts are correctly configured to read from this data file.
3. If you want to use your own dataset, replace the existing data file with your own, making sure to maintain the same format and column names.

The data file contains historical weather information including temperature, humidity, precipitation, wind speed, visibility, and pressure readings. This rich dataset allows the models to learn complex weather patterns and make accurate predictions.

## Contributing

Contributions to improve TrackTempML are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.
