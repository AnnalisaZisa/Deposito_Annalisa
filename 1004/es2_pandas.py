import pandas as pd
import numpy as np


dataset = {'Prodotto': ['pane', 'mele', 'pere', 'patate'],                          #creazione dataset
           'Quantita' : [3, 4, 5, 6],
           'prezzo/1': [1, 1.2, 2.4, 0.6],
           'Città': ['Catania', 'Roma', 'Milano', 'Salerno']
           }

df = pd.DataFrame(dataset)        
print(df)


df['Totale Vendite'] = df['Quantita'] * df['prezzo/1']
print(df)

tot_vendite_per_prodotto = df.groupby('Prodotto')['Totale Vendite'].sum()
print(tot_vendite_per_prodotto)                                                 #mi esce float64 perché?


max_quant_prod = df.groupby('Prodotto')['Quantita'].max()
print(max_quant_prod)      

vendite_per_citta = df.groupby('Città')['Totale Vendite'].max()
citta_max_vendite = vendite_per_citta.idxmax()                              #idmax -> trova l'indice col valore max
print(citta_max_vendite)



vendite_sopra_1000 = df[df['Totale Vendite'] > 1000]

df_ordinato = df.sort_values(by='Totale Vendite', ascending=False)

conteggio_per_città = df['Città'].value_counts()

