import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/world-population.csv")
fig,ax = plt.subplots()

world_countries = data['country']
world_population = data['pop2021']


x = world_countries
y = world_population


ax.bar(x, y)
plt.show()