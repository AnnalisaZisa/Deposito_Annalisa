# file = open ("nome_file.txt","r") #aprire e leggere il file -> r = read

# riga = file.readline() # legge una singola riga del file
# tutte_le_righe = file.read()

# print(tutte_le_righe)

# print(riga)
# file.close()


# #scrittura di file
# file = open ("nome_file.txt", "w") #scrivere -> write

# file.write("Sto sostituendo il testo")
# file.close

file = open ("nome_file.txt", "a") #agiungere al testo
file.write("Sto sostituendo il testo")
file.close

with open("esempio_testo.txt", "w") as file:
    file.write("Auto chiudo la mia chiamata")
