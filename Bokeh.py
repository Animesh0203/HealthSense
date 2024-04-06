from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
import pandas as pd
import time

# Function to read CSV data
def read_csv_data(filename):
    return pd.read_csv(filename, parse_dates=['Time'], index_col='Time')

# Initialize Bokeh plot
source = ColumnDataSource(data=dict(time=[], steps=[], temperature=[], humidity=[]))
p = figure(title="Real-Time Data Visualization", x_axis_label="Time", y_axis_label="Value")

# Plot data
p.line(x='time', y='steps', source=source, line_color="blue", legend_label="Steps")
p.line(x='time', y='temperature', source=source, line_color="red", legend_label="Temperature")
p.line(x='time', y='humidity', source=source, line_color="green", legend_label="Humidity")

# Update data
def update():
    data = read_csv_data("data.csv")
    source.data = dict(time=data.index, steps=data['Steps'], temperature=data['Temperature'], humidity=data['Humidity'])

# Update every 5 seconds
curdoc().add_periodic_callback(update, 5000)

curdoc().title = "Real-Time Data Visualization"
curdoc().add_root(p)
