import mysql.connector

# connecter à la base de donné
def connexion():
    try:
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admine",
        database="application"
    )
        print("Connection Etablie!!!")
        return db
    
    except:
        print("Connection non Etablie!!!")
        
 # ajouter un element à la base de donnée
def ajouter(personne):
    # reccuperer le curseur de notre base de donnee
    db = connexion()
    cursor = db.cursor()
    valeurs = (personne.prenom, personne.nom, personne.photo)
    cursor.execute(""" INSERT INTO personne (prenom, nom, photo) VALUES(%s, %s, %s) """,valeurs)
    
    db.commit()
    
    # affichage
def afficher():
    db = connexion()
    cursor = db.cursor()
    cursor.execute(""" SELECT * FROM personne """)
    # reccuperer toutes les lignes de personnes ajouter dans la base de donnée
    rows = cursor.fetchall()
    return rows

    db.commit()
