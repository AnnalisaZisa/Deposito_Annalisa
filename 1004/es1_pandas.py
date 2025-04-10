import pandas as pd
import numpy as np

names_arr = np.array(['Marco', 'Giulia', 'Francesco', 'Simone', 'Carla', 'Vittoria', 'Cesare'])
cities_arr = np.array(['Milano', 'Pavia', 'Torino', 'Roma', 'Palermo'])
age = np.linspace(0, 30, 6)
salary = np.linspace(0, 2000, 6)


names = []
cities = []
while len(names) < 6: 

    names.append(np.random.choice(names_arr, size = 6))
    cities.append(np.random.choice(cities_arr, size = 6))

    break

dataset = {'Nome': names, 'Eta': age, 'Citta': cities, 'Salario': salary}

df = pd.DataFrame(dataset)        
print(df)
    



