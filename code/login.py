from tkinter import Button, Entry, Image, Label, StringVar, Tk, Toplevel, messagebox
from PIL import Image,ImageTk

class page_acceuil:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1000x700+150+0")
        self.root.title("Acceuil")
        self.root.configure(bg='lightgreen')
        self.root.wm_attributes('-fullscreen', 'True')

        bouton_valider = Button(self.root,text="Deconnecter", command=self.root.destroy, font=("Arial", 18, "bold"), fg="white", bg="red")
        bouton_valider.place(x=600, y=330, width=260)

class page_authentification:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1024x768+300+5")
        self.root.title("Login")
        self.root.resizable(False, False)


        #--------parametre image bg

        bg = Image.open(r"images/background_login.png")

        self.photo_bg = ImageTk.PhotoImage(bg)
        lbl = Label(self.root, image=self.photo_bg ,bg ='#290951')
        lbl.place(x=0,y=0,width=1024,height=770)

        #------- champs formulaire
        self.var_login = StringVar()
        self.var_password = StringVar()

        self.champ_username = Entry(self.root, textvariable=self.var_login ,relief="flat", font=("Arial", 12)) #flat, groove, raised, ridge, solid, or sunken
        self.champ_username.place(x=370, y=431)   
        self.champ_password = Entry(self.root, textvariable=self.var_password, relief="flat", font=("Arial", 12)) #flat, groove, raised, ridge, solid, or sunken
        self.champ_password.place(x=370, y=508)      

        #=================== Bouton login  =========================
        btn_login_admin = Image.open(r"boutons/btn_login.png")
        self.photo_btn_login_admin = ImageTk.PhotoImage(btn_login_admin)

        bouton_valider = Button(lbl,command=self.vers_accueil, bg="white",bd=0,image=self.photo_btn_login_admin,cursor="hand2",activebackground="white")
        bouton_valider.place(x=364,y=576,width=302,height=47)


    def vers_accueil(self):
        login = self.var_login.get()
        # controle de saise
        if self.var_login.get() == "":
            messagebox.showerror('Erreur', "Champ login obligatoire")
        elif self.var_password.get() == "":
            messagebox.showerror('Erreur', "Champ mot de passe obligatoire")
        elif  messagebox.showinfo("Authentification réussi","Bienvenue sur votre espace de travail !!") == 'ok' :
            #--on efface les formulaire
            self.var_login.set("")
            self.var_password.set("")

            self.new_window = Toplevel(self.root)
            self.window = page_acceuil(self.new_window)



        
if __name__ == "__main__":
    window_tk = Tk()
    fenetre_to_run = page_authentification(window_tk)
    window_tk.mainloop()