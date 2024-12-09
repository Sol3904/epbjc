import sqlite3

conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\epbjc\\epbjc\\sqlite-database\\epbjc.db')
cursor_dmg = conex.cursor()

cursor_dmg.execute('''UPDATE champs_dmg SET nome = "Taric" WHERE id = 1''')

conex.commit()
conex.close()