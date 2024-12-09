import sqlite3

conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\epbjc\\epbjc\\sqlite-database\\epbjc.db')
cursor_lanes = conex.cursor()

cursor_lanes.execute('''UPDATE champs_lanes SET lane = "Top" WHERE id = 1''')

conex.commit()
conex.close()