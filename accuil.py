from cgitb import text
from glob import glob
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showinfo
# from listedesinscrits import listeInscrit

# la classe personnage qui va nous permettre de creer une personne à partir de son nom prenom et photo
class Personnage():
    def __init__(self,prenom,nom,photo):
        self.prenom = prenom
        self.nom = nom
        self.photo = photo
        
    # comparaison entre la personne lui même et une autre
    def __eq__(self, other):
        return(self.prenom == other.prenom and self.nom == other.nom)
        
        # la fonction pour selectionner l'image de l'utilisateur
def parcourir():
    global imageName
    imn = askopenfilename(initialdir="/", title="Selectionner une image", 
            filetypes=(( "png files","*.png"),( "jpeg files","*.jpeg")))
    
    # verifier si l'image existe
    
    if imn:
        imageName = imn
    if imageName:
        texte = imageName.split("/")
        photoEntre.configure(text=".../"+texte[-1])    

# verifier si un utilisateur a ete ajouter 
def appartient(liste,val):
    for i in range(len(liste)):
        if liste[i].__eq__(val):
            return 1
    return 0

# la fontion valider
def valider():
    global listePersonne, imageName
    # inisialiser
    imageName = ''
    listePersonne = []
    photo = imageName
    # verifier si les champs ont ete bien renseigner
    if prenomEntre.get() and nomEntre.get() and photo:
        pers = Personnage(prenomEntre.get(),nomEntre.get(),photo)
        
        # on verifie si la personne appartient a la liste
        if appartient(listePersonne,pers):
            showerror(title="Formulaire invalide", message="Desoler la personne existe deja!!")
        else:
            listePersonne.append(pers)
            showinfo(title="Validation reussie", message="{} a bien ete ajouter".format(prenomEntre.get()))   
    else:
        showerror(title="Formulaire invalide", message="Touts les champs doivent être renseigner!!")
        
        # la fonction reinisialiser
def reinisialiser():
    global imageName
    prenomEntre.delete(0, END)
    nomEntre.delete(0,END)
    imageName = ""
    photoEntre.configure(text="Aucune image n'est selectionner!!!")
    
                
             
fen = Tk()
# taille et titre de la fenêtre
fen.geometry("320x320+300+150")
fen.title("Page d'Inscription")

# couleur, taille, texte...
contenu = Canvas(fen,bg="#ff7800")

fontLabel = "Arial 13 bold"
fontEntre = "Arial 11 bold"

# formulaire
prenom = Label(contenu, text="Votre Prenom:", font = fontLabel, fg="white", bg="#ff7800") 
nom = Label(contenu, text="Votre Nom:", font = fontLabel, fg="white", bg="#ff7800")
photo = Label(contenu, text="Votre Photo:", font = fontLabel, fg="white", bg="#ff7800")
validation = Label(contenu, text="Entrez vos informations ici:", font = fontLabel, fg="#ff7800", bg="white")

# imput
prenomEntre = Entry(contenu, font=fontEntre) 
nomEntre = Entry(contenu, font=fontEntre)

# boutton pour selectionner une image
photoEntre = Label(contenu, text="Aucune image selectionner", font = "Arial 7 bold", fg="white", bg="#ff7800")
buttonPacourir = Button(contenu, text="Pr", command=parcourir, fg="#ff7800", bg="white")

# classer chaque partir
#grid sépare ligne et colonne, columnspan c'est la fusion entre deux colonnes, sticky permet d'orienter vers une direction(E->l'EST)
validation.grid(row=0, column=0, columnspan=2)
prenom.grid(row=1, column=0, sticky=E, padx=5, pady=5)
nom.grid(row=2, column=0, sticky=E, padx=5, pady=5)
photo.grid(row=3, column=0, sticky=E, padx=5, pady=5)

#placer les entrer W->l'OUEST
prenomEntre.grid(row=1, column=1, padx=5, pady=5)
nomEntre.grid(row=2, column=1, padx=5, pady=5)
photoEntre.grid(row=3, column=1, padx=5, pady=5, sticky=W)
buttonPacourir.grid(row=3, column=1, padx=5, pady=5, sticky=E)

#  déclarrer les boutons et positionner les 
b1 = Button(fen, text="Valider", command=valider, width=10, fg="white", bg="#ff7800")
b2 = Button(fen, text="Reinisialiser", command=reinisialiser, width=10, fg="white", bg="#ff7800")
b3 = Button(fen, text="Voir la liste", command="", width=10, fg="white", bg="#ff7800")

b1.grid(row=4, column=0, pady=5)
b2.grid(row=5, column=0, pady=5)
b3.grid(row=6, column=0, pady=5)

# positionner le formulaire

contenu.grid(row=0, column=0, padx=5, pady=5)

# afficher la fenêtre

fen.mainloop()