import requests
import re
import matplotlib.pyplot as plt
import numpy as np

# api_key = VK0058OMSFF1Z60C

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=VK0058OMSFF1Z60C'
r = requests.get(url)
data = r.json()

# get value from specific field
date = "2021-10-08"
open = (data['Time Series (Daily)'][date]['1. open'])

print (open)
#output = re.findall("\d+-\d+-\d+","efeffeefefef")
#print (output)

