#coding:utf8
def aire(L,l):
    a = l*L
    return a

def perimetre(L,l):
    p = (2*L) + 2*l
    return p

L=  int(input("entrer la longueur"))
l = int (input("entrer la largeur"))

print ("perimetre de %d et %d : %d" % (l, L, perimetre (L, l)))
print ("surface de %d et %d : %d" % (l, L, aire (L, l)))
