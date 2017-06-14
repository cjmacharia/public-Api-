import requests  #import requests
import json   #import json
print ("Welcome" )

city = input("Enter A known City name: ")

api_key = ("077936f695f61908cd19a5a2452a97fb") #our public Api-key

response = requests.get("http://api.openweathermap.org/data/2.5/weather?q={0}&appid=077936f695f61908cd19a5a2452a97fb".format(city, api_key))  #api call

weather = response.json()

print ("The current weather in {0} is {1}".format(city, weather["weather"][0]["description"])  #the result
)
