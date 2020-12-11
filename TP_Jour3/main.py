#coding:utf8
import sqlite3

connection= sqlite3.connect("GestionFormation.db")
cursor = connection.cursor()

### ajouter Matiere ###
new_matiere = (cursor.lastrowid, "java")
cursor.execute('INSERT INTO Matiere VALUES(?,?)', new_matiere)

### ajouter Cursus ###
new_cursus = (cursor.lastrowid, "devops")
cursor.execute('INSERT INTO Cursus VALUES(?,?)', new_cursus)

### ajouter etudiant ###
new_etudiant = (cursor.lastrowid, "TANKEU", "Ivan", 20, 1)
cursor.execute('INSERT INTO Etudiant VALUES(?,?,?,?,?)', new_etudiant)

#connection.commit()

### lister les matieres ###
req = cursor.execute('SELECT * fROM Matiere')
res = req.fetchall()
print("------------------")
print("liste des matieres")
for row in res:
    print(row)

### lister les Cursus ###
req = cursor.execute('SELECT * fROM Cursus')
res = req.fetchall()
print("------------------")
print("liste des cursus")
for row in res:
    print(row)

### lister les etudiants ###
req = cursor.execute('SELECT * fROM Etudiant')
res = req.fetchall()
print("------------------")
print("liste des etudiants")
for row in res:
    print(row)

### modifier matieres ###
req = cursor.execute('UPDATE Matiere set nomMatiere = "C++" where idMatiere = 2')
#connection.commit()
print("modification des matieres reussies ")

### modifier cursus ###
req = cursor.execute('UPDATE Cursus set nomCursus = "Dev Web" where idCursus = 2')
#connection.commit()
print("modification des matieres reussies ")

### modifier etudiant ###
req = cursor.execute("""UPDATE Etudiant set nomEtudiant = "CARLOS", prenomEtudiant = "arnold", age = 28 where idEtudiant = 2""")
#connection.commit()
print("modification des etudiant reussies ")


### suppression Etudiant ###
req = cursor.execute('DELETE FROM Etudiant where idEtudiant = 4 ')

### suppression Matieres ###
req = cursor.execute('DELETE FROM Matiere where idMatiere = 4 ')

### suppression Cursus ###
req = cursor.execute('DELETE FROM Cursus where idCursus = 4 ')

connection.commit()

cursor.close()
connection.close()