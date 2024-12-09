import sqlite3

conex = sqlite3.connect('C:\Users\solan\Desktop\epbjc\epbjc\sqlite-database\epbjc.db')
cursor_lanes = conex.cursor()

cursor_lanes.execute('''
CREATE TABLE IF NOT EXISTS champs_lanes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    lane TEXT NOT NULL
)
''')

cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Teemo", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Aurelion", "Mid")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Kindred", "Jgl")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Jhin", "Adc")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Braum", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Rell", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Seraphine", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Sona", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("LeBlanc", "Mid")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Swain", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Sylas", "Mid")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Ambessa", "Jgl")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Aurora", "Mid")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Smolder", "Adc")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Singed", "Top")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Gnar", "Top")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Darius", "Top")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Mordekaiser", "Top")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Rakan", "Sup")')
cursor_lanes.execute('INSERT INTO champs_lanes (nome, lane) VALUES ("Xayah", "Adc")')



conex.commit()
conex.close()