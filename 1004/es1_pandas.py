import pandas as pd
import numpy as np

import random

names_arr = np.array(['Marco', 'Giulia', 'Francesco', 'Simone', 'Carla', 'Vittoria', 'Cesare'])
cities_arr = np.array(['Milano', 'Pavia', 'Torino', 'Roma', 'Palermo'])

num_persone = 6

names = []
cities = []


while len(names) < 6: 

    names.append(np.random.choice(names_arr))
   

    continue

while len(cities) < 6:

    cities.append(np.random.choice(cities_arr))

    continue

print (names)
print (cities)


age = np.linspace(0, 30, 6)
salary = np.linspace(800, 2000, 6)

print(age)
print(salary)


dataset = {'Nome': names, 'Eta': age, 'Citta': cities, 'Salario': salary}

df = pd.DataFrame(dataset)        
print(df)
    
df_prime_5= df.head(5)                                           #prime e le ultime 5 righe 
df_ultime_5= df.tail(5)

print(df_prime_5)
print(df_ultime_5)
print(df.dtypes)    


media_età =df['Età'].mean()                                       #calcolo media mediana e std per età
print(media_età)
mediana_età_età =df['Età'].median()
print(mediana_età_età)
std_età= df['Età'].std()
print(std_età)


media_salario =df['Salario'].mean()                                #calcolo media mediana e std per salario
print(media_salario)
mediana_salario =df['Salario'].median()
print(mediana_salario)
std_salario= df['Salario'].std()
print(std_salario)


df = df.drop_duplicates()                                           #rimuovo duplicati
print(df)


df['Età'].fillna(df['Età'].median(), inplace= True)                 #sostituisco NaN con la mediana

# Aggiungiamo una nuova colonna
df['Categoria_Età'] = np.where(df['Età'] < 18, 'Giovane',
                               np.where(df['Età'] <=95, 'Adulto', 'Senior'))

print(df)


