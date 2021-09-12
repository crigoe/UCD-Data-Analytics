import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load datasets

# data1 = pd.read_csv ('intermediate/brics.csv')
# data2 = pd.read_csv ('intermediate/cars.csv')
# data3 = pd.read_csv ('intermediate/gapminder.csv')

x = [1923, 1945, 1966, 2021]
x_np = np.array(x)
y = [4534, 3455, 453443, 34355]
y_np = np.array(y)

plt.plot(x_np,y_np)
plt.show()