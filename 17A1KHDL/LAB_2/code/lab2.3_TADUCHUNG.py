import numpy as np

# 1. Đọc dữ liệu từ hai tập tin
hieu_suat = []
with open('efficiency.txt', 'r') as tap_tin:
    for dong in tap_tin:
        hieu_suat.append(int(dong.strip()))

ca_lam_viec = []
with open('shifts.txt', 'r') as tap_tin:
    for dong in tap_tin:
        ca_lam_viec.append(dong.strip())

# 2. Tạo mảng numpy np_ca_lam_viec từ danh sách ca_lam_viec và kiểm tra kiểu dữ liệu
np_ca_lam_viec = np.array(ca_lam_viec)
print("Kiểu dữ liệu của np_ca_lam_viec:", np_ca_lam_viec.dtype)

# 3. Tạo mảng numpy np_hieu_suat từ danh sách hieu_suat và kiểm tra kiểu dữ liệu
np_hieu_suat = np.array(hieu_suat)
print("Kiểu dữ liệu của np_hieu_suat:", np_hieu_suat.dtype)

# 4. Tính hiệu suất sản xuất trung bình của những nhân viên làm việc vào ca 'Morning'
chi_so_ca_sang = np.where(np_ca_lam_viec == 'Morning')
hieu_suat_ca_sang = np_hieu_suat[chi_so_ca_sang]

hieu_suat_trung_binh_ca_sang = np.mean(hieu_suat_ca_sang)
print("Hiệu suất trung bình của ca 'Morning':", hieu_suat_trung_binh_ca_sang)

# 5. Tính hiệu suất trung bình của những nhân viên làm việc trong các ca khác
chi_so_ca_khac = np.where(np_ca_lam_viec != 'Morning')
hieu_suat_ca_khac = np_hieu_suat[chi_so_ca_khac]

hieu_suat_trung_binh_ca_khac = np.mean(hieu_suat_ca_khac)
print("Hiệu suất trung bình của các ca khác 'Morning':", hieu_suat_trung_binh_ca_khac)

