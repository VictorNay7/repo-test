import pandas as pd
import requests

# Current: pulls in data from a weather api and dsiplays it
# Goal: add scanner functionality 

# URL to json data
apiUrl = ("https://goweather.herokuapp.com/weather/Augusta")

# GET data
response = requests.get(apiUrl).json()

# target temp
# convert temp from celcius to farenheit
temperature = response["temperature"]
temp_farenheit = ((int(temperature[0]+temperature[1])) * 9/5) + 32

# create dataframe from data
# convert dataframe to csv for future use.
df = pd.DataFrame(response.items())
df = df.to_csv()

print("It is " + str(temp_farenheit) + " degrees farenheit in Augusta, Maine.")
