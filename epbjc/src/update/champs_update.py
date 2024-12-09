import sqlite3

conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\epbjc\\epbjc\\sqlite-database\\epbjc.db')
cursor = conex.cursor()

cursor.execute('''UPDATE champs SET nome = "Taric" WHERE id = 1''')

conex.commit()
conex.close()