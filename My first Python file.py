# Import numpy
import numpy as np
import pandas as pd

# Get list np_heigh_in from baseball.csv

data = pd.read_csv ('baseball.csv')

height_in = data['Height'].tolist()
weight_in = data['Weight'].tolist()

# Create a numpy arrays
np_height_in = np.array(height_in)
np_weight_in = np.array(weight_in)


# Convert inch to m and lb to kg
np_height_m = np_height_in * 0.0254
np_weight_kg = np_weight_in * 0.453592

# Calculate BMI
bmi = np_weight_kg / np_height_m ** 2
# Print BMI
print (bmi)