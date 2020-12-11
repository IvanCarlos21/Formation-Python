#coding:utf8
import sqlite3


connection= sqlite3.connect("GestionFormation.db")
cursor = connection.cursor()


def ajouter():
    
    ### ajouter Matiere ###
    def ajouter_matiere( new_nomMatiere):
        try:
            connection= sqlite3.connect("GestionFormation.db")
            cursor = connection.cursor()
            print("je suis connecté à la base donée et je peux ajouter une matiere")
            
            cursor.execute('INSERT INTO Matiere VALUES(?,?)', (cursor.lastrowid, new_nomMatiere))
            connection.commit()
            print("insertion validée")
            cursor.close()
        except sqlite3.Error as err:
            print("[erreur], impossible d'ajouter une matiere: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")

    ### ajouter Cursus ###
    #new_cursus = (cursor.lastrowid, "devops")
    #cursor.execute('INSERT INTO Cursus VALUES(?,?)', new_cursus)
    def ajouter_cursus( new_nomCursus):
        try:
            connection= sqlite3.connect("GestionFormation.db")
            cursor = connection.cursor()
            print("je suis connecté à la base donée et je peux ajouter un Cursus")
            
            cursor.execute('INSERT INTO Cursus VALUES(?,?)', (cursor.lastrowid, new_nomCursus))
            connection.commit()
            print("insertion validée")
            cursor.close()
        except sqlite3.Error as err:
            print("[erreur], impossible d'ajouter un Cursus: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")
    
    ### ajouter Etudiant ###
    #new_etudiant = (cursor.lastrowid, "TANKEU", "Ivan", 20, 1)
    #cursor.execute('INSERT INTO Etudiant VALUES(?,?,?,?,?)', new_etudiant)
    def ajouter_etudiant( new_nomEtudiant, new_prenomEtudiant, new_age):
        try:
            connection= sqlite3.connect("GestionFormation.db")
            cursor = connection.cursor()
            print("je suis connecté à la base donée et je peux ajouter un Etudiant: ")
            id = int(input("quel est l'id du cursus que suit l'eleve "))

            cursor.execute('INSERT INTO Etudiant VALUES(?,?,?,?,?)', (cursor.lastrowid, new_nomEtudiant, new_prenomEtudiant, new_age, id))
            connection.commit()
            print("insertion validée")
            cursor.close()
        except sqlite3.Error as err:
            print("[erreur], impossible d'ajouter un Etudiant: ", err)
        finally:
            connection.close()
            print("The SQLite connection is closed")
    
    #ajouter_matiere('php')
    #ajouter_cursus('Reseau')
    #ajouter_etudiant('Raynolds', 'Adam', 30)
ajouter()

def lister():

    ######### lister matieres
    def lister_matiere():
        try:
            pass
        except sqlite3.Error as err:
            print("[ERREUR] DANS LA LISTE DES MATIERES", err)
        finally:
            pass
    
    lister_matiere()

lister()
import sqlite3

def getDeveloperInfo(id):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from SqliteDb_developers where id = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
            print("Name = ", row[1])
            print("Email  = ", row[2])
            print("JoiningDate  = ", row[3])
            print("Salary  = ", row[4])
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

getDeveloperInfo(2)