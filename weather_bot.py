def weather(location):
    import os
    import requests
    import json
    from dotenv import load_dotenv
    
    load_dotenv()
    WTOKEN = os.getenv('WEATHER_TOKEN')
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'
    url2 = url.format(location,WTOKEN)
        


    response = requests.get(url2)
    response.raise_for_status()
        
    #add message here upon failure of request
    #Load JSON data into Python variable
    weatherData = json.loads(response.text)
    #print(weatherData)


    #print(type(weatherData))
    main = weatherData['weather'][0]['main']
    ktemp = weatherData['main']['temp']
    temp = int((ktemp - 273.15) * 9/5 + 32)
    response = (f"The current weather in {location} is {main} with a temp of {temp} degrees.")
    return(response)
   
    
    
