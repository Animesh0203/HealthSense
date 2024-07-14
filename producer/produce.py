from kafka import KafkaProducer
import time
import csv
import json

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='YOUR_KAFKA_SERVER:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Replace this function with actual sensor data reading
def read_sensor_data():
    # Example sensor data
    data = {
        'timestamp': time.time(),
        'sensor1': 23.5,
        'sensor2': 48.1
    }
    return data

# Send data to Kafka topic
def send_data():
    while True:
        data = read_sensor_data()
        producer.send('sensor_data', data)
        time.sleep(5)  # Adjust the sleep time as needed

if __name__ == "__main__":
    send_data()
