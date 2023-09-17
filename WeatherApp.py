import requests
import customtkinter as ctk

#window
window = ctk.CTk()
window.title('Weather App')
window = ctk.CTk(fg_color = ('#2EA5FF'))
window.geometry('500x700')
window.minsize(500,700)

api_key = '8bcc38ff25914f93d610bb90d8e96648'

def get_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    
    #moves entry to buttom of page
    entry.grid_configure(row = 9, column= 0,columnspan = 3, sticky= 'nsew', padx = 2, pady= 2)
    button.grid_configure(row = 9, column= 3, sticky= 'nsew', padx = 2, pady= 2)
    
    #assigning the information passed for the api call to variables
    temp = response['main']['temp']
    feels_like = response['main']['feels_like']
    humidity = response['main']['humidity']
    windspeed = response['wind']['speed']
    pressure = response['main']['pressure']
    
    location_label = ctk.CTkLabel(window, text=(city), font = ('Work Sans', 30))
    location_label.grid(row = 0, column= 0,columnspan = 4, sticky= 'nsew', padx = 2, pady= 2)

    #frames
    frame1 = ctk.CTkFrame(master=window, width=100, height=100, border_color= 'black', fg_color='#008DFF')
    frame2 = ctk.CTkFrame(master=window, width=100, height=100, border_color= 'black', fg_color='#008DFF')
    frame3 = ctk.CTkFrame(master=window, width=100, height=100, border_color= 'black', fg_color='#008DFF')
    frame4 = ctk.CTkFrame(master=window, width=100, height=100, border_color= 'black', fg_color='#008DFF')
    
    
    frame1.grid(row = 3, column = 0, sticky = 'nsew', padx = 5, pady = 5, columnspan = 2, rowspan=2)
    frame2.grid(row = 3, column = 2, sticky = 'nsew', padx = 5, pady = 5, columnspan = 2, rowspan = 2)
    frame3.grid(row = 5, column = 0, sticky = 'nsew', padx = 5, pady = 5, columnspan = 2, rowspan=2)
    frame4.grid(row = 5, column = 2, sticky = 'nsew', padx = 5, pady = 5, columnspan = 2, rowspan = 2)
    
    
    temp_label = ctk.CTkLabel(window, text=('Temperature: ' + str(round(temp - 273.15, 2))), font = ('Work Sans', 20))
    temp_label.grid(row = 1, column= 0,columnspan = 4, sticky= 'nsew', padx = 2)
    
    feels_like_text = ctk.CTkLabel(frame1, text='Feels like: ', font = ('Work Sans', 20))
    feels_like_num = ctk.CTkLabel(frame1, text=(str(round(feels_like - 273.15, 2))), font = ('Work Sans', 30))
    feels_like_text.pack(anchor = 'nw', padx = 10, pady = 10)
    feels_like_num.pack(expand = True, anchor = 'center')
    
    humidity_label_text = ctk.CTkLabel(frame2, text=('Humidity: '), font = ('Work Sans', 20))
    humidity_label_num = ctk.CTkLabel(frame2, text=(str(humidity) + '%'), font = ('Work Sans', 30))
    humidity_label_text.pack(anchor = 'nw', padx = 10, pady = 10)
    humidity_label_num.pack(expand = True, anchor = 'center')
      
    windspeed_label_text = ctk.CTkLabel(frame3, text=('Wind speed: '), font = ('Work Sans', 20))
    windspeed_label_num = ctk.CTkLabel(frame3, text=(str((windspeed*3600)/1200) + 'km/h'), font = ('Work Sans', 30))
    windspeed_label_text.pack(anchor = 'nw', padx = 10, pady = 10)
    windspeed_label_num.pack(expand = True, anchor = 'center')
    
    pressure_label_text = ctk.CTkLabel(frame4, text=('Pressure: '), font = ('Work Sans', 20))
    pressure_label_num = ctk.CTkLabel(frame4, text=(str(pressure) + 'hPa'), font = ('Work Sans', 30))
    pressure_label_text.pack(anchor = 'nw', padx = 10, pady = 10)
    pressure_label_num.pack(expand = True, anchor = 'center')
    
location = ctk.StringVar()

#entry widget
entry = ctk.CTkEntry(window, textvariable=location)
entry.insert(0, 'Type your location here')
#go button 
button = ctk.CTkButton(window, text="GO", command=lambda: get_weather(api_key, entry.get()))

entry.grid(row = 2, column= 0,columnspan = 3, sticky= 'nsew', padx = 2, pady= 2)
button.grid(row = 2, column= 3, sticky= 'nsew', padx = 2, pady= 2)

#grid configure
window.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
window.rowconfigure((0,1,2,3,4,5,6,7,8), weight = 1, uniform = 'a')

 
    
#run
window.mainloop()