from kafka import KafkaConsumer
import csv
import json

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'sensor_data',
    bootstrap_servers='YOUR_KAFKA_SERVER:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='sensor_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Define CSV file to store the data
csv_file = 'sensor_data.csv'

# Open the CSV file for writing
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['timestamp', 'temperature', 'humidity'])

    # Consume messages from Kafka
    for message in consumer:
        data = message.value
        # Write the data to CSV
        writer.writerow(
            [data['timestamp'], data['temperature'], data['humidity']])
