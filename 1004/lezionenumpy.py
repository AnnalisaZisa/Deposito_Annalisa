import numpy as np


arr = np.linspace(0, 1, 5)                      #genera un array di numeri equidistanti tra un valore iniziale e uno finale 
print(arr)                                      #numero inizio -> 0; numero fine -> 1; grandezza vettore -> 5


                                                #random -> crea un array di numeri casuali
random_arr = np.random.rand(3, 3)               #crea una matrice 3x3 con valori casuali uniformi tra 0 e 1
print(random_arr)



sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)

print("sum: ", sum_value)
print("Mean: ", mean_value)
print("Standard Deviation: ", std_value)