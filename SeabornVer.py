import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

# Function to read CSV data
def read_csv_data(filename):
    return pd.read_csv(filename, parse_dates=['Time'], index_col='Time')

# Initialize plot
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

# Main function
def main():
    while True:
        update_data_and_plot()
        time.sleep(5)

# Function to update data and plot
def update_data_and_plot():
    data = read_csv_data("data.csv")
    plt.clf()  # Clear previous plot
    sns.lineplot(data=data, dashes=False)
    plt.title("Real-Time Data Visualization")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend(title=None)
    plt.pause(0.1)

# Call the main function
if __name__ == "__main__":
    main()
