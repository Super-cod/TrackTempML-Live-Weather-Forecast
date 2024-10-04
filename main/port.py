import serial
import time

# Open the serial port (adjust 'COM3' and baud rate as needed)
ser = serial.Serial('COM3', 9600)
time.sleep(2) 

sensor_data = []


serial_inputs = 0

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        print(f"Received: {line}") 

        if line.startswith("Data: [") and line.endswith("]"):
            # Extract the data between brackets
            data_str = line[line.find("[") + 1 : line.rfind("]")]
            data_str = data_str.strip()  

            # Split the data string and convert to float
            try:
                temperature, humidity = map(float, data_str.split(","))
            except ValueError as e:
                print(f"Error converting data to float: {e}")
                continue  

            if len(sensor_data) < 10:
                sensor_data.append([temperature, humidity])
            else:
                sensor_data.pop(0)  
                sensor_data.append([temperature, humidity])  

            print(f"Stored: {sensor_data[-1]}")  

            
            serial_inputs += 1

            
            if serial_inputs >= 10:
                break

except KeyboardInterrupt:
    
    print("Exiting...")

finally:
    
    ser.close()
    print("Serial port closed.")


avg_temperature = sum(data[0] for data in sensor_data) / len(sensor_data)
avg_humidity = sum(data[1] for data in sensor_data) / len(sensor_data)


print(f"Average Temperature: {avg_temperature:.2f} °C")
print(f"Average Humidity: {avg_humidity:.2f} %")