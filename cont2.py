# -*- coding: utf-8 -*-
class controleur:

    def __init__(self, dic_action, dic_objet, fonctions):
        """Définition des attributs du controleur"""

        self.input = ""
        self.dic_action = dic_action
        self.dic_objet = dic_objet
        self.fonctions = fonctions
        
    def commande(self):
        """Création de la commande à partir de l'analyse de la string en entrée (utilise la méthode analyse)"""
        texte = ""
        do = self.analyse(self.input,self.dic_action)
        what = self.analyse(self.input,self.dic_objet)
        if do != False and what != False:
            texte = "self.fonctions." + do + "_" + what + "()"
            exec(texte)
        else:
            self.fonctions.fonction_erreur()

    def analyse(self, phrase, dico):
        """Traitement d'une phrase a partir des dictionnaires de mots créés"""
        mots = phrase.split()
        act = ""
        for mot in mots:
            if len(mot) < 4:
                if mot in dico:
                    act = dico[mot]
                    break
            else:
                for i in range(4,len(mot)+1):
                    cle = mot[:i]
                    if cle in dico:
                        act = dico[cle]
                        break
                if act != "":
                    break
        if act != "":
            return act
        else:
            return False
