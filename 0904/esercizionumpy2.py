import numpy as np
import random

#punto 1
numeri_casuali = np.random.randint(10, 51, 20)


arr = np.array(numeri_casuali)

print(arr)

#punto 2
arr_2 = arr[:11]

#punto 3
arr_3 = arr[15:]

#punto 4
arr_4 = arr[5:15]

#punto 5
arr_5 = arr[::3]

#punto 6
arr_6 = np.array(arr)
arr_6[5:10] = 99

#punto 7
print(arr)
print(arr_2)
print(arr_3)
print(arr_4)
print(arr_5)
print(arr_6)

