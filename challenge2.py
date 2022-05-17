from unittest import result
import requests
from datetime import datetime
from pprint import pprint
APP_KEY = 'eaeda91363msh2c47905a2399d98p13f800jsndfddc4f51231'
url = 'https://community-open-weather-map.p.rapidapi.com/weather'

def weather_data(city):
		query = {'q':city}
		headers= {
		'X-RapidAPI-Host': 'community-open-weather-map.p.rapidapi.com',
		'X-RapidAPI-Key': APP_KEY
		}
		res = requests.get(url,headers=headers, params=query)
		# capeprint(res.json())
		return res.json()
def display_weather(result,city):
		print("-----------Location------------------ ")
		print( result["name"], result["sys"]["country"])
		print("-------------Date:--------------------- ")
		print("Sunrise: ", datetime.fromtimestamp(result["sys"]["sunrise"]))
		print("Sunset: ", datetime.fromtimestamp(result["sys"]["sunset"]))
		print("-------------------------Weather-------------------------")
		print("Description: {}".format(result['weather'][0]['description']))
		print("Weather: {}".format(result['weather'][0]['main']))
		print("--------------------------Temperature------------------ ")
		print("Current temperature: {}°C ".format(round(result['main']['temp']-273.15, 2)))
		print("Max Temperature: {}°C ".format(round(result['main']['temp_max']-273.15,2)))
		print("Min Temperature: {}°C ".format(round(result['main']['temp_min']-273.15,2)))
		print("--------------------------Wind------------------ ")
		print("Wind speed: {} m/s".format(result['wind']['speed']))
		
		
def main():
	city=input('Enter the city:')
	try:
		w_data = weather_data(city)
		display_weather(w_data, city)
		print()
	except Exception as exception:
		print("City not found", exception)
if __name__=='__main__':
	main()