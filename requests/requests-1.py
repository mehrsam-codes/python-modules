import requests

city = "London" # your city 
url = f"https://wttr.in/{city}?format=3" #your api

response = requests.get(url)

print(response.text)