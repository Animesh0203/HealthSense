# Real-Time Sensor Data Dashboard

This project demonstrates how to set up a real-time sensor data dashboard using a Raspberry Pi, Apache Kafka, and Streamlit. The setup involves a Raspberry Pi that reads temperature and humidity data from a DHT11 sensor, a Kafka producer to send the data to a Kafka topic, a Kafka consumer to receive the data and store it in a CSV file, and a Streamlit app to visualize the data in real-time.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Kafka](#setup-kafka)
- [Producer Setup](#producer-setup)
- [Consumer Setup](#consumer-setup)
- [Streamlit Dashboard](#streamlit-dashboard)
- [Running the Project](#running-the-project)

## Prerequisites

1. Raspberry Pi with DHT11 sensor connected.
2. Apache Kafka installed and running.
3. Python installed on both the Raspberry Pi and the consumer machine.
4. Necessary Python packages installed.

## Setup Kafka

1. Download and install Kafka from [Apache Kafka](https://kafka.apache.org/downloads).
2. Start the Kafka server and create a topic named `sensor_data`.

```sh
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
bin/kafka-topics.sh --create --topic sensor_data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

## Producer Setup

```sh
pip install kafka-python adafruit-circuitpython-dht psutil
sudo apt-get install libgpiod2
```

## Consumer Setup

```sh
pip install kafka-python pandas
```

## Streamlit Dashboard

```sh
pip install streamlit pandas
```

## File Locations

1. Put the producer python file on the Raspberry and customize it according to the sensors you are using.
2. The consumer python file will be ran on the system.
3. To view the data in realtime put the app python file in the same folder as the consumer and run it.
4. Running only consumer python file without the app will just store all the data sent from the producer and can be viewed later.
