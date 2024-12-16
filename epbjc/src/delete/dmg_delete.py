import sqlite3

conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\epbjc\\epbjc\\sqlite-database\\epbjc.db')
cursor_dmg = conex.cursor()

apagar_nome = input("Diga me o nome da linha a apagar ")

try:
 cursor_dmg.execute('DELETE FROM champs_dmg WHERE champ_nomenome = ?',(apagar_nome,))
except:
 print("O nome não foi encontrado")




conex.commit()
conex.close()