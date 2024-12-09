import sqlite3

conex = sqlite3.connect('C:\Users\solan\Desktop\epbjc\epbjc\sqlite-database\epbjc.db')
cursor = conex.cursor()

cursor.execute('SELECT * FROM champs')
resultados = cursor.fetchall()
 
for champ in resultados:
    print(champ)

conex.commit()
conex.close()