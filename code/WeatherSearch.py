import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import datetime as dt
from fmiopendata.wfs import download_stored_query

"""csv tiedoston hakee koodin tekijä. Käyttäjä EI VOI TÄTÄ TEHDÄ. Tiedosto on haettu
ilmatieteenlaitoksen verkkosivuilta. https://en.ilmatieteenlaitos.fi/download-observations. 
Nimetty Weather_Data202212_1h.csv ja tallenettiin samaan kansioon koodin kanssa. Koneluettava
haku löytyy samasta verkkoympäristöstä. https://www.ilmatieteenlaitos.fi/avoin-data 
csv tiedosto tammikuu 2023. Ohjelman haut 1 - 6 tästä aineistosta """

#df = pd.read_csv('Weather_Data202301_1h.csv')
df = pd.read_csv('Weather_Data202212_1h.csv')
df = df[:-1] # pandas cut last rows

seekresults = []

class WeatherResult:
    def results_seek(self, seekresults):

        yearmonth_result = checkyear_month()
        for weather in seekresults:
            print()
            print("*****************************")
            print(f"Sään haku tulokset:")                 
            print("Ilmatieteen laitos (OpenData) Oulunsalo Pellonpään mittausasema")
            print("***************************************************************")
            print(f"{weather.seekid}. Haku {weather.day}.{yearmonth_result[0]} {yearmonth_result[1]} kello {weather.time}")
            print(f"{weather.print_seek()}")
            print()
        
class WeatherSeek():
    def __init__(self, seekid, day, time):
        self.seekid = seekid
        self.day = day
        self.time = time


    def ask_day(self):
        def day_check():
            while True:
                try:
                    day = int(input("Anna haku päivä (1-31): ")) 
                    if day >= 1 and day <= 31: 
                        return int(day) 
                    else:
                        print()
                        print("Virheellinen syöte. Anna oikea päivä, kiitos.")
                        print()
                except ValueError:
                    print()
                    print("Virheellinen syöte. Anna luku, kiitos.")
                    print()
        self.day = day_check()    

    def ask_time(self):
        while True:
            time = str(input("Anna haun kellon aika(HUOM! haku aika tasa tunnein 00:00 muodossa): "))
            result = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00",
            "12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]
            timetemp = []
            timetemp.append(time)
            if any(same_value in result for same_value in timetemp): # jos sama arvo löytyy molemmista taulukoista klo syöte ok. 
                self.time = time
                break
            else:
                print()
                print("Virheellinen syöte kellon ajassa")
                print()

class Temperature(WeatherSeek):
    def __init__(self, seekid, day, time, temperature_results):
        super().__init__(seekid, day, time)
        self.temperature_result = temperature_results

    def make_seek(self):
        
        day_1 = df[df["Time"] == self.time] # pandas taulukko parsitaan annetulla klo arvolla
        day_2 = day_1[day_1["d"] == self.day] #parsitaan annetulla paivan arvolla  
    
        a = day_2["Air temperature (degC)"] # valitaan parsitulta riviltä lämpötila
        a = (a.to_string(index=False)) # Tulostuksen muotoilu pandas taulukon indeksi numerointi pois
        temperature_results = (f"Lämpötila {a} astetta")
        self.temperature_result = temperature_results 

    def print_seek(self):
        return self.temperature_result

class Rainfall(WeatherSeek):
    def __init__(self, seekid, day, time, rainfall_results):
        super().__init__(seekid, day, time)
        self.rainfall_result = rainfall_results

    def make_seek(self):
        day_1 = df[df["Time"] == self.time]
        day_2 = day_1[day_1["d"] == self.day]

        a = day_2["Precipitation amount (mm)"]
        a = (a.to_string(index=False))
        rainfall_results = (f"Sademäärä {a} mm")
        self.rainfall_result = rainfall_results

    def print_seek(self):
        return self.rainfall_result

