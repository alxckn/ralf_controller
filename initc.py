# -*- coding: utf-8 -*-
class initc:

    def __init__(self):
        self.dic_action = {}
        self.dic_objet = {}
        action = ["pren","captur"]
        for i in action:
            self.dic_action[i] = 'take'
        action = ["ouvr","ouve","voir","consult","donn"]
        for i in action:
            self.dic_action[i] = 'open'
        action = ["dis","dire","parle"]
        for i in action:
            self.dic_action[i] = 'say'
        action = ["montre","démontre","démonstration"]
        for i in action:
            self.dic_action[i] = 'show'
        objet = ["photo","image"]
        for i in objet:
            self.dic_objet[i] = 'picture'
        objet = ["video","film"]
        for i in objet:
            self.dic_objet[i] = 'video'
        objet = ["mail","email","messa"]
        for i in objet:
            self.dic_objet[i] = 'mail'
        objet = ["meteo","temp","soleil","pluie","pleu"]
        for i in objet:
            self.dic_objet[i] = 'wheather'
        objet = ["lumière","yeux"]
        for i in objet:
            self.dic_objet[i] = 'eyes'
        objet = ["quelque","chose","mot"]
        for i in objet:
            self.dic_objet[i] = 'smth'
