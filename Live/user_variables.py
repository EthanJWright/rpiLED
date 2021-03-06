import Weather_API
class User_Variables():
    def __init__(self):
        self.number_of_panels = 3
        self.api_call_interval = 300
        
        self.gpio = [None] * self.number_of_panels
        # RGB GPIO ports to be entered
        self.gpio[0] = (17, 22, 24)
        self.gpio[1] = (0, 0, 0)
        self.gpio[2] = (0, 0, 0)
       
       #Shift color scheme for temp
       #Default set to 40F = Purple 100F = Red
        self.weather_offset = 10  
        
      #Temp API variables
        self.tempAPI = Weather_API.Weather() 
        self.tempAPI.api_key = '52347449fab1dab5431fcbc264efcb19'
        self.tempAPI.latitude = '40.014984'
        self.tempAPI.longitude = '-105.270546'
