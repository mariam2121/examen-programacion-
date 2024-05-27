import requests
from bs4  import BeautifulSoup


input('ingrese la ciudad que decea ver los datos meterealogicos: ') 
url = 'https://api.openweathermap.org/data/3.0/onecall?temp={temp}&humidity={humidity}&exclude={descrption}&appid=es&hl=es-419&prev=search&u=https://home.openweathermap.org/api_keys" target'


response = requests.get(url)

if response.status_code == 200:
    date = response.json()
    print(f"la temperatura: {date['temp']}")
    print(f"la humedad: {date['humidity']}")
    print(f"la descripcion del clima: {date['description']}")
    print(f" la sensacion termica: {date['']}")
else:
    print("error en la info")



