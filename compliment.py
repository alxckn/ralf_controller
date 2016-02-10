#!/usr/local/bin/python
# -*- coding: cp1252 -*-

import random

class inutile:

    def __init__(self):
        self.compliments=['accompli','admirable','adorable','agréable','aimable','angélique','artistique','bellissime','bien','bien','tourné','bon','brillant','calme','céleste','charmant']
        self.citations=['Une noisette, j\'la casse entre mes fesses tu vois','Une femme qui est enceinte, par exemple, elle est aware qu\'elle attend un enfant','Pour moi le reve - et pour tout le monde, meme si les gens ne le savent pas (et meme s\'ils ne le savent pas, ils le savent), le reve, it\'s a feeling, c\'est une sensation, une sensation reelle qui se produit si on veut']

    def complimente(self):
        
        nombre = random.randrange(0,len(self.compliments))

        phrase = 'Tu es ' + self.compliments[nombre]

        return phrase

    def cite(self):

        nombre = random.randrange(0,len(self.citations))
        return self.citations[nombre]

