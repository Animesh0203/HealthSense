import pandas as pd
import matplotlib.pyplot as plt
import time

# Function to read CSV data


def read_csv_data(filename):
    return pd.read_csv(filename, parse_dates=['Timestamp'], index_col='Timestamp')

# Function to update data and plot


def update_data_and_plot():
    # Read data from CSV
    data = read_csv_data("Rasp/data.csv")

    # Clear previous plot
    plt.clf()

    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))

    # Plot Temperature
    axs[0].plot(data.index, data['Temp'])
    axs[0].set_title('Temperature')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Temperature (°C)')

    # Plot Humidity
    axs[1].plot(data.index, data['Humidity'])
    axs[1].set_title('Humidity')
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Humidity (%)')

    # Show plot
    plt.tight_layout()
    plt.pause(0.1)  # Pause briefly to update the plot

# Main function


def main():
    # Update data and plot every 5 seconds
    while True:
        update_data_and_plot()
        time.sleep(5)


# Call the main function
if __name__ == "__main__":
    main()
