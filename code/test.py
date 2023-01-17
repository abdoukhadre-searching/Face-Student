import dbconfig as connection
import datetime as dt

conn = connection.database_connection()
my_curseur = conn.cursor()

date_a_linstant = dt.date.today()
# date_a_linstant = str(date_a_linstant)
# date_a_linstant = date_a_linstant.replace("/","-")
print(date_a_linstant)
id = 143
my_curseur.execute(f"SELECT * FROM `presence` WHERE idEtudiant={id} and date='{date_a_linstant}'")
result=my_curseur.fetchall()
print(result)
conn.commit()
conn.close()