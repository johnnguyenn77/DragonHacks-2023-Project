from tkinter import *
from datetime import datetime
import pip._vendor.requests as requests
from make_draggable import make_draggable
import geocoder
from PIL import ImageTk, Image  

class weather_widget:
    global img1
    def time_format_for_location(utc_with_tz):
        local_time = datetime.utcfromtimestamp(utc_with_tz)
        return local_time.time()
    
    def __init__(self, root):
        def time_format_for_location(utc_with_tz):
            local_time = datetime.utcfromtimestamp(utc_with_tz)
            return local_time.time()
        
        def showWeather(self):
            #Enter you api key, copies from the OpenWeatherMap dashboard
            api_key = "7a050779e88d874aee40ae9332caf333"  #sample API
            g = geocoder.ip('me')
            result = g.address
            result = result.split(', ')
            # Get city name from user from the input field (later in the code)
            city_name = result[0]
 
            # API url
            weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
            # Get the response from fetched url
            response = requests.get(weather_url)
 
            # changing response from json to python readable 
            weather_info = response.json()
 
            #self.tfield.delete("1.0", "end")   #to clear the text field for every new output
 
            #as per API documentation, if the cod is 200, it means that weather data was successfully fetched
            kelvin = 273 # value of kelvin
 
            #-----------Storing the fetched values of weather of a city
 
            temp = str(int(weather_info['main']['temp'] - kelvin)) + '°C' #converting default kelvin value to Celcius
            self.id = weather_info['weather'][0]['id']
            feels_like_temp = str(int(weather_info['main']['feels_like'] - kelvin)) + '°C'
            pressure = weather_info['main']['pressure']
            humidity = weather_info['main']['humidity']
            wind_speed = weather_info['wind']['speed'] * 3.6
            sunrise = weather_info['sys']['sunrise']
            sunset = weather_info['sys']['sunset']
            timezone = weather_info['timezone']
            cloudy = weather_info['clouds']['all']
            description = weather_info['weather'][0]['description']
            sunrise_time = time_format_for_location(sunrise + timezone)
            sunset_time = time_format_for_location(sunset + timezone)
 
            #assigning Values to our weather varaible, to display as output
         
            weather = f"Temperature: {temp}\nFeels like in: {feels_like_temp}\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time}\nSunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
            self.tfield.config(text = weather)
        
        self.frame = Frame(root, highlightbackground='white', highlightcolor= "white",highlightthickness=1, bg = "#222222")
        make_draggable(self.frame)
        self.frame.place(x=300, y=20)
        name = Label(self.frame, bg = '#222222', fg = '#66bfbf', text = 'Weather', font = ("Segoe UI Variable Display", 12)).pack(anchor = 'nw', pady=4)
        result_frame = Frame(self.frame, bd = 4, bg = "#222222")
        self.tfield = Label(result_frame, anchor='w', justify=LEFT, fg = 'white', font = ("Segoe UI Variable Display", 12), bg = '#222222')
        
        showWeather(self)
        
        global img1
        if int(self.id) in [200, 201, 202, 210, 211, 212, 221, 230, 231, 232]:
            img1 = Image.open("icon/11d.png")
            #image1 = Image.resize((50, 50), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img1)
        
        if int(self.id) in [300, 301, 302, 310, 311, 312, 313, 314, 321, 520, 522, 531]:
            img1 = Image.open("icon/09d.png")
            #image1 = Image.resize((50, 50), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img1)
            
        if int(self.id) in [500, 501, 502, 503, 504]:
            img1 = Image.open("icon/10d.png")
            #image1 = Image.resize((50, 50), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img1)

        if int(self.id) in [511, 600, 601, 602, 611, 612, 613, 615, 616, 620, 621, 622]:
            img1 = Image.open("icon/13d.png")
            #image1 = Image.resize((50, 50), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img1)

        if int(self.id) in [701, 711, 721, 731, 741, 751, 761, 762, 771, 781]:
            img1 = Image.open("icon/50d.png")
            #img1.resize((300, 300), Image.LANCZOS)
            img1 = ImageTk.PhotoImage(img1)

        if int(self.id) in [800]:
            img1 = Image.open("icon/01d.png")
            #image1 = Image.resize((50, 50), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img1)
            
        if int(self.id) in [801, 802, 803, 804]:
            img1 = Image.open("icon/03d.png")
            #img1.resize((300,20), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(Image.open("icon/03d.png"))
                    
        #to show output
        g = geocoder.ip('me')
        result = g.address
        result = result.split(', ')
        image = Label(result_frame, image = img1, bg = '#222222')
        close_btn = Button(self.frame, width = 3, text = 'x', fg = '#66fbfb', bd = 0, command = self.frame.place_forget, bg = '#222222', font = ("Segoe UI Variable Display", 12))
        close_btn.place(x = 216, y =0)
        weather_now = Label(self.frame, text = result[0]+', ' + result[1], fg = 'white', font = ("Segoe UI Variable Display", 12), bg = '#222222').pack(pady = 4, anchor = 'nw')
        self.tfield.pack(side = LEFT)     
        image.pack(side= RIGHT)
        result_frame.pack()
        
        
#root = Tk()
#root.configure(bg='#222222')
#root.geometry('1280x720')
#root.title("Your study space")

#weatherWidget = weather_widget(root)

#root.mainloop()
