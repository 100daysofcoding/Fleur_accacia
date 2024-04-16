import tkinter as tk
from PIL import Image, ImageTk

def afficher_gif():
    img = Image.open("day100/voir.jpg")
    img = ImageTk.PhotoImage(img)
    label.configure(image=img)
    label.image = img


fenetre = tk.Tk()
fenetre.title= ("Message de fin")

texte = """ Ladies and gentleman ......"""

bouton = tk.Button(fenetre, text="Appuyer pour voir le rendu", command=afficher_gif)
bouton.pack(pady=10)


label = tk.Label(fenetre)
label.pack()

widget_texte = tk.Text(fenetre)
widget_texte.insert(tk.END, texte)
widget_texte.pack()
 
fenetre.mainloop()
