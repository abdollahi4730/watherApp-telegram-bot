class ConfigBotWeather:
    
    def __init__(self ,API_ID ,API_HASH ,BOT_TOKEN , APIKEY_OPENWEATHERMAP ):
        self.API_ID =   API_ID
        self.API_HASH =  API_HASH
        self.BOT_TOKEN =  BOT_TOKEN
        self.APIKEY_OPENWEATHERMAP =  APIKEY_OPENWEATHERMAP

# get these from my.telegram.org
api_id = ""
api_hash = ""
bot_token = "" # get from bot father in telegram

apiKey_openweatherMap = "" # get it from https://openweathermap.org/ 

ConfigBot = ConfigBotWeather( API_ID= api_id , API_HASH= api_hash , BOT_TOKEN= bot_token , APIKEY_OPENWEATHERMAP= apiKey_openweatherMap )
