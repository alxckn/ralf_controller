# -*- coding: utf-8 -*-
import json
import urllib2
import sys

class meteo:

    def __init__(self,ville):
        
        self.ville = ville
        self.temps = ''
        self.temp_min = ''
        self.temp_max = ''
        self.longitude = 0
        self.latitude = 0
        self.dico_today = {'Thunderstorm':'le temps est orageux','Rain':'il pleut','Clouds':'le ciel est couvert','Clear':'il fait beau'}
        self.dico_forecast = {'Thunderstorm':'le temps sera orageux','Rain':'il pleuvra','Clouds':'le ciel sera couvert','Clear':'il fera beau'}
        self.list_day = ['Aujoud\'hui','Demain','Après-demain']

        if self.ville == '':
            self.getCoord()

    def annonce(self):
        
        phrase = ''

        for i in range(0,3):

            self.getMeteo(i)
            if i==0:
                if self.temps != '':
                    phrase += self.list_day[i] + ', '
                    phrase += self.dico_today[self.temps]
                    phrase += ', et la temperature est comprise entre '
                    phrase += str(self.temp_min)
                    phrase += ' et '
                    phrase += str(self.temp_max)
                    phrase += ' degre Celsius. '
            else:
                if self.temps != '':
                    phrase += self.list_day[i] + ', '
                    phrase += self.dico_forecast[self.temps]
                    phrase += ', et la temperature sera comprise entre '
                    phrase += str(self.temp_min)
                    phrase += ' et '
                    phrase += str(self.temp_max)
                    phrase += ' degre Celsius. '

        return(phrase)

    def getMeteo(self,jour):

        self.temps = ''
        self.temp_min = ''
        self.temp_max = ''

        if self.ville != '':
        
            self.getWithCity(jour)

        else:
            
            self.getWithCoord(jour)

    def getWithCity(self,jour):        

        if jour == 0:

            url = 'http://api.openweathermap.org/data/2.5/weather?q='
            url += self.ville
            url += '&units=metric'

            parsed_json = self.recupJson(url)

            self.temps = parsed_json['weather'][0]['main']
            self.temp_min = int(parsed_json['main']['temp_min'])
            self.temp_max = int(parsed_json['main']['temp_max']) + 1

        else:

            url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q='
            url += self.ville
            url += '&cnt=2&units=metric'

            parsed_json = self.recupJson(url)

            self.temps = parsed_json['list'][jour-1]['weather'][0]['main']
            self.temp_min = int(parsed_json['list'][jour-1]['temp']['min'])
            self.temp_max = int(parsed_json['list'][jour-1]['temp']['max']) + 1 

    def getWithCoord(self,jour):

        if jour == 0:

            url = 'http://api.openweathermap.org/data/2.5/weather?lat='
            url += str(self.latitude)
            url += '&lon='
            url += str(self.longitude)
            url += '&units=metric'

            parsed_json = self.recupJson(url)

            self.temps = parsed_json['weather'][0]['main']
            self.temp_min = int(parsed_json['main']['temp_min'])
            self.temp_max = int(parsed_json['main']['temp_max']) + 1

        else:

            url = 'http://api.openweathermap.org/data/2.5/forecast/daily?lat='
            url += str(self.latitude)
            url += '&lon='
            url += str(self.longitude)
            url += '&units=metric&cnt=2'

            parsed_json = self.recupJson(url)

            self.temps = parsed_json['list'][jour-1]['weather'][0]['main']
            self.temp_min = int(parsed_json['list'][jour-1]['temp']['min'])
            self.temp_max = int(parsed_json['list'][jour-1]['temp']['max']) + 1            



    def getCoord(self):
        url = 'http://www.telize.com/geoip'

        parsed_json = self.recupJson(url)

        self.longitude = parsed_json['longitude']
        self.latitude = parsed_json['latitude']

    def recupJson(self,url):
        try:
            page_json = urllib2.urlopen(url)
            json_string = page_json.read()
            parsed_json = json.loads(json_string)
            page_json.close()

            return parsed_json

        except:
            print('Je n\'arrive pas à récupérer les données')
            sys.exit(2)


