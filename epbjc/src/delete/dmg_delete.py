import sqlite3

conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\epbjc\\epbjc\\sqlite-database\\epbjc.db')
cursor_dmg = conex.cursor()

apagar_nome = input("Diga me o nome da linha a apagar ")

cursor_dmg.execute('DELETE FROM champs_dmg WHERE nome = ?',(apagar_nome,))

conex.commit()
conex.close()