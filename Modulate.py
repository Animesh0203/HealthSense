import csv
import time
import random

# Function to append data to the CSV file
def append_to_csv(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Main function
def main():
    # Define the filename and the headers
    filename = 'data.csv'
    headers = ["Steps", "Temperature", "Humidity", "Time"]

    # Write headers to the CSV file if it's empty
    with open(filename, mode='r') as file:
        if not file.read(1):
            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)

    # Initialize step count
    steps = 0

    # Loop to add data every 5 seconds
    while True:
        # Increment steps
        steps += random.randint(1, 10)

        # Generate random temperature and humidity (within +-5 range)
        temperature = random.randint(16, 26)
        humidity = random.randint(75, 85)
        current_time = steps

        # Append data to the CSV file
        append_to_csv(filename, [steps, temperature, humidity, current_time])

        # Print confirmation message
        print("Data added to CSV file")

        # Wait for 5 seconds
        time.sleep(5)

# Call the main function
if __name__ == "__main__":
    main()
