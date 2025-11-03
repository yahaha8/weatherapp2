import requests
API_KEY="d77233f4939c5a7b515b33d023f5d934"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"
city=input("enter the city name:")

url=f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response=requests.get(url)
data=response.json()
if data["cod"]==200:
    n=data["name"]
    w=data["weather"][0]["description"]
    m1=data["main"]["temp_min"]
    m2=data["main"]['temp_max']
    m3=data["main"]['pressure']
    m4=data["main"]['humidity']
    y=data["wind"]['speed']
    sunr=data["sys"]['sunrise']
    suns=data["sys"]['sunset']
print(f"name={n},\nweather={w},\ntemp_min={m1}degcelcius,\ntemp_max={m2}degcelcius,\npressure={m3},\nhumidity={m4},\nwind speed={y},\nsunrise={sunr},\nsunset={suns}")



 

#print(data)

    