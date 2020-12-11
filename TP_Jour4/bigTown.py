#coding:utf8

class Ville:
    def __init__(self, nomVille):
        self.nomVille = nomVille
        self.batiments = []

    #
    def afficher_nbre_batiments(self):
        print("la ville de {} possède {} batiments".format(self.nomVille, len(self.batiments)))

class Batiment:
    def __init__(self, nomBat):
        self.nomBat = nomBat
        self.employes = []

    #
    def afficher_nbre_employes(self):
        print("le batiment {} possède {} employes".format(self.nomBat, len(self.employes)))

class Entreprise:
    def __init__(self, nomEnt):
        self.nomEnt = nomEnt
        self.batiments = []
        self.villes = []
    #
    def afficher_nbre_batiments(self):
        print("l'entreprise' {} possède {} batiments".format(self.nomEnt, len(self.batiments)))
    #
    def afficher_nbre_villes(self):
        print("l'entreprise' {} possède {} villes".format(self.nomEnt, len(self.villes)))


class Employe:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
   


#programme principal

############################### iNSTANCIATION
#creation de l'entreprise
my_ent = Entreprise("kongossa")

#creation de deux villes
ville1 = Ville("Paris")
Ville2 = Ville("Madrid")

#creation de 3 batiments
bat1 = Batiment("Tour Socrates")
bat2 = Batiment("Tour R&D")
Bat3 = Batiment ("Batiment Administratif")

#ajout des villes à l'entreprise
ville1.batiments = [bat1, bat2]
Ville2.batiments = [Bat3]

my_ent.batiments = [bat1, bat2, Bat3]
my_ent.villes = [ville1, Ville2]

#creation de nouveaux employes
empl1 = Employe("Lampard", "Franck")
empl2 = Employe("Drogba", "Didier")
empl3 = Employe("Chip", "Chop")

bat2.employes = [empl2, empl1]
  
  

############################ TEST

my_ent.afficher_nbre_batiments()
my_ent.afficher_nbre_villes()
ville1.afficher_nbre_batiments()
Ville2.afficher_nbre_batiments()
bat2.afficher_nbre_employes()
bat1.afficher_nbre_employes()

