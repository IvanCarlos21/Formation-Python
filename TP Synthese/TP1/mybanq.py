#coding:utf8
import sqlite3

#connection= sqlite3.connect("Banque.db")
#cursor = connection.cursor()

########################################## CRUD ########################################

############### Create

def ajouter():

    def creer_compte(solde , decouvert):
        try:
            connection= sqlite3.connect("Banque.db")
            cursor = connection.cursor()
           
            cursor.execute('INSERT INTO CompteBancaire VALUES(?,?,?)', (cursor.lastrowid, solde, decouvert))
            connection.commit()
            print("insertion validée")
            cursor.close()
        except sqlite3.Error as err:
            print("[erreur], impossible de creer un compte Bancaire: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")

    def creer_agence(nom , id_bank):
        try:
            connection= sqlite3.connect("Banque.db")
            cursor = connection.cursor()
           
            cursor.execute('INSERT INTO Agence VALUES(?,?,?)', (cursor.lastrowid, nom, id_bank))
            connection.commit()
            print("insertion validée")
            cursor.close()
        except sqlite3.Error as err:
            print("[erreur], impossible de creer une Agence Bancaire: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")

    def inscription_client(civilite, nom, prenom, adresse, id_bank):
        try:
            connection= sqlite3.connect("Banque.db")
            cursor = connection.cursor()
           
            cursor.execute('INSERT INTO Client VALUES(?,?,?,?,?,?)', (cursor.lastrowid, civilite, nom, prenom, adresse, id_bank))
            connection.commit()
            print("insertion validée")
            cursor.close()
        except sqlite3.Error as err:
            print("[erreur], impossible de creer un nouveau client: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")

    def ajouter_argent(id_cl, argent):
        try:
            connection= sqlite3.connect("Banque.db")
            cursor = connection.cursor()

           ### req = """ INSERT INTO CompteBancaire(solde)
            ###        SELECT cb.solde FROM CompteBancaire AS cb INNER JOIN Client AS cl ON cb.idCompte == cl.idCompte
            ###        SET solde=?, (argent, )"""

            
            #res = cursor.execute(req)


            #cursor.execute('INSERT INTO Client VALUES(?,?,?,?,?,?)', (cursor.lastrowid, civilite, nom, prenom, adresse, id_bank))
            #cursor.execute('UPDATE Client set adresse = ? where idClient = ?', (adress, id_cl))
            connection.commit()
            print("insertion validée")
            cursor.close()
        except sqlite3.Error as err:
            print("[erreur], impossible de mettre l'argent dans son comptet: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")


    creer_compte(1000, 300)
    creer_agence('LclParis', 1)
    inscription_client("mr", "tankeu", "ivan", "14 avenue du jour", 2 )
    ajouter_argent(1, 550)
ajouter()

############### Read

def lister():

    def lire_info_client():
        try:
            connection= sqlite3.connect("Banque.db")
            cursor = connection.cursor()

            sql_select_query = 'select * from Client'
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            print("Printing ID ")
            for row in records:
                print("Civilité = ", row[1])
                print("nom  = ", row[2])
                print("Prenom  = ", row[3])
                print("Adresse  = ", row[4])
                print("et son  compte bancaire est le compte n°", row[5])
            cursor.close()

        except sqlite3.Error as err:
            print("[erreur], impossible de lire les infos sur ce client: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")


    def lire_info_compte():
        try:
            connection= sqlite3.connect("Banque.db")
            cursor = connection.cursor()

            sql_select_query = 'select * from CompteBancaire'
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            print("Printing ID ")
            for row in records:
                print("le compte n° = ", row[0])
                print(" a un solde  = ", row[1])
                print("et un decouvert de  = ", row[2])
            cursor.close()

        except sqlite3.Error as err:
            print("[erreur], impossible de lire les infos sur ce client: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")

    def lire_info_agence():
        try:
            connection= sqlite3.connect("Banque.db")
            cursor = connection.cursor()

            sql_select_query = 'select * from Agence '
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            print("Printing ID ")
            for row in records:
                print("l'agence' n° = ", row[0])
                print("s'appele  = ", row[1])
                print("et le compte n°  = ", row[2], " y est associe")
            cursor.close()

        except sqlite3.Error as err:
            print("[erreur], impossible de lire les infos sur ce client: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")

    lire_info_client()
    lire_info_compte()
    lire_info_agence()
lister()

############### Update

def modifier():
    def modifier_client(adress, id_cl):
        try:
            connection= sqlite3.connect("Banque.db")
            cursor = connection.cursor()
            print("Connected to SQLite")

            cursor.execute('UPDATE Client set adresse = ? where idClient = ?', (adress, id_cl))
            connection.commit()
            print("Record Updated successfully ")
            cursor.close()

        except sqlite3.Error as err:
            print("[erreur], impossible de modifier le client: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")

    def modifier_solde(sold, id_c):
        try:
            connection= sqlite3.connect("Banque.db")
            cursor = connection.cursor()
            print("Connected to SQLite")

            cursor.execute('UPDATE CompteBancaire set solde = ? where idCompte = ?', (sold, id_c))
            connection.commit()
            print("Record Updated successfully ")
            cursor.close()

        except sqlite3.Error as err:
            print("[erreur], impossible de modifier le client: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")

    def modifier_agence(nom, id_a):
        try:
            connection= sqlite3.connect("Banque.db")
            cursor = connection.cursor()
            print("Connected to SQLite")

            cursor.execute('UPDATE Agence set nomAgence = ? where idAgence = ?', (nom, id_a))
            connection.commit()
            print("Record Updated successfully ")
            cursor.close()

        except sqlite3.Error as err:
            print("[erreur], impossible de modifier le client: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")

    modifier_client("09 rue de la mare de troux, Guyancourt", 1)
    modifier_solde(2000, 1)
    modifier_agence("BNP Paris", 1)

modifier()
############### Delete
def supprimer():

    def supprimer_client(id_cl):
        try:
            connection= sqlite3.connect("Banque.db")
            cursor = connection.cursor()
            print("Connected to SQLite")

            cursor.execute('DELETE FROM Client where idClient = ?', (id_cl, ))
            connection.commit()
            print("Record deleted successfully ")
            cursor.close()
        except sqlite3.Error as err:
            print("[erreur], impossible de supprimer ce client: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")

    def supprimer_agence(id_a):
        try:
            connection= sqlite3.connect("Banque.db")
            cursor = connection.cursor()
            print("Connected to SQLite")

            cursor.execute('DELETE FROM Agence where idAgence = ?', (id_a, ))
            connection.commit()
            print("Record deleted successfully ")
            cursor.close()
        except sqlite3.Error as err:
            print("[erreur], impossible de supprimer cette agence: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")

    def supprimer_compte(id_c):
        try:
            connection= sqlite3.connect("Banque.db")
            cursor = connection.cursor()
            print("Connected to SQLite")

            cursor.execute('DELETE FROM Compte where idCompte = ?', (id_c, ))
            connection.commit()
            print("Record deleted successfully ")
            cursor.close()
        except sqlite3.Error as err:
            print("[erreur], impossible de supprimer ce compte: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")





    supprimer_client(7)
    supprimer_agence(7)
    supprimer_compte(7)


supprimer()

