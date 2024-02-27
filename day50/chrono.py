import time
from tkinter import *
from tkinter import messagebox



fenetre = Tk()
fenetre.title("Chronomètre")
fenetre['bg'] = '#CCEDFF'
fenetre.geometry("300x250")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(fenetre, width=3, font=("Arial", 18, ""), textvariable=hour)
hourEntry.place(x=80, y=20)

minuteEntry = Entry(fenetre, width=3, font=("Arial", 18, ""), textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(fenetre, width=3, font=("Arial", 18, ""), textvariable=second)
secondEntry.place(x=180, y=20)

paused = False  # État de pause initial

def pause():
    global paused
    paused = not paused

def submit():
    try:
        # Vérifie si les champs sont vides
        if hour.get() == "" or minute.get() == "" or second.get() == "":
            raise ValueError("Veuillez entrer des nombres dans tous les champs")
        
        # Convertit les valeurs entrées en secondes
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))
    else:
        while temp > -1:
            if paused:
                # Si en pause, attendre 1 seconde sans décrémenter le temps
                time.sleep(1)
            else:
                # Sinon, continuer à décrémenter le temps et mettre à jour l'interface utilisateur
                mins, secs = divmod(temp, 60)
                hours = 0
                if mins > 60:
                    hours, mins = divmod(mins, 60)
                hour.set("{0:02d}".format(hours))
                minute.set("{0:02d}".format(mins))
                second.set("{0:02d}".format(secs))
                fenetre.update()
                time.sleep(1)
                if temp == 0:
                    messagebox.showinfo("Compte à rebours terminé", "Le temps est écoulé")
                temp -= 1

begin = PhotoImage(file='day50/jouer.png')
begin_btn = Button(fenetre, image=begin, command=submit, cursor="hand2", bg='#CCEDFF')
begin_btn.place(x=25, y=120)

pause_img = PhotoImage(file='day50/bouton-pause.png')
pause_btn = Button(fenetre, image=pause_img, command=pause, cursor="hand2", bg='#CCEDFF')
pause_btn.place(x=125, y=120)

fenetre.mainloop()
