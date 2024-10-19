import numpy as np

arr_a = np.array([1, 2, 3, 4, 5, 6])
arr_b = np.array([7, 2, 10, 2, 9, 4, 9, 8])

# 1. Lấy các phần tử chỉ xuất hiện ở arr_a mà không có trong arr_b
arr_c = np.setdiff1d(arr_a, arr_b)
print("Các phần tử chỉ có trong arr_a:", arr_c)

# 2. Tạo mảng chỉ chứa các phần tử có trong cả arr_a và arr_b
arr_d = np.intersect1d(arr_a, arr_b)
print("Phần tử chung của arr_a và arr_b:", arr_d)

# 3. Tạo arr_e chỉ chứa các phần tử trong [5, 10] của arr_b
arr_e = arr_b[(arr_b >= 5) & (arr_b <= 10)]
print("Các phần tử từ 5 đến 10 trong arr_b:", arr_e)