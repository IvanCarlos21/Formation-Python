#Mère
class Forme:
	#constructeur
	def __init__(self, origine):
		self.origine = origine
	#methodes
	def calculerDistance(self):
		print("la distance ")
	def calculerPerimetre(self):
		print("perimetre")
	def afficher(self):
		print("printf")

#Classe Fille
class Rectangle(Forme):
	#constructeur
	def __init__(self,origine, longueur, largeur):
		Forme.__init__(self, origine)
		self.longueur = longueur 
		self.largeur = largeur 
	#Methodes

	def calculerPerimetre(self):
		print("perimetre")

	def afficher(self):
		print("printf")


