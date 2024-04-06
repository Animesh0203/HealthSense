import csv
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import time

# Function to read CSV data


def read_csv_data(filename):
    return pd.read_csv(filename)


# Initialize global figure
fig = make_subplots(rows=1, cols=3, subplot_titles=("Steps", "Temperature", "Humidity"))

# Update layout
fig.update_layout(title_text="Health Sense Dynamic Data Visualization", showlegend=True)

# Main function


def main():
    # Update data and plot every 5 seconds
    while True:
        update_data_and_plot()
        time.sleep(5)


def update_data_and_plot():
    # Read data from CSV
    data = read_csv_data("data.csv")

    # Clear existing traces
    fig.data = []

    # Update traces for Temperature and Humidity only
    for i, label in enumerate(["Temperature", "Humidity"]):
        fig.add_trace(go.Scatter(x=data.index, y=data[label], mode='lines', name=label), row=1, col=i+1)

    # Show plot
    fig.show()


# Call the main function
if __name__ == "__main__":
    main()
