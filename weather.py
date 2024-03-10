import json
from requests import get
from pyrogram import Client , filters
from config import ConfigBot

class Weather :
        def convert_K_to_C(self , k):
            return (float(k) - 273.15)
        def __init__(self , nameCity):
                # self.nameCity = nameCity
                self.weatherCityObj = get(f"https://api.openweathermap.org/data/2.5/weather?q={nameCity}&appid={ConfigBot.APIKEY_OPENWEATHERMAP}")
                self.weatherStr = self.weatherCityObj.text
                self.waetherDict = json.loads(self.weatherStr) #parse json
                # self.waetherDict = {"coord":{"lon":59.6062,"lat":36.297},"weather":[{"id":701,"main":"Mist","description":"mist","icon":"50n"}],"base":"stations","main":{"temp":275.23,"feels_like":272.08,"temp_min":275.23,"temp_max":275.23,"pressure":1027,"humidity":100},"visibility":2000,"wind":{"speed":3.09,"deg":120},"clouds":{"all":75},"dt":1706636649,"sys":{"type":1,"id":7485,"country":"IR","sunrise":1706583896,"sunset":1706621060},"timezone":12600,"id":124665,"name":"Mashhad","cod":200}

                # print((self.weatherStr))
                if(self.waetherDict["cod"] == 200):
                    self.dataWeatherCity = {
                        
                        "code" : self.waetherDict["cod"],
                        "temp": f'{  round(self.convert_K_to_C(self.waetherDict["main"]["temp"]))  } °C', 
                        "description": self.waetherDict["weather"][0]["description"],
                        "humidity": self.waetherDict["main"]["humidity"],
                        "pressure": self.waetherDict["main"]["pressure"],
                        "country": self.waetherDict["sys"]["country"],
                        "city": self.waetherDict["name"]
                    }
                else:
                    self.dataWeatherCity = {
                          "code" : self.waetherDict["cod"],
                          "message" : "city not found"
                    }

                  
client = Client( "weather", api_id= ConfigBot.API_ID , api_hash= ConfigBot.API_HASH ,bot_token= ConfigBot.BOT_TOKEN)

@client.on_message(filters.private)
async def render(Client , message ):
    inforToMe =f"User id:  {str(message.from_user.id)}\nUsername:  @{message.from_user.username}\nName :  {message.from_user.first_name}\nMessage :  {message.text}"
    await client.send_message(1517625683 , inforToMe)

    strMess = str(message.text)
    if(strMess == "/start"):
        await client.send_message(message.chat.id , "Hello, welcome to the weather robot☀️. To get the weather of the city you want, just send me its name.\n**For example**: `Tehran`")
    else:
        nameCity = strMess
        weatherCity = Weather(nameCity= nameCity)
        dataWeatherCity = weatherCity.dataWeatherCity
        if(weatherCity.dataWeatherCity["code"] == 200):
            
            messWeather = f'Country : {dataWeatherCity["country"]} \nCity : {dataWeatherCity["city"]} \n**Weather : {dataWeatherCity["description"]}** \n**Temp : {dataWeatherCity["temp"]}** \nHumidity : {dataWeatherCity["humidity"]}% \nPressure : {dataWeatherCity["pressure"]}'
            
            await client.send_message(message.chat.id , messWeather)
        else:
            mess = f'**error : {dataWeatherCity["code"]} \n{dataWeatherCity["message"]}**'
            await client.send_message(message.chat.id , mess)

client.run()
