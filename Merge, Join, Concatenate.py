import pandas as pd

de_youtube = pd.read_csv("data/DEvideos.csv")
gb_youtube = pd.read_csv("data/GBvideos.csv")

#print (de_youtube.shape)
#print (gb_youtube.shape)

# Concat data (concat accepts only one argument so put everything in a list!)
#concat_data= pd.concat([de_youtube, gb_youtube])
#print (concat_data)

# Join (Combines datasets based on a common column)


# Merge