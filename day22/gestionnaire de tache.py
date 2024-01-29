from tkinter import *
from tkinter import messagebox

def ajouter_tache():
    tache = entree_tache.get()
    if tache:
        liste_taches.insert(END, tache)
        entree_tache.delete(0, END)
    else:
        messagebox.showwarning("Attention", "Veuillez entrer une tâche.")

def supprimer_tache():
    try:
        index = liste_taches.curselection()[0]
        liste_taches.delete(index)
    except IndexError:
        messagebox.showwarning("Attention", "Veuillez sélectionner une tâche.")

def enregistrer_taches():
    with open("taches.txt", "w") as fichier:
        for i in range(liste_taches.size()):
            fichier.write(liste_taches.get(i) + "\n")
    messagebox.showinfo("Succès", "Tâches enregistrées avec succès dans le fichier 'taches.txt'.")

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Générateur de tâches")
fenetre['bg']='#CCEDFF'
fenetre.iconbitmap("day22/logo.ico")
 
# Frame pour l'entrée de la tâche
frame_user = Frame(fenetre)
frame_user.pack(pady=10)

label_user = Label(frame_user, text="Nouvelle tâche :")
label_user.grid(row=0, column=0)

entree_tache = Entry(frame_user, width=30)
entree_tache.grid(row=0, column=1)

bouton_ajouter = Button(frame_user, text="Ajouter", command=ajouter_tache,bg='#CCEDFF')
bouton_ajouter.grid(row=0, column=2, padx=10)

# Frame pour la liste des tâches
frame_liste = Frame(fenetre)
frame_liste.pack(padx=10, pady=5)

label_liste = Label(frame_liste, text="Liste des tâches :")
label_liste.pack()

scrollbar = Scrollbar(frame_liste, orient=VERTICAL)
liste_taches =Listbox(frame_liste, height=10, width=50, yscrollcommand=scrollbar.set)
scrollbar.config(command=liste_taches.yview)
scrollbar.pack(side=RIGHT, fill=Y)
liste_taches.pack(side=LEFT, fill=BOTH, expand=1)



# Frame pour les boutons
frame_boutons = Frame(fenetre)
frame_boutons.pack(side=BOTTOM, pady=10)

bouton_supprimer = Button(frame_boutons, text="Supprimer", command=supprimer_tache, bg='#CCEDFF')
bouton_supprimer.grid(row=0, column=0, padx=5)

bouton_enregistrer = Button(frame_boutons, text="Enregistrer", command=enregistrer_taches,bg='#CCEDFF')
bouton_enregistrer.grid(row=0, column=1, padx=5)

# Chargement des tâches depuis un fichier
try:
    with open("taches.txt", "r") as fichier:
        for ligne in fichier:
            liste_taches.insert(END, ligne.strip())
except FileNotFoundError:
    pass

fenetre.mainloop()
