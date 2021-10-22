import pandas as pd

de_youtube = pd.read_csv("data/DEvideos.csv")
gb_youtube = pd.read_csv("data/GBvideos.csv")

#print (de_youtube.shape)
#print (gb_youtube.shape)

# Show all column names
# print (de_youtube[0:0])


# Concat data
# --------------
# concat accepts only one argument so put everything in a list!
# concat_data = pd.concat([de_youtube, gb_youtube])
# print (concat_data.shape)

# Join (Combines datasets based on a common column)
# --------------
# Combines DataFrames with common index and joins elements together along an axis.

left = de_youtube.set_index(['title'])
right = gb_youtube.set_index(['title'])

joined_data = left.join(right, lsuffix='_DE', rsuffix='_GB')
print (joined_data[0:0])
print (left.shape)
print (right.shape)
print (joined_data.shape)


# Column 'title' has been removed and serves as an index now?
# Why it says "Index: []" when using the type function?
# How can I show the index?
# print (type(joined_data))

# Merge

merged_data= pd.merge(left,right,on='title')
print(left.shape, right.shape)
print(joined_data.shape, merged_data.shape)