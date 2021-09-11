# Import numpy
import numpy as np
import pandas as pd

# Get list np_heigh_in from baseball.csv

data = pd.read_csv ('baseball.csv')

height_in = data['Height'].tolist()
weight_in = data['Weight'].tolist()
age_in = data['Age'].tolist()


# Create a numpy arrays
np_height_in = np.array(height_in)
np_weight_in = np.array(weight_in)
np_age_in = np.array(age_in)


baseball = [np_height_in, np_weight_in]
np_baseball = np.array(baseball)

# Convert inch to m and lb to kg
np_height_m = np_height_in * 0.0254
np_weight_kg = np_weight_in * 0.453592

# Calculate BMI
bmi = np_weight_kg / np_height_m ** 2

# Define light
light = bmi < 21

# Print out the weight at index 50
# print (np_weight_kg[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
# print (np_height_m[100:111])

# print (np_baseball)

# Print out the shape of np_baseball
# print(np_baseball.shape)

