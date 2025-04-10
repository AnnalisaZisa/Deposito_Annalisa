import numpy as np


# arr = np.linspace(0, 1, 50)

# arr_1 = np.random.rand (50)

# arr_2 = arr + arr_1
# print(arr_2)

# sum_arr_2 = np.sum(arr_2)

# sum_major_5 = np.sum(arr_2[arr_2>5])
# print(sum_major_5)


class Array_1: 

    def __init__ (self, righe, colonne, num_elementi, start, stop):         #creazione array e array casuale
        self.arr = np.linspace(start, stop, num_elementi)
        self.arr_1 = np.random.rand (righe, colonne)
        self.nuovo_arr = self.arr + self.arr_1                              #creazione nuovo array come la somma tra gli array prec
        print(self.arr)
        print(self.arr_1)
        print(self.nuovo_arr)

    def sum_1 (self):                                                       #definizione somma dei songoli array
        sum_arr = np.sum(self.arr)
        sum_arr_1 = np.sum(self.arr_1)
        sum_nuovo_arr = np.sum(self.nuovo_arr)
        print(sum_arr, sum_arr_1, sum_nuovo_arr) 
                                                                       
    def somma_maggiore_5(self): 
        sum_maggiore_5 = np.sum(self.nuovo_arr(self.nuovo_arr>5))
        print(sum_maggiore_5) 


array_1 = Array_1(1, 50, 50, 0, 1)

