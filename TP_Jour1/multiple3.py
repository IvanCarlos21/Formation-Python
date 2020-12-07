#coding:utf8
nombre = int(input("entrez un nombre"))
if(nombre % 2 == 0):
    print("ce nombre est pair")
else:
    if(nombre%3 == 0):
        print("ce nombre est impair mais multiple de 3")
    else:
        print("ce nombre n'est ni pair ni multiple de 3")