import numpy as np

# 1. Tạo mảng arr_zeros gồm 10 phần tử toàn 0 và cập nhật phần tử ở vị trí thứ 5 là 1
arr_zeros = np.zeros(10, dtype=int)
arr_zeros[4] = 1  # Cập nhật phần tử thứ 5 (chỉ số bắt đầu từ 0)
print("arr_zeros sau khi cập nhật:", arr_zeros)

# 2. Tạo arr_h có các giá trị từ 0 đến 24 và đảo ngược thứ tự
arr_h = np.arange(25)[::-1]
print("Mảng arr_h sau khi đảo ngược:", arr_h)

# 3. Tạo arr_k với các phần tử không bằng 0
arr_k = np.array([1, 2, 8, 2, 3, 0, 5, 0])
arr_k_non_zero = arr_k[arr_k != 0]
print("Mảng arr_k chỉ có phần tử khác 0:", arr_k_non_zero)

# 4. Thêm 2 phần tử giá trị 10 và 20 vào cuối mảng arr_k
arr_k_extended = np.append(arr_k, [10, 20])
print("Mảng arr_k sau khi thêm phần tử:", arr_k_extended)

# 5. Thêm phần tử giá trị 100 vào vị trí index = 5
arr_k_insert = np.insert(arr_k, 5, 100)
print("Mảng arr_k sau khi thêm 100 vào vị trí index 5:", arr_k_insert)

# 6. Lấy 3 phần tử tại các vị trí index 0, 1, 2
arr_k_slice = arr_k[:3]
print("3 phần tử đầu tiên của arr_k:", arr_k_slice)