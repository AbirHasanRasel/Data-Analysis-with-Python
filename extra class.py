"""specific column selection & calculate the mean & greater numbers of means &
 list down the greater number of means in a file"""
#Test 1
import numpy as np
import pandas as pd
data=pd.read_csv("GlobalLandTemperaturesByCity.csv")
# print(data)
# print(data.describe())
# print(data['AverageTemperature'].std())
averageTemp=data['AverageTemperature']
meanOfAvgTemp=np.mean(averageTemp)
print(meanOfAvgTemp)

# Filter values greater than the mean
greaterThanMean = averageTemp[averageTemp > meanOfAvgTemp]

# Print the filtered values
print("greater than mean",greaterThanMean)