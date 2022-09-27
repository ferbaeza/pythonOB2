import requests
from pprint import pprint
import os
from dotenv import load_dotenv
import json



def main():
    load_dotenv()
    print("Ejercicio Cuatro")
    print("**************")
    city = str(input("Introduce la ciudad que desea consultar : "))
    API = os.getenv('API')
    URL = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API
    query = requests.get(URL)
    code = query.status_code
    print(f"\nStatus code: {code}\n\n")
    data = query.json()
    p_max= int(data['main']['temp_max'])
    temp_max = round(p_max-273.15, 2)
    p_min= data['main']['temp_min']
    temp_min= round(p_min-273.15,2)
    print(f"La ciudad seleccionada es {city} y tiene una T_Max de {temp_max} y T_Min de {temp_min}\n")

    #pprint(data)



if __name__=="__main__":
    main()