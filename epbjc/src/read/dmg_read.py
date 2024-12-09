import sqlite3

conex = sqlite3.connect('C:\Users\solan\Desktop\epbjc\epbjc\sqlite-database\epbjc.db')
cursor_dmg = conex.cursor()

cursor_dmg.execute('SELECT nome FROM champs_dmg WHERE nome = "Braum"')
resultados = cursor_dmg.fetchall()
 
for dmg in resultados:
    print(dmg)

conex.commit()
conex.close()