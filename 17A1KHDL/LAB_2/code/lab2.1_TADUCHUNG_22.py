import numpy as np

# Tạo mảng nhiệt độ ngẫu nhiên (10 đến 35 độ C) và làm tròn đến 2 chữ số
nhiet_do = np.round(np.random.uniform(10, 35, 30), 2)

# In mảng nhiệt độ
print("Dữ liệu nhiệt độ:", nhiet_do)

# Tính nhiệt độ trung bình
nhiet_do_tb = np.mean(nhiet_do)
print("Nhiệt độ trung bình:", nhiet_do_tb)

# Tìm nhiệt độ cao nhất, thấp nhất và ngày tương ứng
cao_nhat = np.max(nhiet_do)
thap_nhat = np.min(nhiet_do)
ngay_cao_nhat = np.argmax(nhiet_do) + 1
ngay_thap_nhat = np.argmin(nhiet_do) + 1
print(f"Nhiệt độ cao nhất: {cao_nhat} (ngày {ngay_cao_nhat})")
print(f"Nhiệt độ thấp nhất: {thap_nhat} (ngày {ngay_thap_nhat})")

# Tìm sự chênh lệch nhiệt độ lớn nhất giữa các ngày
chenh_lech = np.abs(np.diff(nhiet_do))
ngay_chenh_lech_max = np.argmax(chenh_lech) + 1
gia_tri_chenh_lech_max = np.max(chenh_lech)
print(f"Sự chênh lệch lớn nhất: {gia_tri_chenh_lech_max} (ngày {ngay_chenh_lech_max})")

# Các ngày có nhiệt độ trên 20 độ C
ngay_tren_20 = np.where(nhiet_do > 20)[0] + 1
print(f"Ngày có nhiệt độ trên 20 độ C: {ngay_tren_20}")

# Nhiệt độ ngày 5, 10, 15, 20, 25
ngay_chon = [5, 10, 15, 20, 25]
nhiet_do_ngay_chon = nhiet_do[np.array(ngay_chon) - 1]
print(f"Nhiệt độ ngày 5, 10, 15, 20, 25: {nhiet_do_ngay_chon}")

# Nhiệt độ các ngày trên trung bình
ngay_tren_tb = np.where(nhiet_do > nhiet_do_tb)[0] + 1
nhiet_do_tren_tb = nhiet_do[ngay_tren_tb - 1]
print(f"Nhiệt độ trên trung bình: {nhiet_do_tren_tb}")

# Nhiệt độ các ngày chẵn và lẻ
nhiet_do_chan = nhiet_do[1::2]  # Ngày chẵn (chỉ mục lẻ)
nhiet_do_le = nhiet_do[0::2]    # Ngày lẻ (chỉ mục chẵn)
print(f"Nhiệt độ ngày chẵn: {nhiet_do_chan}")
print(f"Nhiệt độ ngày lẻ: {nhiet_do_le}")
