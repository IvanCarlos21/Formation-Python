#coding:utf8
prenom = str(input("quel est votre prenom?"))
nom = str(input("quel est votre nom?"))
age = int(input("quel est votre age?"))
print("tu t'appele {}, {} et tu a {} ans".format(prenom, nom, age))
#print("tu t'appeles"+ prenom + " " + nom + "et tu as" +age)

#calcul age dans 10 ans
age10 = age + 10
print("tu aura {} dans 10 ans".format(age10))