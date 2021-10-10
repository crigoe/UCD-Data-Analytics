import pandas as pd

airbnb_data = pd.read_csv('data/AB_NYC_2019.csv')

# Show names of all columns
print (airbnb_data[0:0])

# Show number of rows and columns
print (airbnb_data.shape)

# Show missing values in columns
missing_values_count = airbnb_data.isnull().sum()
print(missing_values_count[:])

# Create Pandas DataFrame and show values for specific field
show_me = pd.DataFrame(airbnb_data)
print (show_me['minimum_nights'])
