import sqlite3

conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\epbjc\\epbjc\\sqlite-database\\epbjc.db')
cursor_lanes = conex.cursor()

cursor_lanes.execute('SELECT * FROM champs_lanes')
resultados = cursor_lanes.fetchall()
 
for lane in resultados:
    print(lane)

conex.commit()
conex.close()