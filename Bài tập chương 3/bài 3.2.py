import numpy as np

# 1. Tạo numpy array với các giá trị từ 0 đến 9
arr = np.arange(10)
print("Mảng arr:", arr)

# 2. Hiển thị kiểu dữ liệu và kích thước của arr
print("Kiểu dữ liệu:", arr.dtype)
print("Kích thước:", arr.shape)

# 3. Tách các phần tử chẵn và lẻ thành 2 mảng arr_odd và arr_even
arr_odd = arr[arr % 2 != 0]
arr_even = arr[arr % 2 == 0]
print("Mảng số lẻ:", arr_odd)
print("Mảng số chẵn:", arr_even)

# 4. Thay thế các phần tử chẵn bằng 100
arr_update = np.where(arr % 2 == 0, 100, arr)
print("Mảng sau khi thay thế:", arr_update)