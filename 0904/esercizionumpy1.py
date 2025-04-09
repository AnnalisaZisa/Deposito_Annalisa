import numpy as np

# vettore = np.arange(10, 50)

# print (vettore)

# print("Il tipo dato è:", vettore.dtype) #verifico il tipo di dato


# print("La forma dell'array è:", vettore.shape) #verifico la forma dell'array


# vettore_2 = np.array(vettore, dtype='float64') #cambio il tipo di dato

# print("Il vettore modificato è di tipo:", vettore_2.dtype) #stampo il nuovo tipo dato

# print("Il vettore modificato è: ", vettore_2) #stampo il nuovo array


#slicing -> tagliare pezzi di elementi
#indexing -> riportare l'indice preciso
#boolean indexing ci riporta tutti i valori da un cero punto in poi

# arr = np.array([1, 2, 3, 4, 5])

# print(arr[0]) #indexing

# print(arr[1:3]) #slicing

# print(arr[arr>2]) #boolean indexing

# arr_2d = np.array([ [1,2,3,4], [5,6,7,8], [9,10,11,12]])

# print(arr_2d[1:3])           #slicing sulle righe
# print(arr_2d[:, 1:3])        #slicing sulle colonne
# print(arr_2d[1:, 1:3])       #slicing misto

# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# print(arr[2:7])             #slicing base

# print(arr[1:8:2])           #slicing con passo

# print(arr[:5])              #omettere start e stop
# print(arr[5:])

# print(arr[-5:])             #utilizzare indici negativi
# print(arr[:-5])



arr = np.array ([10, 20, 30, 40, 50])

indices = np.array ([1, 3]) #utilizzo di un array di indici
print(arr[indices])

indices = [0, 2, 4]         #utilizzo di una lista di indici
print(arr[indices])