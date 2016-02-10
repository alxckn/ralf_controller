from met2 import meteo
from compliment import inutile
import random
from mailfinal import mail
##from class_led import led
##from class_led import led_control

class fonctionsc:

    def open_video(self):
        print("Quelle video voulez vous ouvrir?")
        video = raw_input()
        print("J'ouvre " + video + ".avi")

    def open_picture(self):
        print("Quelle photo voulez vous ouvrir?")
        picture = raw_input()
        print("J'ouvre " + picture + ".jpeg")

    def open_mail(self):
        text=mail().lisMail()

    def open_wheather(self):
        text=meteo('').annonce()
        print(text)

    def take_video(self):
        print("Je prends une video")

    def take_picture(self):
        print("Je prends une photo")

    def say_smth(self):
        test = random.randrange(0,10)

        if test < 8:
            text=inutile().complimente()
        else:
            text=inutile().cite()

##    def show_eyes(self):
##        GPIO.setmode(GPIO.BCM)
##        led_control().combinaison("rbj1,b2,r0.5")

    def fonction_erreur(self):

        text = 'Je n\'ai pas compris, par contre, '
        text += inutile().complimente()
