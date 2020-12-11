#coding:utf8
def add(a,b):
    c = a + b
    return c

def sous(a,b):
    c = a - b
    return c

def mult(a,b):
    c = a * b
    return c

def div(a,b):
    c = a / b
    return c

nbre1=int (input ("1er nombre : "))
nbre2=int (input ("2ieme nombre : "))

#print ("addition de %d et %d : %d" % (nbre1, nbre2, add (nbre1, nbre2)))
#print ("soustraction de %d et %d : %d" % (nbre1, nbre2, sous (nbre1, nbre2)))
#print ("multiplication de %d et %d : %d" % (nbre1, nbre2, mult (nbre1, nbre2)))
#print ("division de %d et %d : %d" % (nbre1, nbre2, div (nbre1, nbre2)))
print("addition {}".format(add(nbre1, nbre2)))
print("soustraction {}".format(sous(nbre1, nbre2)))
print("multiplication {}".format(mult(nbre1, nbre2)))
print("division {}".format(div(nbre1, nbre2)))
