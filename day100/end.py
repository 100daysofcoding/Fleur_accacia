import tkinter as tk

fenetre = tk.Tk()
fenetre.config(border=10,background="#A2DBDF")
fenetre.title= ("Message de fin")

texte = """ Bonsoir cher tous """
    

widget_texte = tk.Text(fenetre)
widget_texte.insert(tk.END, texte)
widget_texte.pack()

fenetre.mainloop()
