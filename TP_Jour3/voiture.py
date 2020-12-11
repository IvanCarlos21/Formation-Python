

class Voiture:
    def __init__(self):
        self._roues = 4
    #getter
    @property
    def roues(self):
        print('recuperation des roues')
        return self._roues
    #setter
    @roues.setter
    def roues(self, r):
        print("changement du nombre de roues")
        self._roues = r
    
#programme principal
ma_voiture = Voiture()
print(ma_voiture.roues)
ma_voiture.roues = 5
print(ma_voiture.roues)

#fonction dir pour avoir l'apercu des methodes de l'objet
print(dir(ma_voiture))
#attribut __dict__donne les valeurs des attributs
print(ma_voiture.__dict__)