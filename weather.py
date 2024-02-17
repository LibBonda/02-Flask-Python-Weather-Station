from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_current_weather(city="London"):
       
        request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=appid={os.getenv(API_KEY)}&q{city}&units=metric'
      
        weather_data = requests.get(request_url).json()
        return weather_data

if __name__ == "__main__":
            print('\n***Get Current Weather Conditions***\n')
    
            city = input("\nPlease enter a city name: ")
    
    #Check for empty strings or string with white spaces
if not bool(city.strip()):
            city = "London"
    
weather_data = get_current_weather(city)

print("\n")
print(weather_data)
    
    
        # def get_current_weather(city="London"):
        #     if not api_key:
        #         print("API_KEY environment variable is not set.")

        # return None
       
       # request_url = f"https://www.meteosource.com/api/v1/free/point?q=${city}&appid=${api_key}&units=metric" 
        
    
# request_url = f"https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${api_key}&units=metric"
    
    # request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=appid={os.getenv(API_key)}&q{city}&units=metric'

    # request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    # f'b1b15e88fa797225412429c1c50c122a1">api.openweathermap.org/data/2.5/forecast?id&appid={os.getenv("API_KEY")}
    # appid={os.getenv(API_KEY)}&q{city}&units=metric'
    
    
    
# request_url = f'https://api.openweathermap.org/data/2.5/weather?q=${*city*}&appid=${*API_KEY*}&units=metric'
    
#     weather_data=requests.get(request_url).json()
# # def get_current_weather (city="London"):
#     request_url=f'https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric'
    
#     weather_data=requests.get(request_url).json()