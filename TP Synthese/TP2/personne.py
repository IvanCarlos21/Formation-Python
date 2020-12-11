#coding:utf8

class Adresse:
    #constructeur
    def __init__(self,nom,sexe,):
        self.__nom = nom
        self.__sexe = sexe
        self.__adresses = []

    #getter // nom
    @property
    def nom(self):
        print('recuperation du nom de la nom')
        return self.__nom
    #setter
    @nom.setter
    def nom(self, n):
        print("changement du nom de la nom")
        self.__nom = n
    
    #getter // sexe
    @property
    def sexe(self):
        print('recuperation du sexe')
        return self.__sexe
    #setter
    @sexe.setter
    def sexe(self, s):
        print("changement du nom du sexe")
        self.__nom = s

    #getter // adresse
    """
    @property
    def adresse(self):
        print('recuperation du nom de la adresse')
        return self.__adresse
    #setter
    @adresse.setter
    def adresse(self, v):
        print("changement du nom de la adresse")
        self.__nom = v
    
    """

