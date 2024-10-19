import requests
import numpy as np

# Đọc dữ liệu từ URL
url_heights = 'http://wiki.stat.ucla.edu/socr/Data/SOCR_Data_MLB_HeightsWeights/heights_1.txt'
url_weights = 'http://wiki.stat.ucla.edu/socr/Data/SOCR_Data_MLB_HeightsWeights/weights_1.txt'

# Tải dữ liệu chiều cao
response_heights = requests.get(url_heights)
if response_heights.status_code == 200:
    # Kiểm tra nội dung phản hồi
    try:
        height = [float(line.strip()) for line in response_heights.text.splitlines()]
    except ValueError as e:
        print("Lỗi khi chuyển đổi chiều cao:", e)
        print(response_heights.text)  # In ra nội dung phản hồi để kiểm tra
else:
    print("Không thể tải dữ liệu chiều cao.")

# Tải dữ liệu cân nặng
response_weights = requests.get(url_weights)
if response_weights.status_code == 200:
    # Kiểm tra nội dung phản hồi
    try:
        weight = [float(line.strip()) for line in response_weights.text.splitlines()]
    except ValueError as e:
        print("Lỗi khi chuyển đổi cân nặng:", e)
        print(response_weights.text)  # In ra nội dung phản hồi để kiểm tra
else:
    print("Không thể tải dữ liệu cân nặng.")

# Kiểm tra xem dữ liệu đã được tải về thành công
if 'height' in locals() and 'weight' in locals() and height and weight:
    # 1. Tạo numpy array arr_height từ list height
    arr_height = np.array(height)

    # 2. Tạo numpy array arr_weight từ list weight
    arr_weight = np.array(weight)

    # 3. Chuyển đổi từ pound sang kg
    he_so_quy_doi = 0.453592
    arr_weight_kg = arr_weight * he_so_quy_doi

    # Tính BMI
    arr_height_m = arr_height * 0.0254  # Chuyển đổi từ inches sang mét
    arr_bmi = arr_weight_kg / (arr_height_m ** 2)

    # Giá trị cân nặng ở vị trí index = 50 trong arr_weight_kg
    can_nang_tai_index_50 = arr_weight_kg[50]

    # Tạo arr_height_m_100 với các phần tử từ index 100 đến 110 (bao gồm cả 110)
    arr_height_m_100 = arr_height_m[100:111]

    # Các cầu thủ có BMI < 21
    cau_thu_bmi_nho_hon_21 = arr_bmi[arr_bmi < 21]

    # Tính chiều cao và cân nặng trung bình
    chieu_cao_trung_binh = np.mean(arr_height_m)
    can_nang_trung_binh = np.mean(arr_weight_kg)

    # Tìm chiều cao và cân nặng lớn nhất
    chieu_cao_lon_nhat = np.max(arr_height_m)
    can_nang_lon_nhat = np.max(arr_weight_kg)

    # Tìm chiều cao và cân nặng nhỏ nhất
    chieu_cao_nho_nhat = np.min(arr_height_m)
    can_nang_nho_nhat = np.min(arr_weight_kg)

    # Các cầu thủ có BMI > 30
    cau_thu_bmi_lon_hon_30 = arr_bmi[arr_bmi > 30]

    # In ra kết quả
    print(f"Cân nặng tại index 50: {can_nang_tai_index_50:.2f} kg")
    print(f"Chiều cao từ index 100 đến 110: {arr_height_m_100}")
    print(f"Cầu thủ có BMI < 21: {cau_thu_bmi_nho_hon_21}")
    print(f"Chiều cao trung bình: {chieu_cao_trung_binh:.2f} m")
    print(f"Cân nặng trung bình: {can_nang_trung_binh:.2f} kg")
    print(f"Chiều cao lớn nhất: {chieu_cao_lon_nhat:.2f} m")
    print(f"Cân nặng lớn nhất: {can_nang_lon_nhat:.2f} kg")
    print(f"Chiều cao nhỏ nhất: {chieu_cao_nho_nhat:.2f} m")
    print(f"Cân nặng nhỏ nhất: {can_nang_nho_nhat:.2f} kg")
    print(f"Cầu thủ có BMI > 30: {cau_thu_bmi_lon_hon_30}")
else:
    print("Dữ liệu không được tải thành công.")
