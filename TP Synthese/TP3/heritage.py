#codind:utf8

class Alphabet:
    def __init__(self, nom):
        self.lettre_nom = nom
    def info(self):
        print("je suis une lettre de l'aphabet")
    def test1(self):
        print("Fonction test1() de la classe alphabet")
    def test2(self):
        print("Fonction test2() de la classe alphabet")

class Mot:
    def info(self):
        print("je suis un mot")
    def test1(self):
        print("Fonction test1() de la classe Mot")
    def test3(self):
        print("Fonction test3() de la classe Mot")

class Accent:
    def info(self):
        print("je suis un accent")
    def test2(self):
        print("Fonction test2() de la classe Accent")
    def test3(self):
        print("Fonction test3() de la classe Accent")

class A(Alphabet):
    def info(self):
        print("je suis la lettre A")
    def test1(self):
        print("Fonction test1() de la classe A")

class Abracadabra(Mot):
    def test1(self):
        print("Fonction test1() de la classe Abracadabra")

class AGrave(A, Accent, Abracadabra):
    def test4(self):
        print("Fonction test4() de la classe AGravve")


#################################### main()
aAccentGrave = AGrave("à")
aAccentGrave.lettre_nom
aAccentGrave.info()
aAccentGrave.test1()
aAccentGrave.test2()
aAccentGrave.test3()
aAccentGrave.test4()


############################# conclusion #########################""

#l’héritage va se faire selon l’ordre des classes mères indiquées et cela de manière récursive
# le programme va d'abord commencer par chercher la méthode dans AGrave, 
# puis si il ne la trouve pas cherchera dans A. 
# S’il ne la trouve pas il cherchera ensuite dans Alphabet, 
# puis dans Accent, puis dans Abracadabra et finalement dans Mot.
