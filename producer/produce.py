from kafka import KafkaProducer
import time
import csv
import json
import board
import adafruit_dht
import psutil

temp = 0
humidity = 0

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='YOUR_KAFKA_SERVER:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Replace this function with actual sensor data reading
def read_sensor_data():
    # We first check if a libgpiod process is running. If yes, we kill it!
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()
    sensor = adafruit_dht.DHT11(board.D23)
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
    except RuntimeError as error:
        print(error.args[0])
        continue
    except Exception as error:
        sensor.exit()
        raise error
    return temp, humidity

# Send data to Kafka topic
def send_data():
    while True:
        temp, humidity = read_sensor_data()
        producer.send('Temp', temp)
        producer.send('Humidity', humidity)
        time.sleep(5)  # Adjust the sleep time as needed

if __name__ == "__main__":
    send_data()
