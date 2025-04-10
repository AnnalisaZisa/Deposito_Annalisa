import numpy as np

arr = np.linspace(0, 1, 12)            #array equidistante

arr_1 = arr.reshape((3, 4))

matrice_ran = np.random.rand(3, 4)
print(matrice_ran)


sum_arr = np.sum(arr)
print (sum_arr)

sum_matrice = np.sum(matrice_ran)
print(sum_matrice)


#extra
class Array: 

    def __init__(self, righe, colonne, num_elementi, start, stop):
        self.arr = np.linspace(start, stop, num_elementi)
        self.arr_2 = self.arr.reshape(righe, colonne)
        self.arr_3 = self.arr_2.random.rand(righe, colonne)

    def somma_arr (self):
        somma_arr = np.sum(self.arr)
        somma_arr_3 = np.sum(self.arr_3)
        return somma_arr, somma_arr_3
    
    def stampa_info(self):
        print(f"la somma dell'array è: {somma_arr_2} e dell'array 3 è: {somma_arr_3}")
    
    

nuov_arr = Array (0,3,4, 12, 0, 1)
nuov_arr.stampa_info()




