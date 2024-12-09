Dentro da pasta create, no caminho C:\Users\solan\Desktop\epbjc\epbjc\src\create, estão 4 ficheiros; esses sendo:
champs_create.py
dmg_create.py
lanes_create.py
rift.db

Cada ficheiro tem a função de criar as tabelas
champs
champs_dmg
champs_lanes
respetivamente, sendo rift.db o resultado das operações das mesmas.

A tabela champs armazena o nome de um champion (além de autoincrementar o id)
A tabela champs_dmg armazena o nome e o tipo de dano de um champion (além de autoincrementar o id)
A tabela champs_lanes armazena o nome e a lane onde o champion é jogado (além de autoincrementar o id)




Dentro da pasta read, no caminho C:\Users\solan\Desktop\epbjc\epbjc\src\read, estão 3 ficheiros; esses sendo:
champs_read.py
dmg_read.py
lanes_read.py

Cada ficheiro tem a função de extrair os dados das tabelas criadas pelos ficheiros da pasta create, e mostra-los no terminal.

Um ciclo for é utilizado em cada ficheiro read para permitir a exibição da tabela no terminal linha a linha.


Dentro das pastas delete e update, estão os ficheiro com as respetivas funções dedicadas a cada tabela, ainda por trabalhar.
