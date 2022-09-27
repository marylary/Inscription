import imghdr
import imp
from tkinter import *
from PIL import Image, ImageTk

import service as serv

def listeInscrit(fenetre):
    newFen = Toplevel(fenetre)
    newFen.geometry("350x400+350+150")
    newFen.title("Liste des Inscrits")
    
    cont = Canvas(newFen, bg="#ff7800")
    fontLabel = "Arial 11 bold"
        # label
    resultat = Label(cont, text="Liste des gens inscrits", font = fontLabel, fg="#ff7800", bg="white")
    photo = Label(cont, text="Photo", width="15", font = fontLabel,  fg="white", bg="#ff7800")
    prenom = Label(cont, text="Prenom", width="6", font = fontLabel, fg="white", bg="#ff7800")
    nom = Label(cont, text="Nom", width="12", font = fontLabel, fg="white", bg="#ff7800")
    status = Label(newFen, text="Aucun inscrit pour le moment", font ="Arial 9 bold", fg="white", bg="#ff7800")

        # classement
    cont.grid(row=0,column=0)
    resultat.grid(row=0,column=0,columnspan=3)
    photo.grid(row=1,column=0,padx=5,pady=5)
    prenom.grid(row=1,column=1,padx=5,pady=5)
    nom.grid(row=1,column=2,padx=5,pady=5)
    status.grid(row=2,column=0,columnspan=3, pady=3)
    
    liste= serv.afficher()
    # reccuperer les donnees dans la liste "ANTIALIAS" cree un aspert plus liste sur une image
    if liste:
        r=2
        for p in liste:
            # au niveau de p on donne l'indice de chaque colonne situer dans la base de donnée
            photoLab = Label(cont, bg="white", height=50)
            img = Image.open(p[3])
            img = img.resize((80,80),Image.ANTIALIAS)
            photoLab.img = ImageTk.PhotoImage(img)
            photoLab.configure(image=photoLab.img)
            
            pren = Label(cont, text=p[1], font = fontLabel, fg="white", bg="#ff7800")
            no = Label(cont, text=p[2], font = fontLabel, fg="white", bg="#ff7800")
            
            # positionnement
            photoLab.grid(row=r, column=0, pady=2)
            pren.grid(row=r, column=1)
            no.grid(row=r, column=2)
            
            # definir la ligne qui sépare les labels des donnees
            cont.create_line(9,55,355,55, width=1, fill='white')
            r+=1
            
            # le nombre de personne dans la liste
            status.configure(text="{} Inscrit pour le moment".format(len(liste)))
            status.grid(row=r,column=0,columnspan=3,pady=2)
            
    newFen.mainloop()
            