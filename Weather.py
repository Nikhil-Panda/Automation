import requests

API_KEY = "API KEY HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a City Name:")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
#forming the api link to fetch data about the city's weather

response = requests.get(request_url)
#sending a get request to the url formed above

if response.status_code == 200:
    data = response.json()
    weather=data['weather'][0]['description']
    print("Weather:", weather)
    temparature = round(data['main']['temp'] - 273.15, 2)
    print("Temparature:",temparature,"Celsius")
else:
    print("Error Occured")
    print("status code:", response.status_code)
    print("response content", response.content)
    

