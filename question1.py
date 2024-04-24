#Question 1. write python program to import crop.csv file and do the following task
#1. Draw scatter plot (we have data on the yield and rainfall for different crops in a region)
#2. Draw histogram to visualize the distribution of customer ages.
#3. Draw line plot to visualize the trend in crop yield for each crop.

import pandas as pd
import matplotlib.pyplot as plt

def scatter_plot(data):
    plt.scatter(data['Rainfall'], data['Yield'])
    plt.xlabel('Rainfall (mm)')
    plt.ylabel('Yield (kg/ha)')
    plt.title('Yield vs Rainfall')
    plt.show()


def histogram(data):
    plt.hist(data['Age'], bins=10, color='skyblue', edgecolor='black')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Distribution of Customer Ages')
    plt.show()


def line_plot(data):
    for crop in data['Crop'].unique():
        crop_data = data[data['Crop'] == crop]
        plt.plot(crop_data['Year'], crop_data['Yield'], label=crop)
    plt.xlabel('Year')
    plt.ylabel('Yield (kg/ha)')
    plt.title('Trend in Crop Yield')
    plt.legend()
    plt.show()


crop_data = pd.read_csv('crop.csv')

scatter_plot(crop_data)

histogram(crop_data)

line_plot(crop_data)
