import numpy as np 

low_N = -500_000
upper_N = 500_000

arr_np = np.arange(low_N, upper_N)
print(arr_np)

arr_sum_all = np.sum(arr_np)
print(arr_sum_all)

arr1 = np.array([1, 2, 3, 4, 5])

arr_condition = arr_np % 2 == 0
print(np.sum(arr_condition))
