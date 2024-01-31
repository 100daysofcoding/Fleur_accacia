from tkinter import *
from tkinter import messagebox

fenetre =Tk()
fenetre.title("Page de connexion")
fenetre['bg']='#CCEDFF'
fenetre.geometry("400x400")
fenetre.resizable(height='False',width='False')



def visibilité():
    global password_visible
    password_visible = not password_visible
    if password_visible:
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

def forgot_password():
    messagebox.showinfo("Forgot Password", "Please enter your email to reset your password.")
    
def login():
    username = entree_username.get()
    password = entry_password.get()

    # Vérification des informations de connexion
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")    


image=PhotoImage(file='day23/image.png')
label_photo=Label(fenetre,image=image,bg='#CCEDFF')
label_photo.place(x='170',y='20')


#creation de la frame
frame_user = Frame(fenetre,bg='#CCEDFF')
frame_user.pack(pady=125)

#creation boite d'acces username
entree_username = Entry(frame_user, width=30, border=2)
entree_username.grid(row=0, column=1)
entree_username.insert(0,"Username")


user = PhotoImage(file='day23/user.png')
label_user = Label(frame_user, image=user, bg='#CCEDFF')
label_user.grid(row=0, column=0) 



password_visible = False 
#creation boite d'acces password
entry_password = Entry(frame_user, width=30,border=2, show="*")
entry_password.grid(row=1, column=1 ,pady=15)
entry_password.insert(0,"Password")


code = PhotoImage(file='day23/padlock.png')
label_code = Label(frame_user, image=code, bg='#CCEDFF')
label_code.grid(row=1, column=0, padx=5)



vue = PhotoImage(file='day23/eye.png')
label_vue = Label(frame_user, image=vue, bg='#CCEDFF',cursor="hand2")
label_vue.grid(row=1, column=1,padx=(0, 2), sticky=E)
label_vue.bind("<Button-1>", lambda event: visibilité())



#Forgot password
label_password = Label(frame_user, text="Forgot password ?",fg='black',bg='#CCEDFF',cursor="hand2")
label_password.place(x=85,y=70)
label_password.bind("<Button-1>", lambda event: forgot_password())



#connexion
bouton_connexion = Button(frame_user, text="LOGIN", font=("Arial",15,"bold"),bg='#CCEDFF',border=2,command=login)
bouton_connexion.grid(row=2, columnspan=2, pady=20)





fenetre.mainloop()

