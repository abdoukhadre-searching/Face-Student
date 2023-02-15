from tkinter import messagebox
import dbconfig as connection
import datetime as dt
import time

def generer_absence():
    try:
        run_absence_confirmation = messagebox.askyesno("Absence","Confirmer le marquage des Absences pour la journée d'aujourd'hui ?")
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
                my_curseur.execute(f"SELECT * FROM `presence` WHERE idEtudiant = {id} AND date = '{date_aujourdhui}' AND status='Présent'")
                present_oui_non = my_curseur.fetchone()

                nom_prenom = etudiant[1] + " " + etudiant[2]
                if present_oui_non is not None:
                    # print(f"Etudiant  {etudiant[1], etudiant[2]} deja marque ou présent:\n)")# {present_oui_non}\n")
                    pass
                else:
                    # print(f"Etudiant: {etudiant[1], etudiant[2]} absent")
                    # inserer cet etudiant dans la liste avec status=absent
                    variables = (
                        date_aujourdhui,
                        "TD",
                        "PYTHON",
                        "Absent",
                        "Abdou Khadre Diop",
                        id,
                        nom_prenom,
                        "17:15",
                        heure_actuelle,
                    )
                    my_curseur.execute("INSERT INTO `presence` (`id`, `date`, `seance`, `matiere`, `status`, `enseignant`, `idEtudiant`, `nomPrenomEtudiant`, `heureDebut`, `heureFin`) VALUES (null, %s,%s,%s,%s,%s,%s,%s,%s,%s) ", variables)
                    conn.commit()
                    # print(f"..{nom_prenom} marqué absent pour aujourdhui..")
            
            conn.close()
            messagebox.showinfo("Absence",f"Marquage des Absences pour la date d'aujourd'hui {date_aujourdhui} effectué avec succés !")

    except Exception as e:

        print("erreur dans 'run_absence()'...",e)
        messagebox.showerror("Erreur",f"Attention une erreur est survenue: \n {str(e.args)}")
        print(f"Erreur {str(e)} ") 

#appel
generer_absence()