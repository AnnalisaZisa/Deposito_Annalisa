import sqlite3  # Importa il modulo per lavorare con SQLite

# Creiamo db
conn = sqlite3.connect('scuola.db')

# Definiamo il cursore
cur = conn.cursor()

# Creiamo la tabella studenti
cur.execute('''
    CREATE TABLE IF NOT EXISTS studenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')

## Inseriamo i nomi alla tabella
while True: 

    scelta = input("Vuoi aggiungere uno studente? ")
    if scelta == "si": 
        cur.execute("INSERT INTO studenti (nome) VALUES (?)", (input("Inserisci il nome dello studente "),)) 

    else: 
        break

# Salviamo le modifiche
conn.commit()


# Stampiamo i dati
cur.execute("SELECT * FROM studenti")
righe = cur.fetchall()

for riga in righe:
   print(riga)

# Raggruppo per nomi
cur.execute("SELECT nome, COUNT(*) AS numero_studenti, FROM studenti, GROUP BY nome")


# Cancelliamo i dati per non intasare il db
#cur.execute("DELETE FROM studenti where id NOT IN (" ")")
#conn.commit()

# Chiudiamo la connessione
conn.close() 

