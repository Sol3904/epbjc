import sqlite3

conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\epbjc\\epbjc\\sqlite-database\\epbjc.db')
cursor_dmg = conex.cursor()

cursor_dmg.execute('SELECT champ_nome FROM champs_dmg WHERE id = 1')
#cursor_dmg.execute('SELECT * FROM champs_dmg')
resultados = cursor_dmg.fetchall()
 
for dmg in resultados:
    print(dmg)

conex.commit()
conex.close()