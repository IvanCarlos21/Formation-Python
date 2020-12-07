#coding:utf8
devise = str(input("choissir entre '$' et'€'pour votre devise "))
if (devise == '$'):
    monnaie = float(input("entrez votre monnaie"))
    monnaie = monnaie * 1.21
    print("votre monnaie convertir donne {} en euros".format(monnaie))
elif (devise == '€'):
    monnaie = float(input("entrez votre monnaie"))
    monnaie = monnaie * 0.83
    print("votre monnaie convertir donne {} en dollar".format(monnaie))
else:
    print("qu'est ce que tu n'a pas compris? sale chien")
