import numpy as np
import csv

# 1. Đọc dữ liệu từ file CSV
file_path = 'diem_hoc_phan.csv'

def doc_du_lieu(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

# Đọc dữ liệu từ file
raw_data = doc_du_lieu(file_path)

# Tách header và dữ liệu
header = raw_data[0]  # Tiêu đề cột
data = np.array(raw_data[1:], dtype=float)  # Loại bỏ tiêu đề, chuyển dữ liệu sang NumPy array

# 2. Chuyển đổi thang điểm 10 sang điểm chữ

# Hàm quy đổi điểm
def quy_doi_diem(diem):
    if 8.5 <= diem <= 10:
        return 'A'
    elif 8.0 <= diem < 8.5:
        return 'B+'
    elif 7.0 <= diem < 8.0:
        return 'B'
    elif 6.5 <= diem < 7.0:
        return 'C+'
    elif 5.5 <= diem < 6.5:
        return 'C'
    elif 5.0 <= diem < 5.5:
        return 'D+'
    elif 4.0 <= diem < 5.0:
        return 'D'
    else:
        return 'F'

# Hàm áp dụng quy đổi cho toàn bộ mảng điểm
def ap_dung_quy_doi(diem_array):
    diem_chu = []
    for diem in diem_array:
        diem_chu.append(quy_doi_diem(diem))
    return np.array(diem_chu)

# 3. Chia tách dữ liệu theo học phần
hp1 = data[:, 2]  # Điểm học phần 1
hp2 = data[:, 3]  # Điểm học phần 2
hp3 = data[:, 4]  # Điểm học phần 3

# 4. Phân tích dữ liệu cho từng học phần

# Hàm phân tích: tính tổng, trung bình, độ lệch chuẩn
def phan_tich_diem(hoc_phan):
    tong = np.sum(hoc_phan)
    trung_binh = np.mean(hoc_phan)
    do_lech_chuan = np.std(hoc_phan)
    return tong, trung_binh, do_lech_chuan

phan_tich_hp1 = phan_tich_diem(hp1)
phan_tich_hp2 = phan_tich_diem(hp2)
phan_tich_hp3 = phan_tich_diem(hp3)

# 5. Phân tích điểm tổng hợp theo điểm chữ

# Hàm thống kê số lượng sinh viên theo điểm chữ
def thong_ke_diem_chu(hoc_phan):
    diem_chu = ap_dung_quy_doi(hoc_phan)
    unique, counts = np.unique(diem_chu, return_counts=True)
    return dict(zip(unique, counts))

tong_hop_hp1 = thong_ke_diem_chu(hp1)
tong_hop_hp2 = thong_ke_diem_chu(hp2)
tong_hop_hp3 = thong_ke_diem_chu(hp3)

# 6. In kết quả
print("Phân tích HP1: Tổng: {}, Trung bình: {:.2f}, Độ lệch chuẩn: {:.2f}".format(*phan_tich_hp1))
print("Phân tích HP2: Tổng: {}, Trung bình: {:.2f}, Độ lệch chuẩn: {:.2f}".format(*phan_tich_hp2))
print("Phân tích HP3: Tổng: {}, Trung bình: {:.2f}, Độ lệch chuẩn: {:.2f}".format(*phan_tich_hp3))

print("Thống kê điểm chữ HP1:", tong_hop_hp1)
print("Thống kê điểm chữ HP2:", tong_hop_hp2)
print("Thống kê điểm chữ HP3:", tong_hop_hp3)
