from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkcalendar import DateEntry
import cv2
import dbconfig as connection
import os
import numpy as np
from datetime import datetime
import datetime as dt
import time


from infobip_api_client.api_client import ApiClient, Configuration
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest
from infobip_api_client.model.sms_destination import SmsDestination
from infobip_api_client.model.sms_response import SmsResponse
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.exceptions import ApiException

class pagePrincipal:
    def __init__(self,root):
        self.root = root
        self.root.title("FACE STUDENT 2022")
        self.root.geometry("1295x728+120+25")
        self.root.resizable(False, False)

        self.tabControl = ttk.Notebook(root)

        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)
        self.tab5 = ttk.Frame(self.tabControl)
        self.tab6 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text ='Authentification')
        self.tabControl.add(self.tab2, text ='Gestion enseignant')
        self.tabControl.add(self.tab3, text ="Gestion etudiant + traitements d'image")
        self.tabControl.add(self.tab4, text ="Gestion des comptes d'utilisateur")
        self.tabControl.add(self.tab5, text ="Gestion liste de présences")
        self.tabControl.add(self.tab6, text ="Gestion des séances et marquage")

        self.tabControl.pack(expand = 1, fill ="both")
        #self.tabControl.place(x=0,y=-10, )
        #-----------------------------------------------------
        # tab1_secondaire1 = ttk.Frame(self.tab1)
        # tab1_secondaire2 = ttk.Frame(self.tab1)
        # tabControl_tab1 = ttk.Notebook(self.tab1)
        #-----desactive tous les panels-----------------------
        self.tabControl.tab(0, state="normal")
        self.tabControl.tab(1, state="hidden")
        self.tabControl.tab(2, state="hidden")
        self.tabControl.tab(3, state="hidden")
        self.tabControl.tab(4, state="hidden")
        self.tabControl.tab(5, state="hidden")

        # ==================tab3 gestion etudiants
        titre_page = Label(self.tab3, text="Page de gestion des informations des Etudiants",font=("time new roman",16, "bold"),fg="black")
        titre_page.place(x=400, y=20)
        s_titre_page = Label(self.tab3, text="Système de Gestion des Présences des TD et TP - Copyright @2022 ",font=("time new roman",10),fg="black")
        s_titre_page.place(x=400, y=50)
        #==================tab6 gestion reconnaissance=
        titre_page_recog = Label(self.tab6, text="Panel pour la reconnaissance faciale et le marquage de présence",font=("time new roman",16, "bold"),fg="black")
        titre_page_recog.place(x=300, y=20)
        s_titre_page_recog = Label(self.tab6, text="Système de Gestion des Présences des TD et TP - Copyright @2022 ",font=("time new roman",10),fg="black")
        s_titre_page_recog.place(x=400, y=50)
        #==================tab5 gestion liste de presence
        titre_page_list = Label(self.tab5, text="Gestion de liste de presence au TD et TP",font=("time new roman",40, "bold"),fg="green")
        titre_page_list.place(x=100, y=20)
        s_titre_page_list = Label(self.tab5, text="Système de Gestion des Présences des TD et TP - Copyright @2022 ",font=("time new roman",17),fg="black")
        s_titre_page_list.place(x=200, y=90)

        #--Formulaire de seances de td  ou tp 
        self.var_id_enseignant = IntVar()
        self.var_matiere = StringVar()
        self.var_classe = StringVar()
        self.var_salle  = StringVar()
        self.var_heure_debut = StringVar()
        self.var_heure_fin = StringVar()
        self.var_type_seance = StringVar()

        #----var matire
        self.var_python= StringVar()

        
        lbl_debut = Label(self.tab6, font=("time new roman",12,"bold"),text="Heure de début",fg='black')
        lbl_debut.place(x=330,y=90)        
        h_debut_cbo = Combobox(self.tab6, textvariable=self.var_heure_debut,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        h_debut_cbo["values"]=("Debut","08:00:00","08:15:00","08:30:00","08:45:00","09:00:00","09:15:00","09:30:00","09:45:00","10:00:00","10:15:00","10:30:00","10:45:00")
        h_debut_cbo.current(0)
        h_debut_cbo.place(x=480,y=90,width=80)

        lbl_fin = Label(self.tab6, font=("time new roman",12,"bold"), text="Fin de séance",fg='black')
        lbl_fin.place(x=330,y=120)        
        h_fin_cbo = Combobox(self.tab6, textvariable=self.var_heure_fin,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        h_fin_cbo["values"]=("Fin","10:00:00","10:15:00","10:30:00","10:45:00","11:00:00","11:15:00","11:30:00","11:45:00","12:00:00","12:15:00","12:30:00","12:45:00","13:00:00")
        h_fin_cbo.current(0)
        h_fin_cbo.place(x=480,y=120,width=80)

        lbl_type_seance = Label(self.tab6,font=("time new roman",12,"bold"),text="Type de seance",fg='black')
        lbl_type_seance.place(x=20,y=90)
        type_seance_cbo = Combobox(self.tab6, textvariable=self.var_type_seance,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        type_seance_cbo.place(x=150,y=90,width=150)
        type_seance_cbo['values'] = ("Choisir","TD", "TP")
        type_seance_cbo.current(0)
        #contenu seance
        lbl_contenu_seance = Label(self.tab6,font=("time new roman",12,"bold"),text=" Rapport Contenu seance",fg='black')
        lbl_contenu_seance.place(x=20,y=120)
        contenu = Text(self.tab6,fg="black",font=("time new roman",12,"bold"),height=10,width=50,bg='white',relief=FLAT)
        contenu.place(x=25,y=160)

        lbl_matiere = Label(self.tab6, font=("time new roman",12,"bold"),text="Matière",fg='black')
        lbl_matiere.place(x=590,y=90)
        self.matiere_cbo = Combobox(self.tab6, textvariable=self.var_matiere,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        self.matiere_cbo["values"] = ('Java', 'Python', 'Algorithme', 'XML', 'Reseaux')
        self.matiere_cbo.current(0)
        # self.matiere_cbo.bind('<<ComboboxSelected>>',self.recup_matiere)
        self.matiere_cbo.place(x=680,y=90,width=300)

        lbl_classe = Label(self.tab6,font=("time new roman",12,"bold"),text="Classe",fg='black')
        lbl_classe.place(x=590,y=120)
        classe_cbo = Combobox(self.tab6, textvariable=self.var_classe,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        classe_cbo.place(x=680,y=120,width=300)
        classe_cbo['values'] = ("Sélectionner la classe","L1 SRT", "Licence 2", "Licence 3", "Master 1", "Master 2")
        classe_cbo.current(0)

        #--bouton engistrer 
        btn_save_seance = Button(self.tab6,bg="#174577",text="Enregister", foreground="white", command="",bd=0,cursor="hand2",activebackground="#174577")
        btn_save_seance.place(x=500,y=160,width=180,height=33)
        btn_modifier_seance = Button(self.tab6,bg="#174577",text="Modifier", foreground="white", command="",bd=0,cursor="hand2",activebackground="#174577")
        btn_modifier_seance.place(x=500,y=200,width=180,height=33)
        btn_marquage_seance = Button(self.tab6,bg="green",text="Lancer la reconnaissance", foreground="white", command=self.lancer_reconnaissance_seance,bd=0,cursor="hand2",activebackground="lightgreen")
        btn_marquage_seance.place(x=500,y=240,width=180,height=33)



        

        #===================================================================

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

        champ_username = Entry(self.tab1, textvariable=self.var_login ,relief="flat", font=("Arial", 12)) #flat, groove, raised, ridge, solid, or sunken
        champ_username.place(x=370, y=431)   
        champ_password = Entry(self.tab1, textvariable=self.var_password, relief="flat", font=("Arial", 12)) #flat, groove, raised, ridge, solid, or sunken
        champ_password.place(x=370, y=508)

        self.var_id_etudiant = IntVar() #integer in db
        self.var_nom_etudiant = StringVar()
        self.var_niveau_etudiant = StringVar()
        self.var_prenom_etudiant = StringVar()
        self.var_sexe_etudiant = StringVar()
        self.var_date_naissance_etudiant = StringVar()
        self.var_lieu_naissance_etudiant = StringVar()
        self.var_tel_etudiant = StringVar()

        self.matiere_v_coches = []
        self.matiere_no_v_coches = []
              

        
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
        niveau_combo= ttk.Combobox(self.tab3,foreground='#174577' , textvariable=self.var_niveau_etudiant ,font=("time new roman",12, "bold"), state="readonly")
        niveau_combo.place(x=490,y=140)
        niveau_combo["values"] = ("Sélectionner le niveau","Licence 1", "Licence 2", "Licence 3", "Master 1", "Master 2")
        niveau_combo.current(0)
        # niveau_combo.bind("<<ComboboxSelected>>",self.get_matiere_unvalidate())

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
        lieuNaissance_etudiant.place(x=560,y=220, width=135)

        matiere_etudiant_lbl = Label(self.tab3, text="Matière(s) non validé(s)",font=("time new roman",12, "bold"),fg="red")
        matiere_etudiant_lbl.place(x=725, y=100)

        #------------------------------
        # for scrolling vertically
        yscrollbar = Scrollbar(self.tab3)
        yscrollbar.pack(side = RIGHT, fill = Y)

        yscrollbar2 = Scrollbar(self.tab3)
        yscrollbar2.pack(side = RIGHT, fill = Y)
        
        self.var_matiere_valide = StringVar()

        self.list_matiere_nonValide = Listbox(self.tab3, bd=0, justify="center", height= 5 ,selectmode = "multiple", yscrollcommand = yscrollbar.set)
        self.list_matiere_nonValide.place(x=755,y=135)

        self.confirm_btn = Button(self.tab3, text=" Confirmer ", bg="red",fg="white", command= self.get_matiere_unvalidate)
        self.confirm_btn.place(x=780, y=220)
        
        self.list_matiere_valide = Listbox(self.tab3, bg="red",bd=0,justify="center", height= 5 ,selectmode = "multiple", yscrollcommand = yscrollbar2.set)
        self.list_matiere_valide.place(x=980,y=135)

        self.confirm_btn = Button(self.tab3, text=" Confirmer ", bg="green",fg="white", command= self.get_matiere_validate)
        self.confirm_btn.place(x=1000, y=220)

        matiere = ["C","Reseaux","ATO","Java","Python"]
        
        for each_item in range(len(matiere)):            
            self.list_matiere_nonValide.insert(END, matiere[each_item])
            self.list_matiere_nonValide.itemconfig(each_item, bg = "white")

            self.list_matiere_valide.insert(END, matiere[each_item])
            self.list_matiere_valide.itemconfig(each_item, bg = "white")
            
        # Attach listbox to vertical scrollbar
        yscrollbar.config(command = self.list_matiere_nonValide.yview)
        yscrollbar.config(command = self.list_matiere_valide.yview)

        yscrollbar2.config(command = self.list_matiere_nonValide.yview)
        yscrollbar2.config(command = self.list_matiere_valide.yview)
        #------------------------------

        matiere_etudiant_lbl = Label(self.tab3, text="Matière(s) validé(s)",font=("time new roman",12, "bold"),fg="green")
        matiere_etudiant_lbl.place(x=950, y=100)

        contactEtudiant_lbl = Label(self.tab3, text="Numero telephone",font=("time new roman",12, "bold"),fg="black")
        contactEtudiant_lbl.place(x=400, y=100)
        # lbl = Label(self.tab3,image=img, bg='#174577')
        # lbl.place(x=840,y=135,height=33,width=220)
        contactEtudiant_entry = Entry(self.tab3, fg ="#174577",textvariable=self.var_tel_etudiant,relief=FLAT,font=("time new roman",12, "bold"))
        contactEtudiant_entry.place(x=550,y=100, width=145)

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
        btn_supprime_image_etudiant = Button(self.tab3,bg="#174577",text="Actualiser", foreground="white", command=self.afficher_infos_table,bd=0,cursor="hand2",activebackground="#174577")
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


        self.student_table= ttk.Treeview(table_frame, columns=("id","prenom","nom","niveau","sexe","dateNaissance","lieuNaissance","telephoneEtudiant","absence_matiere", "matiere_v", "matiere_no_v"),xscrollcommand=scroll_x.set,yscrollcommand= scroll_y.set)
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
        self.student_table.heading("absence_matiere",text="Absences matieres")        
        self.student_table.heading("matiere_v",text="Matiere(s) valide(s)")
        self.student_table.heading("matiere_no_v",text="Matiere(s)non valide(s)")

        #`id_eleve`, `nom`, `adresse`, `dateNaissance`, `niveau`, `niveau`, `sexe`, `domaine`, `annee`, `contactParent`, `enseignant`, `semestre`, `photo`

        self.student_table.column("id",width=100,stretch=0)
        self.student_table.column("prenom",width=100,stretch=0)
        self.student_table.column("nom",width=100,stretch=0)
        self.student_table.column("niveau",width=100,stretch=0)
        self.student_table.column("sexe",width=100,stretch=0)
        self.student_table.column("dateNaissance",width=135,stretch=0)
        self.student_table.column("lieuNaissance",width=135,stretch=0)
        self.student_table.column("telephoneEtudiant",width=120,stretch=0)
        self.student_table.column("absence_matiere",width=140,stretch=0)
        self.student_table.column("matiere_v",width=100)
        self.student_table.column("matiere_no_v",width=100)


        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_datatable)
        #self.student_table.bind("<ButtonRelease>",self.get_data_alert_sms)
        self.afficher_infos_table()


        #-------- Tableau  tab5  liste de presence  Etudiant ---------------
        table_frame_liste=Frame(self.tab5, bd=2, relief=RIDGE)
        table_frame_liste.place(x=0, y=235, width=1330, height=670) #w=1226

        scroll_x_= ttk.Scrollbar(table_frame_liste, orient= HORIZONTAL)
        scroll_y_= ttk.Scrollbar(table_frame_liste, orient= VERTICAL)


        self.studente_liste_presence= ttk.Treeview(table_frame_liste, columns=("id","date","seance","matiere","status","enseignant","idEtudiant","nomPrenomEtudiant","heureDebut","heureFin"),xscrollcommand=scroll_x_.set,yscrollcommand= scroll_y_.set)
        s = ttk.Style()
        s.configure('Treeview', rowheight= 40)
        s.configure("Treeview.Heading", font=("time new roman", 10, "bold"))
        scroll_x_.pack(side=BOTTOM, fill=X)
        scroll_y_.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.studente_liste_presence.xview)
        scroll_y_.config(command=self.studente_liste_presence.yview)

        self.studente_liste_presence.heading("id",text="ID")
        self.studente_liste_presence.heading("date",text="Date")
        self.studente_liste_presence.heading("seance",text="Type de seance")
        self.studente_liste_presence.heading("matiere",text="Matiere")
        self.studente_liste_presence.heading("status",text="Status")
        self.studente_liste_presence.heading("enseignant",text="Enseignant")
        self.studente_liste_presence.heading("idEtudiant",text="Code Etudiant")
        self.studente_liste_presence.heading("nomPrenomEtudiant",text="Prenom Nom")
        self.studente_liste_presence.heading("heureDebut",text="Heure de debut")        
        self.studente_liste_presence.heading("heureFin",text="Heure de fin")

        #`id_eleve`, `nom`, `adresse`, `dateNaissance`, `niveau`, `niveau`, `sexe`, `domaine`, `annee`, `contactParent`, `enseignant`, `semestre`, `photo`

        self.studente_liste_presence.column("id",width=100,stretch=0)
        self.studente_liste_presence.column("date",width=100,stretch=0)
        self.studente_liste_presence.column("seance",width=100,stretch=0)
        self.studente_liste_presence.column("matiere",width=100,stretch=0)
        self.studente_liste_presence.column("status",width=100,stretch=0)
        self.studente_liste_presence.column("enseignant",width=135,stretch=0)
        self.studente_liste_presence.column("idEtudiant",width=135,stretch=0)
        self.studente_liste_presence.column("nomPrenomEtudiant",width=120,stretch=0)
        self.studente_liste_presence.column("heureDebut",width=140,stretch=0)
        self.studente_liste_presence.column("heureFin",width=140,stretch=0)


        self.studente_liste_presence["show"]="headings"
        self.studente_liste_presence.pack(fill=BOTH,expand=1)
        self.studente_liste_presence.bind("<ButtonRelease>", self.get_liste_presence_details)
        self.afficher_liste()

        # champ de recherche
        self.var_recherche = StringVar()
        self.var_matieres_filter = StringVar()
        self.var_nb_presence_matiere = IntVar()

        recherche_cbo = Combobox(self.tab5, textvariable=self.var_recherche, foreground="black" ,font=("time new roman",25, "bold"), state="readonly")
        recherche_cbo["values"]=("Présent","Absent")
        recherche_cbo.current(0)
        recherche_cbo.place(x=420, y=150) 
        recherche_label= Label(self.tab5, text="Filtrer les ",fg="black",font=("Arial", 23)) #flat, groove, raised, ridge, solid, or sunken
        recherche_label.place(x=200, y=150)
        recherche_btn= Button(self.tab5, text="Rechercher",bg="lightgreen",command=self.filtre,relief=FLAT, fg="black",font=("Arial", 15)) #flat, groove, raised, ridge, solid, or sunken
        recherche_btn.place(x=820, y=150)
        actualiser_btn= Button(self.tab5, text="Actualiser",bg="grey",command=self.actualiser_liste,relief=FLAT, fg="black",font=("Arial", 15)) #flat, groove, raised, ridge, solid, or sunken
        actualiser_btn.place(x=950, y=150)
        gen_absence_btn= Button(self.tab5, text="Generer absence",bg="green",command=self.generer_absence,relief=FLAT, fg="white",font=("Arial", 15)) #flat, groove, raised, ridge, solid, or sunken
        gen_absence_btn.place(x=1060, y=150)

        lab_matiere= Label(self.tab5, text="Matières",fg="black",font=("Arial", 15)) #flat, groove, raised, ridge, solid, or sunken
        lab_matiere.place(x=200, y=200)
        matiere_cbo = Combobox(self.tab5, textvariable=self.var_matieres_filter, foreground="black" ,font=("time new roman",15, "bold"), state="readonly")
        matiere_cbo["values"]=("Réseaux","Python", "ATO", "C")
        matiere_cbo.current(0)
        matiere_cbo.place(x=300, y=200) 
        nombre_presence_par_matiere= Label(self.tab5, textvariable=self.var_nb_presence_matiere,fg="red",font=("Arial", 30)) #flat, groove, raised, ridge, solid, or sunken
        nombre_presence_par_matiere.place(x=80, y=180)
        label__= Label(self.tab5, text="Code etudiant: ",fg="black",font=("Arial", 15)) #flat, groove, raised, ridge, solid, or sunken
        label__.place(x=700, y=200)

        self.var_id = IntVar()
        label__= Label(self.tab5, textvariable=self.var_id,fg="black",font=("Arial", 15)) #flat, groove, raised, ridge, solid, or sunken
        label__.place(x=870, y=200)

        bouton_= Button(self.tab5, command=self.nombre_absence_par_matiere, text="Calculer",fg="white",bg="blue",font=("Arial", 10)) #flat, groove, raised, ridge, solid, or sunken
        bouton_.place(x=600, y=200)
        

    def get_liste_presence_details(self, event=""):
        cursor_focus = self.studente_liste_presence.focus()
        content = self.studente_liste_presence.item(cursor_focus)
        donnees = content["values"]
        print("Donnee tableau etudiant:\n",donnees)
        self.var_id.set(donnees[6])
        

    def nombre_absence_par_matiere(self):
        try:
            conn = connection.database_connection()
            my_curseur = conn.cursor()
            my_curseur.execute(f"SELECT COUNT(*) FROM `presence` WHERE idEtudiant='{self.var_id.get()}' and matiere = '{self.var_matieres_filter.get()}' and status = '{self.var_recherche.get()}' ")   
            nb_absence = my_curseur.fetchone()
            print(nb_absence[0])
            self.var_nb_presence_matiere.set(nb_absence[0])
            conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showinfo("Erreur",f"Une erreur est survenue: {str(ex.args)}")
            print(f"Erreur lors de la requette :{str(ex)}")

        
    def get_matiere_unvalidate(self):            
        
        cname = self.list_matiere_nonValide.curselection()
        for i in cname:
            op = self.list_matiere_nonValide.get(i)
            self.matiere_v_coches.append(op)
        # for val in self.matiere_v_coches:
        print(self.matiere_v_coches)

    def get_matiere_validate(self):            
        self.matiere_no_v_coches = []
        cname = self.list_matiere_valide.curselection()
        for i in cname:
            op = self.list_matiere_valide.get(i)
            self.matiere_no_v_coches.append(op)
        # for val in self.matiere_no_v_coches:
        print(self.matiere_no_v_coches)

    def generer_absence(self):
        try:
            run_absence_confirmation = messagebox.askyesno("Absence","Confirmer le marquage des Absences pour la journée d'aujourd'hui ?", parent=self.tab5)
            if run_absence_confirmation  > 0 :
                conn = connection.database_connection()
                my_curseur = conn.cursor()
                # print("genration liste d'absence en cours...")
                my_curseur.execute(f"SELECT * FROM `etudiant`")
                etudiants = my_curseur.fetchall()
                # print(f"\nEtape 1: L'ensemble des etudiants....\n{etudiants}\n")

                #on recupere la date d'aujourdhui
                date_aujourdhui = dt.date.today()
                date_aujourdhui = date_aujourdhui.strftime("%Y-%m-%d")          
                # print(date_aujourdhui)           

                # print("Etape 2: Récupère id de l'etudiant ...\n")
                heure_actuelle = time.strftime("%H:%M:%S")

                for etudiant in etudiants: 
                    # print(f"Infos d'un etudiant: \n {etudiant}\n")
                    # print(f"ID meme etudiant: {etudiant[0]}\n")
                    id = etudiant[0]

                    # verifie si cet etudiant est deja present pour la date d'aujourdhui
                    my_curseur.execute(f"SELECT * FROM `presence` WHERE idEtudiant = {id} AND date = '{date_aujourdhui}' ")#AND status='Présent'")
                    present_oui_non = my_curseur.fetchone()

                    nom_prenom = etudiant[1] + " " + etudiant[2]
                    if present_oui_non is not None:
                        # print(f"Etudiant  {etudiant[1], etudiant[2]} deja marque ou présent:\n)")# {present_oui_non}\n")
                        pass
                    else:
                        # on verifie si cet etudaint a valider cette matiere...
                        my_curseur.execute(f"SELECT * FROM `etudiant` WHERE id_etudiant = {id}")
                        etudiant = my_curseur.fetchone() 
                        liste_des_matire_valide_par_etu = etudiant[9]
                        print(f"Etudiant: {(liste_des_matire_valide_par_etu)}")
                        
                        # inserer cet etudiant dans la liste avec status=absent
                        matiere="Python"

                        if str(matiere) in liste_des_matire_valide_par_etu:
                            variables = (
                                date_aujourdhui,
                                "TD",
                                matiere,
                                "VALIDE",
                                "Abdou Khadre Diop",
                                id,
                                nom_prenom,
                                "17:15",
                                heure_actuelle,
                            )
                            my_curseur.execute("INSERT INTO `presence` (`id`, `date`, `seance`, `matiere`, `status`, `enseignant`, `idEtudiant`, `nomPrenomEtudiant`, `heureDebut`, `heureFin`) VALUES (null, %s,%s,%s,%s,%s,%s,%s,%s,%s) ", variables)
                            my_curseur.execute(f"UPDATE `etudiant` SET absence_matiere = absence_matiere + 1 WHERE id_etudiant = {id}")
                            conn.commit()
                        else: 
                            variables = (
                                date_aujourdhui,
                                "TD",
                                matiere,
                                "Absent",
                                "Abdou Khadre Diop",
                                id,
                                nom_prenom,
                                "17:15",
                                heure_actuelle,
                            )
                            my_curseur.execute("INSERT INTO `presence` (`id`, `date`, `seance`, `matiere`, `status`, `enseignant`, `idEtudiant`, `nomPrenomEtudiant`, `heureDebut`, `heureFin`) VALUES (null, %s,%s,%s,%s,%s,%s,%s,%s,%s) ", variables)
                            my_curseur.execute(f"UPDATE `etudiant` SET absence_matiere = absence_matiere + 1 WHERE id_etudiant = {id}")
                            conn.commit()
                            print(f"..{nom_prenom} marqué absent pour aujourdhui..")
                
                conn.close()
                messagebox.showinfo("Absence",f"Marquage des Absences pour la date d'aujourd'hui {date_aujourdhui} effectué avec succés !", parent=self.tab5)
                self.actualiser_liste()

        except Exception as e:

            print("erreur dans 'run_absence()'...",e)
            messagebox.showerror("Erreur",f"Attention une erreur est survenue: \n {str(e.args)}")
            print(f"Erreur {str(e)} ") 
    
    def envoie_sms(self, contact, nom_eleve):
            BASE_URL = "ejl32n.api.infobip.com"
            API_KEY = "d83cb93f2a1322ac17f450a802290ae8-9e283a45-6f53-4922-b3d9-643cd7db4d78"

            client_config = Configuration(
                host= BASE_URL,
                api_key={"APIKeyHeader": API_KEY},
                api_key_prefix={"APIKeyHeader": "App"},
            )

            api_client = ApiClient(client_config)

            sms_request = SmsAdvancedTextualRequest(
                messages = [
                    SmsTextualMessage(
                        destinations=[
                            SmsDestination(
                                to=str(contact),
                            ),
                        ],
                        _from="SMS UABD",
                        text=f"Bonjour chère etudiant  {nom_eleve}  nous somme navré mais vous a cumulé plus de 2 absences non justifiées au cours de cette semaine.\n Votre présence au sein de l'administration est vivement souhaité durant cette semaine pour soumettre des motifs de votre absence régulière",
                    )
                ]
            )

            api_instance = SendSmsApi(api_client)

            try:
                api_response: SmsResponse = api_instance.send_sms_message(sms_advanced_textual_request=sms_request)
                print(api_response)
                messagebox.showinfo("Message Envoyé","Envoie réussi !\nMessage reçu par l'etudiant'",parent=self.root)
            except ApiException as ex:
                print("Erreur lors de l'envoie du message au Parent.")
                messagebox.showerror("Problème","Erreur lors de l'envoie du Message à l'etudiant ou peut etre du a un probleme de réseaux",parent=self.root)
                print(ex)     
    
    def get_data_alert_sms(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        print(data)
        # self.var_nom_eleve.set(data[1]+' '+ data[2]),
        # self.var_contact_parent.set(data[4])
        send_sms = messagebox.askyesno("Envoie de message",f"Confirmer l'envoie du message vers cet etudiant:\n Prenom nom: {data[1]+' '+ data[2]} \n Telephone: {data[7]}", parent=self.root)
        
        if send_sms > 0 :
            # pass
            nom_prenom = data[1]+' '+ data[2]
            self.envoie_sms(str(data[7]), nom_prenom)
            conn = connection.database_connection()
            my_curseur = conn.cursor()            
            val=(data[0],)
            # reset du nombre absence semestre a zero
            sql_sup="UPDATE `eleve` SET absence_matiere = 0 WHERE id_etudiant=%s"            
            my_curseur.execute(sql_sup,val)

            # sql = "DELETE FROM `liste_rouge` WHERE id_eleve=%s"
            # my_curseur.execute(sql,val)            
           
            conn.commit()
            conn.close()            
            # self.show_liste_rouge()


    
    def filtre(self):
        try:
            conn = connection.database_connection()
            my_curseur = conn.cursor()
            my_curseur.execute(f"SELECT * FROM `presence` where status like '{self.var_recherche.get()}'")   
            etudiants = my_curseur.fetchall()
            if len(etudiants) != 0:
                self.studente_liste_presence.delete(*self.studente_liste_presence.get_children())  
                for etu in etudiants:
                    self.studente_liste_presence.insert("", END,values=etu)
                    conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showinfo("Erreur",f"Une erreur est survenue: {str(ex.args)}")
            print(f"Erreur lors l'affichage :{str(ex)}")

        
    def actualiser_liste(self):
        self.afficher_liste()

    def afficher_liste(self):
        try:
            conn = connection.database_connection()
            my_curseur = conn.cursor()
            my_curseur.execute("SELECT * FROM `presence`")   
            etudiants = my_curseur.fetchall()
            if len(etudiants) != 0:
                self.studente_liste_presence.delete(*self.studente_liste_presence.get_children())  
                for etu in etudiants:
                    self.studente_liste_presence.insert("", END,values=etu)
                    conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showinfo("Erreur",f"Une erreur est survenue: {str(ex.args)}")
            print(f"Erreur lors l'affichage :{str(ex)}")


    def lancer_reconnaissance_seance(self):
        face_classifier=cv2.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")
        model_clf = cv2.face.LBPHFaceRecognizer_create()
        model_clf.read("model/model.xml")
        cap =cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        # Pour assurer une seule insertion dans le marquage
        variable = True

        # variable etudiant
        prenom_etudiant = ""
        nom_etudiant = ""

        # img_id=0
        while True:
            ret,img=cap.read() # Recupere video depuis Webcam
            gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            visages=face_classifier.detectMultiScale(img, 1.7, 5)#(img, 1.05, 6)
            visages=face_classifier.detectMultiScale(gray, 1.7, 5)
            #-------- Redimensionner l'Image ---------------
            minisize = (img.shape[1],img.shape[0])
            miniframe = cv2.resize(img, minisize)
            visages =  face_classifier.detectMultiScale(miniframe)
            couleur = (100,255,255)
            couleur_verte = (0,255,0)
            cv2.putText(img,"Reconnaissance faciale + Marquage ",(10,30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2) 
            cv2.putText(img,f"Date-Heure: {str(datetime.now())}",(10,60), cv2.FONT_HERSHEY_COMPLEX,0.6,(100,55,255),2)                        

            for (x,y,w,h) in visages:
                # on recupere l'id et le taux de precision [0:1]
                id,predict=model_clf.predict(gray[y:y+h,x:x+w])

                taux_de_precision=int((100 * (1-predict/300)))
                print(f"ID Etudiant: {id} ___ Taux de precision {taux_de_precision} %")

                try:
                    conn = connection.database_connection()
                    my_curseur = conn.cursor()
                    my_curseur.execute("SELECT id_etudiant,prenom,nom FROM `etudiant` WHERE id_etudiant="+str(id))
                    result=my_curseur.fetchone()
                    if result is not None:
                        id_etudiant = result[0]
                        prenom_etudiant = result[1]
                        nom_etudiant = result[2]
                        print("Informations étudiants:\n", prenom_etudiant, nom_etudiant)      


                    else:
                        pass
                except Exception as ex:
                    print(f"Erreur: {str(ex)}")
                    messagebox.showinfo("Erreur",f"Attention une erreur est survenue lors d'une requette: \n{str(ex)}")

                if taux_de_precision > 75:  
                    cv2.rectangle(img, (x,y), (x+w,y+h), (couleur_verte),2) 
                    # cv2.rectangle(img,(x-2,y+h+65),(x+w,y+h+5),(0,150,0),-4)
                    cv2.putText(img,f"Nom prenom: {prenom_etudiant} {nom_etudiant}",(x+5,y+h+20), cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),2) 
                    cv2.putText(img,f"Code Etudiant: {id}",(x+5,y+h+45), cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),2)   
                    
                    # -------------Insertion de cet etudiant dans la table presence pour le marquage...
                    
                    date_a_linstant = dt.date.today()
                    date_a_linstant = str(date_a_linstant)
                    date_a_linstant = date_a_linstant.replace("/","-")
                    #date_a_linstant = date_a_linstant.strftime("%y/%m/%d")
                    heure_actuelle = time.strftime("%H:%M:%S")

                    seance = "TD" # wala TP
                    matiere ="PYTHON"
                    status = "Présent"
                    enseignant = "Monsieur Dahirou Gueye"
                    idEtudiant =  id    
                    nomPrenomEtudiant = f"{prenom_etudiant} {nom_etudiant}"
                    heureDebut = "18:00"
                    heureFin = heure_actuelle

                    requette = "INSERT INTO `presence` (`id`, `date`, `seance`, `matiere`, `status`, `enseignant`, `idEtudiant`, `nomPrenomEtudiant`, `heureDebut`, `heureFin`) VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    
                    conn = connection.database_connection()
                    my_curseur = conn.cursor()
                    
                    if variable:                        
                        # my_curseur.execute(requette, (date_a_linstant, seance, matiere, status, enseignant, idEtudiant, nomPrenomEtudiant, heureDebut, heureFin))
                        # conn.commit()
                        # # conn.close()
                        # variable = False                    
                        # print("..marquage effectué avec succes !..")
                        pass
                    
                    # Verifie si l'etudiant est déja marqué
                    try:  
                        my_curseur.execute(f"SELECT * FROM `presence` WHERE idEtudiant = '{id}' AND date = '{str(date_a_linstant)}'")
                        result=my_curseur.fetchall()
                        print("result", result)
                        if len(result) == 0: # si on a pas de resultat
                            if variable: 
                                # inserer presence
                                my_curseur.execute(requette, (date_a_linstant, seance, matiere, status, enseignant, idEtudiant, nomPrenomEtudiant, heureDebut, heureFin))
                                conn.commit()
                                # conn.close()
                                variable = False                    
                                print("..marquage effectué avec succes !..")                                                                                            
                        else: # deja present pour cette date
                            cv2.putText(img,"Etudiant Present",(x+5,y+h+65), cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2) 
                            print("Etudiant Present aujourd'hui")
                            
                            
                    except Exception as ex:
                        print(f"Erreur: {str(ex)}")                 
                    


                else:              
                    cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255),2)                        
                    cv2.putText(img,"Tentative de reconnaissance de visage...",(x-5,y+h+15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (couleur), 2)

            cv2.imshow("Enregistrement du visage", img)


            if cv2.waitKey(1)==27: #if cv2.waitKey(1) or int(img_id) == 100:
                # dire("Collecte d'image effectuées")
                break
        
        cap.release()
        cv2.destroyAllWindows()

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
        self.tabControl.tab(5, state="hidden")

    def vers_tab2(self):
        login = self.var_login.get()
            # controle de saise
        if login == "":
            messagebox.showerror('Erreur', "Champ login obligatoire", parent=self.tab1)
        elif self.var_password.get() == "":
            messagebox.showerror('Erreur', "Champ mot de passe obligatoire", parent=self.tab1)
        elif  messagebox.showinfo("Authentification réussi","Bienvenue sur votre espace de travail !!", parent=self.tab1) == 'ok' :
            #--on efface les formulaire
            self.var_login.set("")
            self.var_password.set("")
            self.tabControl.select(2) # gestin etudaint
            self.tabControl.tab(0, state="hidden")
            self.tabControl.tab(1, state="normal")
            self.tabControl.tab(2, state="normal")
            self.tabControl.tab(3, state="normal")
            self.tabControl.tab(4, state="normal")
            self.tabControl.tab(5, state="normal")

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

                if cv2.waitKey(1)==27 or int(img_id) == 30: #if cv2.waitKey(1) or int(img_id) == 100:
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
                    my_curseur.execute("INSERT INTO `etudiant` (`prenom`, `nom`, `niveau`, `sexe`, `dateNaissance`, `lieuNaissance`, `telephone`, `absence_matiere`, `matiere_valide`, `matiere_non_valide` ) VALUES (%s,%s,%s,%s,%s,%s,%s,0,%s,%s)",
                        ( 
                            self.var_prenom_etudiant.get(),
                            self.var_nom_etudiant.get(),
                            self.var_niveau_etudiant.get(),
                            self.var_sexe_etudiant.get(),
                            self.var_date_naissance_etudiant.get(),
                            self.var_lieu_naissance_etudiant.get(),
                            self.var_tel_etudiant.get(),
                            str(self.matiere_v_coches),
                            str(self.matiere_no_v_coches)
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