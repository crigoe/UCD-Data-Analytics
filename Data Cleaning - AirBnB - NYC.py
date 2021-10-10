import pandas as pd

airbnb_data = pd.read_csv('data/AB_NYC_2019.csv')
print (airbnb_data[0:0])
print (airbnb_data.shape)

missing_values_count = airbnb_data.isnull().sum()
print(missing_values_count[:])

# DataFrame
show_me = pd.DataFrame(airbnb_data)
print (show_me['minimum_nights'])
