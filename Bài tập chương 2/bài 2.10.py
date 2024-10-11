import json

# Đọc dữ liệu từ file json
# Sử dụng r để định nghĩa chuỗi thô hoặc thay \ bằng /
with open(r"Bài tập chương 2\nhan_vien.json", encoding="utf-8") as file:
    du_lieu = json.load(file)

# In thông tin ra màn hình
print(f"Tên công ty : {du_lieu['cong_ty']['ten']}")
print(f"Địa chỉ : {du_lieu['cong_ty']['dia_chi']}")

# Tính số nhân viên
tong_so_nhan_vien = sum(don_vi['so_nhan_vien'] for don_vi in du_lieu['cong_ty']['don_vi'])
print(f"Tổng số nhân viên : {tong_so_nhan_vien}")

# Thống kê nhân viên theo đơn vị
print("--- Thống kê nhân viên theo đơn vị ----")
for don_vi in du_lieu['cong_ty']['don_vi']:
    ten_don_vi = don_vi['ten']
    so_nhan_vien = don_vi['so_nhan_vien']
    ty_le = (so_nhan_vien / tong_so_nhan_vien) * 100
    print(f"Tên đơn vị : {ten_don_vi}")
    print(f"Số nhân viên : {so_nhan_vien}")
    print(f"Tỷ lệ : {ty_le:.2f} %")
