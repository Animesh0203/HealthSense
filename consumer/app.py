import streamlit as st
import pandas as pd
import time

# Path to the CSV file
csv_file = 'sensor_data.csv'

# Function to read the latest data from the CSV file


def read_latest_data():
    df = pd.read_csv(csv_file)
    latest_data = df.iloc[-1]
    return latest_data, df

# Streamlit app


def main():
    st.title("Real-Time Dashboard")

    # Layout
    col1, col2, col3 = st.columns(3)
    graph_col1, graph_col2 = st.columns(2)

    # Update data every 5 seconds
    while True:
        latest_data, df = read_latest_data()

        with col1:
            st.metric("Timestamp", latest_data['timestamp'])
        with col2:
            st.metric("Temperature (°C)", latest_data['temperature'])
        with col3:
            st.metric("Humidity (%)", latest_data['humidity'])

        with graph_col1:
            st.line_chart(df[['timestamp', 'temperature']].set_index(
                'timestamp'), use_container_width=True)
        with graph_col2:
            st.line_chart(df[['timestamp', 'humidity']].set_index(
                'timestamp'), use_container_width=True)

        time.sleep(5)  # Adjust the refresh rate as needed
        st.experimental_rerun()


if __name__ == "__main__":
    main()
