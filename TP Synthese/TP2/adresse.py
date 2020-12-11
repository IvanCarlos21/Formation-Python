#coding:utf8

class Adresse:
    #constructeur
    def __init__(self,rue,ville,codePostal):
        self.__rue = rue
        self.__ville = ville
        self.__codePostal = codePostal

    #getter // rue
    @property
    def rue(self):
        print('recuperation du nom de la rue')
        return self.__rue
    #setter
    @rue.setter
    def rue(self, r):
        print("changement du nom de la rue")
        self.__rue = r
    
    #getter // codePostal
    @property
    def codePostal(self):
        print('recuperation du code postal')
        return self.__codePostal
    #setter
    @codePostal.setter
    def codePostal(self, cdp):
        print("changement du nom de la rue")
        self.__rue = cdp

    #getter // ville
    @property
    def ville(self):
        print('recuperation du nom de la ville')
        return self.__ville
    #setter
    @ville.setter
    def ville(self, v):
        print("changement du nom de la ville")
        self.__ville = v

