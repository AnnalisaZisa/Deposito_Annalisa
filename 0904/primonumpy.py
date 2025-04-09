import numpy as np

arr = np.array ([1, 2, 3, 4, 5])

arr2d = np.array([[1, 2, 3],[4, 5, 6]])

print(arr)
print(arr2d)

# np.array()
# np.zeros()
# np.ones()
# np.arange()
# np.linspace()

# print("Forma dll'array:", arr2d.shape)
# print("Dimensioni dell'array:", arr.ndim)
# print("Tipo di dati:", arr.dtype)
# print("Numero di elementi:", arr.size)
# print("Somma degli elementi:", arr.sum())
# print("Media degli elementi:", arr.mean())
# print("Valore massimo:", arr.max())
# print("Indice del valore massimo:", arr.argmax())

arr = np.arange(6)
reshaped_arr = arr.reshape((2,3))
print(reshaped_arr)