class WindSpeed(WeatherSeek):
    def __init__(self, seekid, day, time, windspeed_results):
        super().__init__(seekid, day, time)
        self.windspeed_result = windspeed_results
        
    def make_seek(self):
        day_1 = df[df["Time"] == self.time]
        day_2 = day_1[day_1["d"] == self.day]

        a = day_2["Wind speed (m/s)"]
        a = (a.to_string(index=False))
        windspeed_results = (f"Tuulen nopeus {a} m/s")
        self.windspeed_result = windspeed_results

    def print_seek(self):
        return self.windspeed_result

class GustWind(WeatherSeek):
    def __init__(self, seekid, day, time, gustwind_results):
        super().__init__(seekid, day, time)
        self.gustwind_result = gustwind_results
       
    def make_seek(self):
        day_1 = df[df["Time"] == self.time]
        day_2 = day_1[day_1["d"] == self.day]

        a = day_2["Gust speed (m/s)"]
        a = (a.to_string(index=False))
        gustwind_results = (f"Tuuli puuskassa {a} m/s")
        self.gustwind_result = gustwind_results

    def print_seek(self):
        return self.gustwind_result  

class WindDirection(WeatherSeek):
    def __init__(self, seekid, day, time, winddirection_results):
        super().__init__(seekid, day, time)
        self.winddirection_result = winddirection_results
        
    def make_seek(self): 
        day_1 = df[df["Time"] == self.time]
        day_2 = day_1[day_1["d"] == self.day]

        a = day_2["Wind direction (deg)"]
        a = int(a.to_string(index=False)) # vaihdetaan muuttujan int tyyppi if hakua varten

        if (a >= 338) or (a <= 22): # Pohjoinen 338 - 360 tai 0 - 22
            winddirection_results = (f"Pohjoistuulta suunnasta {a} astetta")       
        elif (a >= 23) and (a <= 67): # Koillinen 23 - 67
            winddirection_results = (f"Koillistuulta suunnasta {a} astetta") 
        elif (a >= 68) and (a <= 112): # Itä 68 - 112
            winddirection_results = (f"Itätuulta suunnasta {a} astetta")
        elif (a >= 113) and (a <= 157): # Kaakko 113 - 157
            winddirection_results = (f"Kaakkoistuulta suunnasta {a} astetta")
        elif (a >= 158) and (a <= 202): # Etelä 158 - 202
            winddirection_results = (f"Etelätuulta suunnasta {a} astetta")
        elif (a >= 203) and (a <= 247): # Lounas 203 - 247
            winddirection_results = (f"Lounaistuulta suunnasta {a} astetta")
        elif (a >= 248) and (a <= 292): # Länsi 248 - 292
            winddirection_results = (f"Länsituulta suunnasta {a} astetta")
        elif (a >= 293) and (a <= 337): # Luode 293 - 337  
            winddirection_results = (f"Luoteistuulta suunnasta {a} astetta")
        else:
            winddirection_results = (f"Tuuli suunnasta {a} astetta")
       
        self.winddirection_result = winddirection_results

    def print_seek(self):
        return self.winddirection_result

def temperature_statistic():

    day_1 = df[df["Time"] == "12:00"] # pandas taulukko parsitaan annetulla klo arvolla
    a = day_1["Air temperature (degC)"] #
    temperature_result = a.to_numpy()# method to concert column to numpy array

    #print(temperature_result)
    fig1, ax = plt.subplots()
    fig1 ,ax.set_xlim(1, 31)
    ax.set_title("Kuukauden päivä lämpötila kello 12:00")
    ax.set_xlabel("Päivät")
    ax.set_ylabel('Lämpötila')
                
    xpoints = np.array(temperature_result)
    ypoints = np.array(([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 
                    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]))
    plt.plot(ypoints, xpoints)

    return(plt.plot)

