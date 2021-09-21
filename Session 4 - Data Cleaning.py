import pandas as pd
import numpy as np

netflix_data= pd.read_csv("netflix_titles.csv")
print(netflix_data.head())
print(netflix_data.shape)

missing_values_count = netflix_data.isnull().sum()
print(missing_values_count[:])

# Drop rows with missing values
#droprows= netflix_data.dropna()
#print(netflix_data.shape,droprows.shape)

# Drop columns with missing values
# dropcolumns = netflix_data.dropna(axis=1)
# print(netflix_data.shape,dropcolumns.shape)
# print (dropcolumns[0:0])

# Fill all missing values with 0
# cleaned_data = netflix_data.fillna(0)
# print (cleaned_data.isnull().sum())

# Fill all missing values to the value that comes next in the same column
cleaned_data = netflix_data.fillna(method='bfill', axis=0).fillna(0)

# drop duplicates
drop_duplicates = netflix_data.drop_duplicates()
print(netflix_data.shape,drop_duplicates.shape)

# drop duplicated of specific col

drop_duplicates= netflix_data.drop_duplicates(subset=['show_id'])
print(netflix_data.shape,drop_duplicates.shape)