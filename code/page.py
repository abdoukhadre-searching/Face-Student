from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkcalendar import DateEntry
import cv2
import dbconfig as connection
import os
import numpy as np



class pagePrincipal:
    def __init__(self,root):
        self.root = root
        self.root.title("FACE STUDENT 2022")
        self.root.geometry("1295x728+120+25")

        self.tabControl = ttk.Notebook(root)

        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)
        self.tab5 = ttk.Frame(self.tabControl)


        self.tabControl.add(self.tab1, text ='Authentification')
        self.tabControl.add(self.tab2, text ='Gestion enseignant')
        self.tabControl.add(self.tab3, text ="Gestion etudiant + traitements d'image")
        self.tabControl.add(self.tab4, text ="Gestion des comptes d'utilisateur")
        self.tabControl.add(self.tab5, text ="Gestion liste de présences")

        self.tabControl.pack(expand = 1, fill ="both")
        #-----------------------------------------------------
        # tab1_secondaire1 = ttk.Frame(self.tab1)
        # tab1_secondaire2 = ttk.Frame(self.tab1)
        # tabControl_tab1 = ttk.Notebook(self.tab1)
        #-----desactive tous les panels-----------------------
        self.tabControl.tab(0, state="normal")
        self.tabControl.tab(1, state="normal")
        self.tabControl.tab(2, state="normal")
        self.tabControl.tab(3, state="normal")
        self.tabControl.tab(4, state="normal")

        titre_page = Label(self.tab3, text="Page de gestion des informations des Etudiants",font=("time new roman",16, "bold"),fg="black")
        titre_page.place(x=400, y=20)
        s_titre_page = Label(self.tab3, text="Système de Gestion des Présences des TD et TP - Copyright @2022 ",font=("time new roman",10),fg="black")
        s_titre_page.place(x=400, y=50)

        # tabControl_tab1.add(self.tab1_secondaire1, text="Connexion enseignant")
        # tabControl_tab1.add(self.tab1_secondaire2, text="Connexion admin")
        # tabControl_tab1.place(x=0, y=0, height=800, width=1300)

        #--------parametre image bg ---------------------

        bg = Image.open(r"images/background_login.png")

        self.photo_bg = ImageTk.PhotoImage(bg)
        lable_login = Label(self.tab1, image=self.photo_bg ,bg ='#290951')
        lable_login.place(x=0,y=0,width=1024,height=770)

        #------- champs formulaire ---------------------
        self.var_login = StringVar()
        self.var_password = StringVar()
        self.var_id_etudiant = IntVar() #integer in db
        self.var_nom_etudiant = StringVar()
        self.var_niveau_etudiant = StringVar()
        self.var_prenom_etudiant = StringVar()
        self.var_sexe_etudiant = StringVar()
        self.var_date_naissance_etudiant = StringVar()
        self.var_lieu_naissance_etudiant = StringVar()
        self.var_tel_etudiant = StringVar()

        champ_username = Entry(self.tab1, textvariable=self.var_login ,relief="flat", font=("Arial", 12)) #flat, groove, raised, ridge, solid, or sunken
        champ_username.place(x=370, y=431)   
        champ_password = Entry(self.tab1, textvariable=self.var_password, relief="flat", font=("Arial", 12)) #flat, groove, raised, ridge, solid, or sunken
        champ_password.place(x=370, y=508)      

        
        #-------------tab 3
        identifiant_etudiant_lbl = Label(self.tab3, text="Numero d'identification",font=("time new roman",12, "bold"),fg="black")
        identifiant_etudiant_lbl.place(x=20, y=100)
        lbl = Label(self.tab3,textvariable=self.var_id_etudiant,  fg="black",font=("time new roman",12, "bold"))
        lbl.place(x=230,y=100)

        nom_etudiant_lbl = Label(self.tab3, text="Nom etudiant",font=("time new roman",12, "bold"),fg="black")
        nom_etudiant_lbl.place(x=20, y=140)
        # lbl = Label(self.tab3,image=img, bg='#174577')
        # lbl.place(x=160,y=135,height=33,width=220)
        nom_etudiant = Entry(self.tab3, fg="#174577",textvariable=self.var_nom_etudiant,relief=FLAT,font=("time new roman",12, "bold"))
        nom_etudiant.place(x=170,y=140)

        prenom_etudiant_lbl = Label(self.tab3, text="Prenom etudiant",font=("time new roman",12, "bold"),fg="black")
        prenom_etudiant_lbl.place(x=20, y=180)
        # lbl = Label(self.tab3,image=img, bg='#174577')
        # lbl.place(x=160,y=175,height=33,width=220)
        prenom_etudiant = Entry(self.tab3, fg ="#174577",textvariable=self.var_prenom_etudiant,relief=FLAT,font=("time new roman",12, "bold"))
        prenom_etudiant.place(x=170,y=180)

        niveau_etudiant_lbl = Label(self.tab3, text="Niveau",font=("time new roman",12, "bold"),fg="black")
        niveau_etudiant_lbl.place(x=400, y=140)
        # lbl = Label(self.tab3,image=img, bg='#174577')
        # lbl.place(x=480,y=135,height=33,width=220)
        niveau_combo= ttk.Combobox(self.tab3,foreground='#174577',textvariable=self.var_niveau_etudiant ,font=("time new roman",12, "bold"), state="readonly")
        niveau_combo.place(x=490,y=140)
        niveau_combo["values"] = ("Sélectionner le niveau","Licence 1", "Licence 2", "Licence 3", "Master 1", "Master 2")
        niveau_combo.current(0)

        sexe_etudiant_lbl = Label(self.tab3, text="Genre",font=("time new roman",12, "bold"),fg="black")
        sexe_etudiant_lbl.place(x=400, y=180)
        # lbl = Label(self.tab3,image=self.img, bg='#174577')
        # lbl.place(x=480,y=175,height=33,width=220)
        sexe_combo= ttk.Combobox(self.tab3,foreground='#174577',textvariable=self.var_sexe_etudiant ,font=("time new roman",12, "bold"), state="readonly")
        sexe_combo["values"]=("Selectionner le sexe","Homme","Femme")
        sexe_combo.current(0)
        sexe_combo.place(x=490,y=180)

        dateNaissance_etudiant_lbl = Label(self.tab3, text="Date Naissance",font=("time new roman",12, "bold"),fg="black")
        dateNaissance_etudiant_lbl.place(x=20, y=220)
        # lbl = Label(self.tab3,image=img, bg='#174577')
        # lbl.place(x=160,y=215,height=33,width=220)
        date_naissance=DateEntry(self.tab3,selectmode='day',textvariable=self.var_date_naissance_etudiant)
        date_naissance.place(x=170,y=222,width=200)

        lieuNaissance_etudiant_lbl = Label(self.tab3, text="Lieu de naissance",font=("time new roman",12, "bold"),fg="black")
        lieuNaissance_etudiant_lbl.place(x=400, y=220)
        # lbl = Label(self.tab3,image=img, bg='#174577')
        # lbl.place(x=550,y=215,height=33,width=220)
        lieuNaissance_etudiant = Entry(self.tab3, fg ="#174577",textvariable=self.var_lieu_naissance_etudiant,relief=FLAT,font=("time new roman",12, "bold"))
        lieuNaissance_etudiant.place(x=560,y=220)

        contactEtudiant_lbl = Label(self.tab3, text="Numero telephone",font=("time new roman",12, "bold"),fg="black")
        contactEtudiant_lbl.place(x=725, y=140)
        # lbl = Label(self.tab3,image=img, bg='#174577')
        # lbl.place(x=840,y=135,height=33,width=220)
        contactEtudiant_entry = Entry(self.tab3, fg ="#174577",textvariable=self.var_tel_etudiant,relief=FLAT,font=("time new roman",12, "bold"))
        contactEtudiant_entry.place(x=875,y=140)

        #-----boutons
        btn_sv_p = Button(self.tab3,bg="#174577",text="Enregister", foreground="white", command=self.insert_etudiant,bd=0,cursor="hand2",activebackground="#174577")
        btn_sv_p.place(x=50,y=290,width=140,height=33)
        btn_update_p = Button(self.tab3,bg="#174577",text="Modifier", foreground="white", command="",bd=0,cursor="hand2",activebackground="#174577")
        btn_update_p.place(x=200,y=290,width=140,height=33)
        btn_delete_p = Button(self.tab3,bg="#174577", text="Supprimer", foreground="white", command= "",bd=0,cursor="hand2",activebackground="#174577")
        btn_delete_p.place(x=350,y=290,width=140,height=33)
        btn_effacer_p = Button(self.tab3,bg="#174577",text="Annuler", foreground="white", command=self.reset_formulaire,bd=0,cursor="hand2",activebackground="#174577")
        btn_effacer_p.place(x=500,y=290,width=140,height=33)
        btn_photo_visage_etudiant = Button(self.tab3,bg="#174577",text="Prendre photo", foreground="white", command=self.lancer_camera,bd=0,cursor="hand2",activebackground="#174577")
        btn_photo_visage_etudiant.place(x=650,y=290,width=140,height=33)
        btn_code_etudiant = Button(self.tab3,bg="green",text="Actualiser le modèle de reconnaissance", foreground="white", command=self.actualiser_fichier_reconnaissance,bd=0,cursor="hand2",activebackground="lightgreen")
        btn_code_etudiant.place(x=820,y=290,width=230,height=33)
        btn_supprime_image_etudiant = Button(self.tab3,bg="#174577",text="Supprimer photos", foreground="white", command="",bd=0,cursor="hand2",activebackground="#174577")
        btn_supprime_image_etudiant.place(x=1070,y=290,width=110,height=33)

        #============ Bouton login  =========================
        btn_login_admin = Image.open(r"boutons/btn_login.png")
        self.photo_btn_login_admin = ImageTk.PhotoImage(btn_login_admin)
        bouton_valider = Button(lable_login,command=self.vers_tab2, bg="white",bd=0,image=self.photo_btn_login_admin,cursor="hand2",activebackground="white")
        bouton_valider.place(x=364,y=576,width=302,height=47)

        bouton_deconnexion = Button(self.tab2,text="Deconnexion",bd=0, command=self.retour, bg="red",cursor="hand2",activebackground="white")
        bouton_deconnexion.place(x=800,y=20,width=302,height=47)
        #-------- Tableau Liste Etudiant ---------------
        table_frame=Frame(self.tab3, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=355, width=1230, height=370) #w=1226

        scroll_x= ttk.Scrollbar(table_frame, orient= HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame, orient= VERTICAL)


        self.student_table= ttk.Treeview(table_frame, columns=("id","prenom","nom","niveau","sexe","dateNaissance","lieuNaissance","telephoneEtudiant","absence_semestre"),xscrollcommand=scroll_x.set,yscrollcommand= scroll_y.set)
        s = ttk.Style()
        s.configure('Treeview', rowheight= 40)
        s.configure("Treeview.Heading", font=("time new roman", 10, "bold"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id",text="Numero Etudiant")
        self.student_table.heading("prenom",text="Prenom")
        self.student_table.heading("nom",text="Nom")
        self.student_table.heading("niveau",text="Niveau")
        self.student_table.heading("sexe",text="Sexe")
        self.student_table.heading("dateNaissance",text="Date de Naissance")
        self.student_table.heading("lieuNaissance",text="Lieu de Naissance")
        self.student_table.heading("telephoneEtudiant",text="Telephone")
        self.student_table.heading("absence_semestre",text="Absence semestrielle")        
        #self.student_table.heading("photo",text="Photo Profil")

        #`id_eleve`, `nom`, `adresse`, `dateNaissance`, `niveau`, `niveau`, `sexe`, `domaine`, `annee`, `contactParent`, `enseignant`, `semestre`, `photo`

        self.student_table.column("id",width=100,stretch=0)
        self.student_table.column("prenom",width=100,stretch=0)
        self.student_table.column("nom",width=100,stretch=0)
        self.student_table.column("niveau",width=100,stretch=0)
        self.student_table.column("sexe",width=100,stretch=0)
        self.student_table.column("dateNaissance",width=135,stretch=0)
        self.student_table.column("lieuNaissance",width=135,stretch=0)
        self.student_table.column("telephoneEtudiant",width=120,stretch=0)
        self.student_table.column("absence_semestre",width=140,stretch=0)
        #self.student_table.column("photo",width=100)


        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_datatable)
        self.afficher_infos_table()

    def actualiser_fichier_reconnaissance(self):
        data_dir=("photos_etudiants")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids  =[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Chargement des images enregistres",imageNp)
            cv2.waitKey(1)==13            
        ids=np.array(ids)

        #========== Train the classifier and save the results ===============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("model/model.xml")
        # dire("Actualiser du modeles de reconnaissance faciales")

        cv2.destroyAllWindows()
        messagebox.showinfo("Resultat","Modele actualisé avec succés !", parent=self.tab3)

    def afficher_infos_table(self):
        try:
            conn = connection.database_connection()
            my_curseur = conn.cursor()
            my_curseur.execute("SELECT * FROM `etudiant`")   
            etudiants = my_curseur.fetchall()

            if len(etudiants) != 0:
                self.student_table.delete(*self.student_table.get_children())  
                for etu in etudiants:
                    self.student_table.insert("", END,values=etu)
                    conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showinfo("Erreur",f"Une erreur est survenue: {str(ex.args)}")
            print(f"Erreur lors l'affichage :{str(ex)}")

    #================ Recupérer les données du Tableau ===========
    def get_datatable(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        donnees = content["values"]
        print("Donnee tableau etudiant:\n",donnees)
        self.var_id_etudiant.set(donnees[0]),
        self.var_prenom_etudiant.set(donnees[1]),
        self.var_nom_etudiant.set(donnees[2]),
        self.var_niveau_etudiant.set(donnees[3]),        
        self.var_sexe_etudiant.set(donnees[4]),
        self.var_date_naissance_etudiant.set(donnees[5]),
        self.var_lieu_naissance_etudiant.set(donnees[6]),
        self.var_tel_etudiant.set(donnees[7]),  


    
    def retour(self):
        self.tabControl.select(0)
        self.tabControl.tab(0, state="normal")
        self.tabControl.tab(1, state="hidden")
        self.tabControl.tab(2, state="hidden")
        self.tabControl.tab(3, state="hidden")
        self.tabControl.tab(4, state="hidden")

    def vers_tab2(self):
        # login = var_login.get()
        #     # controle de saise
        # if var_login.get() == "":
        #     messagebox.showerror('Erreur', "Champ login obligatoire")
        # elif var_password.get() == "":
        #     messagebox.showerror('Erreur', "Champ mot de passe obligatoire")
        # elif  messagebox.showinfo("Authentification réussi","Bienvenue sur votre espace de travail !!") == 'ok' :
        #     #--on efface les formulaire
        #     var_login.set("")
        #     var_password.set("")
        self.tabControl.select(1)
        self.tabControl.tab(0, state="hidden")
        self.tabControl.tab(1, state="normal")
        self.tabControl.tab(2, state="normal")
        self.tabControl.tab(3, state="normal")
        self.tabControl.tab(4, state="normal")

    def lancer_camera(self):
        id = self.var_id_etudiant.get()
        if id == 0:
            messagebox.showerror('Erreur', "Veuiller selectionner un Etudiant", parent=self.tab3)
        else:
            face_classifier=cv2.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")

            cap =cv2.VideoCapture(0, cv2.CAP_DSHOW)

            img_id=0
            while True:
                ret,img=cap.read()#recupere video depuis webcam
                gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                visages=face_classifier.detectMultiScale(img, 1.3, 5)#(img, 1.05, 6)
                visages=face_classifier.detectMultiScale(gray, 1.3, 5)
                #-------- Redimensionner l'Image ---------------
                minisize = (img.shape[1],img.shape[0])
                miniframe = cv2.resize(img, minisize)
                visages =  face_classifier.detectMultiScale(miniframe)
                for (x,y,w,h) in visages:
                    img_id+=1
                    #visage_recadre=img[y:y+h, x:x+w]
                    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)                        
                    cv2.putText(img,"Prise d'images faciales...",(x-5,y+h+15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)
                    #Save just the rectangle faces in SubRecFaces
                    img_save = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    sub_face = img_save[y:y+h, x:x+w]                        
                    #face = cv2.resize(img[y:y+h, x:x+w](img),(450,450))
                    #face = cv2.cvtColor(face, cv2.COLOR_RGB2BGR)
                    #face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY) 
                                          
                    file_name_path = "photos_etudiants/etudiant."+str(id)+"."+str(img_id)+".jpg" 
                    # file_name_path = "photos_etudiants/etudiant."+str(id)+"."+str(img_id)+".jpg"                        
                    cv2.imwrite(file_name_path,sub_face)
                    cv2.putText(img,"Nombres de captures effectuées:",(10,30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2) #face en debut de fonction                        
                    cv2.putText(img,str(img_id),(10,90), cv2.FONT_HERSHEY_COMPLEX, 1.2, (255,255,255), 2)
                cv2.imshow("Enregistrement du visage", img)

                if cv2.waitKey(1)==27 or int(img_id) == 10: #if cv2.waitKey(1) or int(img_id) == 100:
                    # dire("Collecte d'image effectuées")
                    break
            
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo(f"Résultat","Image faciales de l'etudiant enregistrées", parent=self.tab3)

    def insert_etudiant(self):
        if self.var_tel_etudiant.get() =="" or self.var_nom_etudiant.get()=="" or self.var_prenom_etudiant.get()=="" or self.var_niveau_etudiant.get()=="Selectionner la classe"  or self.var_sexe_etudiant.get() =="Selectionner le sexe" or self.var_date_naissance_etudiant.get()=="" or self.var_lieu_naissance_etudiant.get() =="":
            messagebox.showerror("Erreur","Attention tous les champs sont requises !",parent=root)
        else:
            try:
                conn = connection.database_connection()
                my_curseur = conn.cursor()
                my_curseur.execute(f"SELECT * FROM `etudiant` WHERE id_etudiant={self.var_id_etudiant.get()}")
                resultat = my_curseur.fetchone()
                if resultat is not None:
                    print(resultat)                    
                    messagebox.showerror("Attention","cet identifiant existe déjà)",parent=self.tab3)
                    print("Cet identifiant existe déjà")                                        
                else:
                    my_curseur.execute("INSERT INTO `etudiant` (`prenom`, `nom`, `niveau`, `sexe`, `dateNaissance`, `lieuNaissance`, `telephone`, `absence_semestre`)VALUES (%s,%s,%s,%s,%s,%s,%s,0)",
                        ( 
                            self.var_prenom_etudiant.get(),
                            self.var_nom_etudiant.get(),
                            self.var_niveau_etudiant.get(),
                            self.var_sexe_etudiant.get(),
                            self.var_date_naissance_etudiant.get(),
                            self.var_lieu_naissance_etudiant.get(),
                            self.var_tel_etudiant.get(),
                        )
                    )
                    conn.commit()
                    self.afficher_infos_table()
                    # self.fetch_data()
                    # self.reset_data()
                    conn.close()
                    messagebox.showinfo("Succés","Enregistrement effectué)",parent=self.tab3)
                    print("Etudiant ajouté dans le systeme")

            except Exception as ex:
                messagebox.showinfo("Erreur",f"Une erreur est survenue: {str(ex.args)}",parent=self.tab3)
                print(f"Erreur {str(ex)} ")

    def reset_formulaire(self):
        self.var_id_etudiant.set(0)
        self.var_nom_etudiant.set("")
        self.var_prenom_etudiant.set("")
        self.var_date_naissance_etudiant.set("")
        self.var_niveau_etudiant.set("Selectionner le niveau")
        self.var_lieu_naissance_etudiant.set("")
        self.var_tel_etudiant.set("")
        self.var_sexe_etudiant.set("Selectionner le sexe")

    


if __name__ == "__main__":
    root=Tk()
    obj=pagePrincipal(root)
    root.mainloop()