def weather_machineseek():
    end_time = dt.datetime.now()
    end_time = end_time - dt.timedelta(minutes=130)
    output_time = end_time
    start_time = end_time - dt.timedelta(minutes=1)
    start_datetime = start_time.isoformat(timespec="seconds") + "Z"
    end_datetime = end_time.isoformat(timespec="seconds") + "Z" # ->  2020-07-07T12:00:00Z
    output_datetime = output_time.isoformat(timespec="seconds")

    obs = download_stored_query(f"fmi::observations::weather::multipointcoverage&fmisid=101786&starttime={start_datetime}&endtime={end_datetime}&")
    
    latest_tstep = max(obs.data.keys())
    temperature_value = obs.data[latest_tstep]["Oulu lentoasema"]["Air temperature"]['value']
    wind_value = obs.data[latest_tstep]["Oulu lentoasema"]["Wind speed"]['value']

    root = tk.Tk()
    root.title('Tulostus tiedot')
    root.iconbitmap('saa_kuva.ico')
    root.geometry('300x200+50+50')
    message = tk.Label(root, text = f"Aika: {output_datetime}")
    message1 = tk.Label(root, text = f"Oulun lentoaseman lämpötila {temperature_value} astetta")
    message2 = tk.Label(root, text = f"Oulun lentoaseman tuulen nopeus {wind_value} m/s")         
    message.pack()
    message1.pack()
    message2.pack()

    return(root)

def checkyear_month():
        
    month = (df.m.head(1)) 
    month = str(month.to_string(index=False))
    year = (df.Year.head(1))  
    year = str(year.to_string(index=False))
   
    return month, year

def main():
    yearmonth_result = checkyear_month()
    seekid = 1

    while True:
        def intcount():
            while True:
                try:
                    print()
                    print(f"Ilmatieteen laitos (OpenData) Oulunsalo Pellonpään mittausasema")
                    print(f"Tilasto kuukausi {yearmonth_result[0]} vuosi {yearmonth_result[1]}")
                    valuenumber = int(input("Anna halutun mittaustuloksen numero:\n(1) Lämpötila\n(2) Sademäärä\n(3) Tuulen nopeus\n(4) Tuuli puuskassa\n\
(5) Tuulen suunta\n(6) Diagrammi tilasto kuukauden päivä lämpötiloista (kello 12:00)\n(7) Lämpötila ja tuulen nopeus Oulun Lentoasema(machine search)\n\
(0) Lopetus ja tulostus\n"))
                    return int(valuenumber)
                except ValueError:
                    print()
                    print("Virheellinen syöte. Anna luku, kiitos.")
                    print()
        searchtype = intcount() 
        
        if searchtype == 1:
            weather = Temperature(seekid, 0 , "", "")
            Temperature.ask_day(weather)
            Temperature.ask_time(weather)
            Temperature.make_seek(weather)
            seekresults.append(weather)
            seekid += 1
        elif searchtype == 2:
            weather = Rainfall(seekid, 0 , "", "")
            Rainfall.ask_day(weather)
            Rainfall.ask_time(weather)
            Rainfall.make_seek(weather)
            seekresults.append(weather)
            seekid += 1
        elif searchtype == 3:
            weather = WindSpeed(seekid, 0 , "", "")
            WindSpeed.ask_day(weather)
            WindSpeed.ask_time(weather)
            WindSpeed.make_seek(weather)
            seekresults.append(weather)
            seekid += 1
        elif searchtype == 4:
            weather = GustWind(seekid, 0 , "", "")
            GustWind.ask_day(weather)
            GustWind.ask_time(weather)
            GustWind.make_seek(weather)
            seekresults.append(weather)
            seekid += 1
        elif searchtype == 5:
            weather = WindDirection(seekid, 0 , "", "")
            WindDirection.ask_day(weather)
            WindDirection.ask_time(weather)
            WindDirection.make_seek(weather)
            seekresults.append(weather)
            seekid += 1
        elif searchtype == 6:
            plt.plot = temperature_statistic()
            plt.show()
        elif searchtype == 7:
            root = weather_machineseek()
            root.mainloop() # keep the window displaying
        elif searchtype == 0:
            break
        else:
            print()
            print("Virheellinen valinta. Anna oikea haku numero kiitos.")
            print()

    Printout = WeatherResult()
    Printout.results_seek(seekresults)

#Program Start main() function
if __name__ == "__main__":
    main()
