import sqlite3

conex = sqlite3.connect('C:\Users\solan\Desktop\epbjc\epbjc\sqlite-database\epbjc.db')
cursor = conex.cursor()

cursor.execute('SELECT * FROM champs_lanes')
resultados = cursor.fetchall()
 
for lane in resultados:
    print(lane)

conex.commit()
conex.close()