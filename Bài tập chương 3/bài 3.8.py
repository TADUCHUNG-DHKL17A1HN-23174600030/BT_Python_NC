import numpy as np

# Đọc dữ liệu từ tập tin heights.txt
with open('heights.txt', 'r') as file:
    heights = [float(line.strip()) for line in file]

# Đọc dữ liệu từ tập tin positions.txt
with open('positions.txt', 'r') as file:
    positions = [line.strip() for line in file]

# a) Tạo numpy array np_positions từ list positions
np_positions = np.array(positions)
print("Kiểu dữ liệu của np_positions:", np_positions.dtype)

# b) Tạo numpy array np_heights từ list heights
np_heights = np.array(heights)
print("Kiểu dữ liệu của np_heights:", np_heights.dtype)

# 2. Tính chiều cao trung bình của các GK
heights_gk = np_heights[np_positions == 'GK']
avg_height_gk = np.mean(heights_gk)
print("\nChiều cao trung bình của các GK:", avg_height_gk)

# 3. Tính chiều cao trung bình của các vị trí khác (không phải GK)
heights_other = np_heights[np_positions != 'GK']
avg_height_other = np.mean(heights_other)
print("Chiều cao trung bình của các vị trí khác:", avg_height_other)

# 4. Tạo mảng players với cấu trúc tự định nghĩa
players = np.zeros(len(positions), dtype=[('position', 'U5'), ('height', 'f4')])
players['position'] = np_positions
players['height'] = np_heights

# 5. Sắp xếp mảng players theo chiều cao
players_sorted = np.sort(players, order='height')

# Chiều cao cao nhất và thấp nhất
highest = players_sorted[-1]
lowest = players_sorted[0]
print("\nVị trí có chiều cao cao nhất:", highest['position'], "với chiều cao:", highest['height'])
print("Vị trí có chiều cao thấp nhất:", lowest['position'], "với chiều cao:", lowest['height'])
