import csv
import pandas as pd
import matplotlib.pyplot as plt
import time

# Function to read CSV data
def read_csv_data(filename):
    return pd.read_csv(filename)

# Initialize the plot outside the function
data = read_csv_data("data.csv")
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Plot each column and add text boxes for latest data
plots = {}
latest_texts = {}
for i, label in enumerate(["Steps", "Temperature", "Humidity"]):
    plots[label], = axs[i].plot(data.index, data[label])
    axs[i].set_title(label)
    axs[i].set_xlabel("Time")
    axs[i].set_ylabel(label)

    # Add textbox to display latest data
    latest_texts[label] = axs[i].text(0.5, -0.15, f"Latest {label}: {data[label].iloc[-1]}", transform=axs[i].transAxes,
                ha='center', fontsize=10, bbox=dict(facecolor='lightgray', alpha=0.5))

# Main function
def main():
    while True:
        update_data_and_plot()
        time.sleep(5)

# Function to update data and plot
def update_data_and_plot():
    global data
    # Read data from CSV
    new_data = read_csv_data("data.csv")

    # Update plot data
    for label in ["Steps", "Temperature", "Humidity"]:
        plots[label].set_data(new_data.index, new_data[label])

        # Update latest data textbox
        latest_texts[label].set_text(f"Latest {label}: {new_data[label].iloc[-1]}")

    # Update the limits of the x-axis if necessary
    if new_data.index.max() > axs[0].get_xlim()[1]:
        axs[0].set_xlim(new_data.index.min(), new_data.index.max())

    # Redraw the plot
    plt.pause(0.1)

# Call the main function
if __name__ == "__main__":
    main()
