import sqlite3

conex = sqlite3.connect('C:\\Users\\solan\\Desktop\\epbjc\\epbjc\\sqlite-database\\epbjc.db')
cursor = conex.cursor()

pergunta = input("Quer apagar a tabela champs? ")
if pergunta == "sim":
    crtz = input("Tem a certeza? ")
    if crtz == "sim":
        absoluta = input("Tem a certeza absoluta? ")
        if absoluta == "sim":
            warning = input("Cuidado que vai tudo á vida, quer MESMO? ")
            if warning == "sim":
                cursor.execute('DELETE FROM champs')

if pergunta or crtz or absoluta or warning == "nao":
    print("Obrigada meu")

conex.commit()
conex.close()