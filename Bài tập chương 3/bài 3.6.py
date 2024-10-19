import numpy as np

# 1. Tạo array arr có kích thước 3x3 với các giá trị True
arr = np.full((3, 3), True)
print("Bài 1:")
print(arr)

# 2. Tạo arr_1D và chuyển đổi thành arr_2D
arr_1D = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
arr_2D = arr_1D.reshape((3, 3))

# Đổi cột 1 và cột 3
arr_2D[[0, 2], :] = arr_2D[[2, 0], :]
print("\nBài 2:")
print(arr_2D)

# 3. Chuyển đổi dòng 1 và dòng 2
arr_2D[:, [0, 1]] = arr_2D[:, [1, 0]]
print("\nBài 3:")
print(arr_2D)

# 4. Đảo ngược các cột của arr_2D
arr_2D = arr_2D[:, ::-1]
print("\nBài 4:")
print(arr_2D)

# 5. Đảo ngược lại các cột của arr_2D
arr_2D = arr_2D[:, ::-1]
print("\nBài 5:")
print(arr_2D)

# 6. Kiểm tra giá trị rỗng trong arr_2D_null
arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9], [4, 5, 6]])
has_nan = np.isnan(arr_2D_null).any()
print("\nBài 6: Có giá trị rỗng hay không:", has_nan)

# 7. Thay thế giá trị null bằng 0
arr_2D_null = np.nan_to_num(arr_2D_null)
print("\nBài 7:")
print(arr_2D_null)
