#Créer un programme qui permet de saisir 2 nombres : Pour chaque nombre saisi on contrôle 
#si il s'agit d'un type entier, 
#pour le 2ieme nombre saisi on contrôle en plus si il est différent de 0. 
#Pour le premier nombre saisi, on contrôle en plus si il est un nombre pair. 
#Si tout est bon on fait la division du premier par le deuxième

#coding:utf8
try:
    y = int(input("entrer un second nombre entier et différent de zero: "))
    x = int(input("entrer un nombre entier et pair: "))
except TypeError:
    print("tu es trop bête, on te dit un nombre")
except(x % 2 != 0):
    print("tu es trop bête, on te dit un nombre pair")


try:
except TypeError:
    print("tu es trop bête, on te dit un nombre")
except ZeroDivisionError:
    print("tu es trop bête, on te dit un nombre non nul")

print("la division de %d par %d est egal à : %d", x, y, x/y)