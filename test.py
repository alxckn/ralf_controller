from cont2 import controleur
from initc import initc
from fonctionsc import fonctionsc

initcontroleur = initc()
fonctionsc = fonctionsc()

cont = controleur(initcontroleur.dic_action,initcontroleur.dic_objet,fonctionsc)

while True:
    test = raw_input('Entrez quelque chose : ')
    cont.input = test
    cont.commande()
